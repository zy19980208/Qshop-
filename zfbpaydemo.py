from alipay import AliPay

# 公钥
alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA64MmgYBsiDjFVUFPi+ZMkAx0SyeVe43pjhY7CJ28Tuhf7pjXJC9uKuecoqg7GbpSDJSufm+nAkpD1MYqTQFCqRps/e6+MYvIXysHq+hpPLrBnU8VydFmE5t0geCb3tysQbb+qLN8eh9YsJPOjHfG7Fyxp45vmEmyeHvWCLYXs4cjDauqfIrHMJ/KnCDS/bVVyxv6X4Cs0pAsASu1UXL+c9tXNSuFLRh8lNh4LkTTpVmzf4oE5rFoPaYJm8VXRbCqvgh37w5avjCx1hhbUdT8wAKEkPXpjNEsog0uyw8IomBRICnYvaSkcgx1EeCzW8kLW1xvzPsiYRGlJtaRxw0FiwIDAQAB
-----END PUBLIC KEY-----"""


# 私钥
alipay_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEpgIBAAKCAQEA64MmgYBsiDjFVUFPi+ZMkAx0SyeVe43pjhY7CJ28Tuhf7pjXJC9uKuecoqg7GbpSDJSufm+nAkpD1MYqTQFCqRps/e6+MYvIXysHq+hpPLrBnU8VydFmE5t0geCb3tysQbb+qLN8eh9YsJPOjHfG7Fyxp45vmEmyeHvWCLYXs4cjDauqfIrHMJ/KnCDS/bVVyxv6X4Cs0pAsASu1UXL+c9tXNSuFLRh8lNh4LkTTpVmzf4oE5rFoPaYJm8VXRbCqvgh37w5avjCx1hhbUdT8wAKEkPXpjNEsog0uyw8IomBRICnYvaSkcgx1EeCzW8kLW1xvzPsiYRGlJtaRxw0FiwIDAQABAoIBAQDDxkcpGeeeqYqon10Pz8bPa/r0SpiBl+uRmLtEI1NZSOQORHF7fA4ZjmVv9WcDsRXprWMMaaYsSi3u3zhkwOp4BiaaRG9IYomTSwLajZ2FxT2Tlh1nojE3lV+ZY2xPK6PqEMPK20Fbh1lDl+r4a80pyLhJsCbmMkUw0MiQf0ZejhxwcKEzw4PIJuUTgCpF8f03lh/MJWdluyYAOcUct00if1ktkOvQjxzyEXzZeUnIxHECvbX0xX6OhObGVE5spkAD9UOdUC3BpIEb1z4JjdDf8zhvaDlsWV5zpvdeKeQPRDFTB2vd0Zohh4hQ6TdQRw8vaZPbL8qea+0ROEEke4YZAoGBAPpEUqDuRWdmab/CSddID6Kc8qwQMZHvpRASwIkdZu+k+TImVySIBJ8fc9rqZbIOhrVhS2d8zaBubQEW+It4qccpefjkAbmFHW08oBHS+ab7nksahJlNJBz99GrpzAAPvTAR33+5tAXEN63oXtJvcX9/lrUDueGD4frDhHAQIbenAoGBAPDoTNhOyb1Irt5CfJapFeAFTl7JwsURHfHdFIej1ygTb4gTruoyt4pROOsMf0wiWPpadHZ7/3E75BxKktWZP+BEOF+51iOgmouuNu2vsKkuZakaygJNgZ6GcZdjfYa8sU7gE41v3GoEHLY+Uli5L6/N1z3kF8aUVFWxA3e/Af99AoGBAOQUhjVyUUA13qRLXd5cJxus66CSNYrpm0X1wRB1Ak3ezNi+hmadq5CVKpHVUw8eG/iLjhvnasMOQDthAuyg8CG5FBcXPNclkLbwLHVyD+H1qMKLjVLlMcdWTn1tS2S281UuxMBzrrQeqhvNDTW9KPPohKG9npb/CWDu9PDoUsI7AoGBANy/sLLBN4E4GezWNb4EgGP/2Llo3g2gSrU3JTnJez1g2eFyT+SQxrh7BtHzaK5GBwyZWIC9zOtguvzlpLkPrYV+Xb3x1vRclWELKZARXqsYNdWIE7WaefzeKzZS11Jgk4S4NZJz/yAyVnD0mJZuUvEgiGxRFyxC/ShshMX0hAstAoGBALs1m3OGpnf0b/z3Bt3S9X/7aszZA9hhaFFm24e1nqEDS92A8FVMhCM9V6p9eg0Cx83L4I2A0x5B/qYuDtpYpk1gtFTGZfpxMeqvaV1JVf72k4TWT9ixQ/123S8BXSHue7L4SFJEI6X9SAHR1o1m595w53gCIT96VMUl1oFLhYwU
-----END RSA PRIVATE KEY-----"""

# 实例化支付对象
alipay = AliPay(
        appid = '2016101300673955',
        app_notify_url=None,
        app_private_key_string=alipay_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",
)
# 实例化订单
order_string = alipay.api_alipay_trade_page_pay(
    subject = '牛羊生鲜',  # 交易主体
    out_trade_no= '10000000000', # 订单号
    total_amount = '100', # 交易总金额
    return_url = None,  # 请求支付，之后及时回调的一个接口
    notify_url = None  # 通知地址
)

# 发送支付请求
# 请求地址  支付网关 + 实例化订单
result = 'https://openapi.alipaydev.com/gateway.do?'+order_string
print(result)

