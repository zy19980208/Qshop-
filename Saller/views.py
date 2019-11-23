from django.shortcuts import render
from Saller.models import *
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import hashlib
from django.core.paginator import Paginator


#登录装饰器
def LoginVaild(func):
    def inner(request,*args,**kwargs):
        username = request.COOKIES.get('username')
        # 获取session
        session_username = request.session.get('username')
        if username and session_username and username == session_username:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/Saller/login/')
    return inner
def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()

    return result

# Create your views here.
def register(request):
    if request.method == 'POST':
        error_msg=''
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email:
            # 判断邮箱是否存在
            loginuser = LoginUser.objects.filter(email=email).first()
            if not loginuser:
                #不存在 写库
                user = LoginUser()
                user.email = email
                user.username = email
                user.password = setPassword(password)
                user.user_type = 0
                user.save()
            else:
                error_msg = '邮箱已经被注册，请登录'
        else:
            error_msg = '邮箱不可以为空'

    return render(request,'saller/register.html',locals())



def login(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        code = request.POST.get('vaild_code')
        if email:
            user = LoginUser.objects.filter(email=email,user_type=0).first()
            if user:
                if user.password==setPassword(password):
                    vaild_code = Vaild_Code.objects.filter(code_status=0,code_user=email,code_content=code).last()
                    if vaild_code:
                        if time.time() - vaild_code.code_time < 120:
                            response = HttpResponseRedirect("/Saller/index/")
                            response.set_cookie("username", user.username)
                            response.set_cookie("user_id", user.id)
                            request.session['username'] = user.username  ## 设置session
                            vaild_code.code_status = 1
                            vaild_code.save()
                            return response
                        else:
                            error_msg = '验证码超时，请重新获取'
                    else:
                        error_msg = '验证码不正确'
                else:
                    error_msg = '密码错误'
            else:
                error_msg = '该用户不存在，请先注册'
        else:
            error_msg = '邮箱不可为空'
    return render(request,'saller/login.html',locals())

@LoginVaild
def index(request):
    return render(request,'saller/index.html')

# 登出
def logout(request):
    # 删除cookie  删除session
    response = HttpResponseRedirect('/Saller/login/')
    # response.delete_cookie('kname')
    keys = request.COOKIES.keys()
    for one in keys:
        response.delete_cookie(one)
    del request.session['username']
    return response

def goods_list(request,status,page):
    page = int(page)
    if status == '0':
        goods_obj = Goods.objects.filter(goods_status = 0).order_by('goods_number')
    else:
        goods_obj = Goods.objects.filter(goods_status = 1).order_by('goods_number')
    goods_all = Paginator(goods_obj,10)
    page = goods_all.page(page)


    return render(request,'saller/goods_list.html',locals())

def goods_status(request,status,id):
    '''
    完成当下架的时候修改status为0
    当上架的时候修改status为1
    :param request:
    :param status: 操作内容 up上架  down下架
    :param id:商品id
    :return:
    '''

    id= int(id)
    goods = Goods.objects.get(id=id)
    if status == 'up':
        # 上架
        goods.goods_status = 1
    else:
        # 下架
        goods.goods_status = 0
    goods.save()
    # return HttpResponseRedirect('/goods_list/1/1')
    url = request.META.get('HTTP_REFERER','/Saller/goods_list/1/1/')
    return HttpResponseRedirect(url)

@LoginVaild
def personal_info(request):

    user_id =  request.COOKIES.get('user_id')

    user = LoginUser.objects.filter(id=user_id).first()
    if request.method=='POST':
        data = request.POST
        user.username = data.get('username')
        user.phone_number = data.get('phone_number')
        user.age = data.get('age')
        user.gender = data.get('gender')
        user.address = data.get('address')
        if request.FILES.get('photo'):
            user.photo = request.FILES.get('photo')
        user.save()
    return render(request,'saller/personal_info.html',locals())
@LoginVaild
def goods_add(request):
    # 处理post请求，获取数据，保存数据，返回响应
    goods_type = GoodsType.objects.all()
    if request.method == 'POST':
        data = request.POST
        print(data)
        goods = Goods()
        goods.goods_number = data.get('goods_number')
        goods.goods_name = data.get('goods_name')
        goods.goods_price = data.get('goods_price')
        goods.goods_count = data.get('goods_count')
        goods.goods_location = data.get('goods_location')
        goods.goods_safe_date = data.get('goods_safe_date')
        goods.picture = request.FILES.get('picture')
        goods.goods_status = 1
        goods.save()
        goods_type = request.POST.get('goods_type')  # select标签的value  类型是string
        # goods.goods_type_id = int(goods_type)
        goods.goods_type = GoodsType.objects.get(id = goods_type)  # 保存类型
        # 保存店铺
        # 从cookie中获取到用户信息
        user_id = request.COOKIES.get('user_id')
        goods.goods_store = LoginUser.objects.get(id = user_id)
        goods.save()
    return render(request,'saller/goods_add.html',locals())

import smtplib
from email.mime.text import MIMEText

def send_email(params):
    # params 字典类型
    subject = params.get('subject')
    content = params.get('content')
    sender = 'zyzy3021@163.com'

    rec = params.get('toemail')

    password = 'zy123456'
    message = MIMEText(content,'plain','utf-8')
    message['Subject'] = subject
    message['From'] = sender # 发件人
    message['To'] = str(rec) # 收件人
    try:
        smtp = smtplib.SMTP_SSL('smtp.163.com',465)
        smtp.login(sender,password)
        smtp.sendmail(sender,rec.split(","),message.as_string())
        smtp.close()
        return True
    except:
        return False


import random
import time
def get_code(request):
    result = {"code":10000,"msg":""}
    # 获取email
    email = request.GET.get("email")
    # 判断用户是否存在
    if email:
        # 判断email是否有值
        flag = LoginUser.objects.filter(email=email).first()
        if flag:
            # 用户存在
            # 发送验证码
            code = random.randint(1000,9999)
            # print(code)
            content = "悄摸的告诉您，您的验证码是%s"%(code)
            print(content)
            params = dict(subject="登录验证码",content=content,toemail=[email])
            # eflag = send_email(params)
            # if eflag:
            # 保存验证码到数据库
            vaild_code = Vaild_Code()
            vaild_code.code_content = code
            vaild_code.code_status = 0
            vaild_code.code_user = email
            vaild_code.code_time = time.time()
            vaild_code.save()
            result = {"code":10000,"msg":"验证码发送成功"}
            # else:
            #     result = {"code": 10003, "msg": "不晓得啥问题，看着办吧"}
        else:
            # 用户不存在
            result = {"code":10002,"msg":"用户不存在"}
    else:
        result = {"code":10001,"msg":"邮箱不能为空"}

    return


def ormobjectstest(request):
    # 对goods模型进行操作
    data = Goods.objects.all()
    # queryset 全部的数据  全部的字段
    data = Goods.objects.myfilter()
    print(data)
    return HttpResponse('ormobjectstest')

from Buyer.models import *
# 商品订单页
@LoginVaild
def order(request,status):
    ## status 订单状态  字符串0 1 2 3
    status = int(status)
    # 查询该用户的所有订单
    # 获取登录用户
    user_id = request.COOKIES.get('user_id')
    user = LoginUser.objects.get(id=user_id )
    # # 卖家订单详情
    order_info = OrderInfo.objects.filter(store_id=user,status = status).all()
    # # 根据卖家id  找到订单详情
    # order_info = OrderInfo.objects.filter(store_id=1).first()
    # payorder = order_info.order_id
    # buyer_user = payorder.order_user
    # # 反向找地址
    # buyer_address = buyer_user.useraddress_set.first()

    # address = order_info.order_id.order_user.useraddress_set.first()




    return render(request,'saller/order.html',locals())

def sendemail(request):
    """
     使用ajax
    :param request:
    :return:
    """
    # 订单详情id
    order_info_id = request.GET.get('order_info_id')
    # 找到买家的邮箱
    # 使用异步发送邮件
    # 发送邮件
    return HttpResponse('发送邮件成功')

def seller_caozuo(request):
    """
    拒绝订单
    :param request:
    :type
        拒绝   修改订单详情状态
        发货
    :return:
    """
    type = request.GET.get('type')
    order_info_id = request.GET.get('order_info_id')
    order_info = OrderInfo.objects.get(id = order_info_id)
    if type == 'jujue':
        order_info.status = 4
        order_info.save()
    elif type == 'fahuo':
        order_info.status = 2
        order_info.save()

    url = '/Saller/order/1'
    return HttpResponseRedirect(url)

