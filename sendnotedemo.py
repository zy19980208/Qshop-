import requests      ###   http 库  pip install requests

## 请求地址
url = "http://106.ihuyi.com/webservice/sms.php?method=Submit"

#APIID
account = "C22844973"
#APIkey
password = "31b8e890f4b2304ee71e886b2905356f"

## 收件人手机号
mobile = "17803373102"
## 短信内容
content = "您的验证码是：1111。请不要把验证码泄露给其他人。"
## 请求头
headers = {
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"
}
## 构建发送参数
data = {
    "account": account,
    "password": password,
    "mobile": mobile,
    "content": content,
}
## 发送
response = requests.post(url,headers = headers,data=data)
    #url    请求地址
    #headers  请求头
    #data 请求数据  内容

print(response.content.decode())