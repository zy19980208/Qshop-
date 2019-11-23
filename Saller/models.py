from django.db import models
from django.db.models import Manager

# Create your models here.

class LoginUser(models.Model):
    # id不用写
    email = models.EmailField()
    password = models.CharField(max_length=32)
    username = models.CharField(max_length=32,null=True,blank=True)
    #null针对数据库，表示可以为空，即在数据库存储中可以为空
    #blank 针对表单，表示在表单中该字段可以不填，但是对数据库没有影响
    phone_number = models.CharField(max_length=11,null=True,blank=True)
    photo = models.ImageField(upload_to='img',null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(null=True,blank=True,max_length=4)
    address = models.TextField(null=True,blank=True)
    user_type = models.IntegerField(default=1) #0卖家    1买家  2管理员

class MyGoodsType(Manager):
    def myaddtype(self,type_label,type_description,type_picture='images/banner01.jpg'):
        goods_type = GoodsType()
        goods_type.type_label = type_label
        goods_type.type_description = type_description
        goods_type.type_picture = type_picture
        goods_type.save()

class GoodsType(models.Model):
    type_label = models.CharField(max_length=32)
    type_description = models.TextField()
    type_picture = models.ImageField(upload_to='images')
    objects = MyGoodsType()


class MyGoodsFilter(Manager):
    # 自定义方法
    # 自定义查询   查询条件：  id<10 的商品
    def myfilter(self):
        data = Goods.objects.filter(id__lt=10).values('goods_name')
        return data
    def myadd(self,goods_number,goods_name,goods_price,goods_count,goods_location,goods_safe_date,picture):
        goods = Goods()
        goods.goods_number = goods_number
        goods.goods_name = goods_name
        goods.goods_price = goods_price
        goods.goods_count = goods_count
        goods.goods_location = goods_location
        goods.goods_safe_date = goods_safe_date
        goods.picture = picture
        goods.goods_status = 1
        goods.save()

class Goods(models.Model):
    goods_number = models.CharField(max_length=11,verbose_name='商品编号')
    goods_name = models.CharField(max_length=32,verbose_name='商品名字')
    goods_price = models.FloatField(verbose_name='价格')
    goods_count = models.IntegerField(verbose_name='数量')
    goods_location = models.CharField(max_length=254,verbose_name='产地')
    goods_safe_date = models.IntegerField(verbose_name='保质期')
    goods_status = models.IntegerField(verbose_name='状态')
    goods_pro_time = models.DateField(auto_now=True,verbose_name='生产日期')
    picture = models.ImageField(upload_to='images')  #商品图片
    goods_description = models.TextField(default='买不了吃亏，买不了上当！！')


    # 类型  一对多
    goods_type = models.ForeignKey(to=GoodsType,on_delete=models.CASCADE,default=1)
    # 店铺一对多
    goods_store = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE,default=1)

    objects = MyGoodsFilter()

class Vaild_Code(models.Model):
    code_content = models.CharField(max_length=8,verbose_name='验证码')
    code_time = models.FloatField(verbose_name='创建时间')
    code_status = models.IntegerField(verbose_name='状态') # 1--使用  0--未使用
    code_user = models.EmailField(verbose_name='邮箱')



