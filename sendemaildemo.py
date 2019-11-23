import smtplib
from email.mime.text import MIMEText

# 构建邮箱
# 主题
subject = "0715测试demo"
# 内容
content = '你猜我是谁^_^'
# 发件人
sender = 'zyzy3021@163.com'
# 接收人  单个 多个收件人
rec = """985439276@qq.com,
ljljlj23@163.com
"""

password = 'zy123456'
# MIMEText 参数 发送内容，内容类型
message = MIMEText(content,'plain','utf-8')
message['Subject'] = subject
message['From'] = sender # 发件人
message['To'] = rec # 收件人


# 发送邮件
smtp = smtplib.SMTP_SSL('smtp.163.com',465)
smtp.login(sender,password)
# 参数说明  发件人  收件人  发送邮件  类似一种json的格式
smtp.sendmail(sender,rec.split(",\n"),message.as_string())
smtp.close()

