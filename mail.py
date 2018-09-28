from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
import smtplib

message ='''
hello，world！
来自我的电脑
'''


msg = MIMEMultipart()

msg['Subject'] = Header("来自Python的邮件",'utf-8')
msg['From'] = Header('1690697629@qq.com')
msg['To'] = Header('receiver','utf-8')

part = MIMEText(message,'plain','utf-8') 
msg.attach(part)

part = MIMEApplication(open('ISSM Invitaiton Letter.pdf','rb').read())  
part.add_header('Content-Disposition', 'attachment', filename="ISSM Invitaiton Letter.pdf")  
msg.attach(part) 

from_addr = '1690697629@qq.com' #发件邮箱
password = 'wsmrutdgfhzfdjhi' #邮箱密码
to_addr =[ '1093593298@qq.com','1690697629@qq.com'] #收件邮箱

smtp_server = 'smtp.qq.com' #SMTP服务器，以新浪为例

try:
    server = smtplib.SMTP_SSL(smtp_server,465) #第二个参数为默认端口为25，有些邮件有特殊端口
    print('开始登录')
    server.login(from_addr,password) #登录邮箱
    print('登录成功')
    print("邮件开始发送")
    server.sendmail(from_addr,to_addr,msg.as_string())  #将msg转化成string发出
    server.quit()
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("邮件发送失败",e)

