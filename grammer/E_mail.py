from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib
import random
import string


# 3401487400（高校论坛管理员）
# 'campusforum@qq.com'    '1429532958@qq.com', '1072120607@qq.com'
# iminfexpazdqcade
# 发送邮件服务器：smtp.qq.com，使用SSL，端口号465或587


def verify_code(leng=6):
    chars = string.digits
    code = ''
    for j in range(leng):
        code += random.choice(chars)
    return code


# 输入Email地址和口令:
from_addr = '373104598@qq.com'
# 输入收件人地址:
to_addr = 'campusforum@qq.com'
# 授权码
password = 'iminfexpazdqcade'
# 输入SMTP服务器地址:
smtp_server = 'smtp.qq.com'

msg = MIMEText(u'【高校论坛】邮箱验证码{0}用于注册个人账号,如非本人操作，请忽略此邮件。'.format(verify_code()), 'plain', 'utf-8')
msg['From'] = u'高校论坛管理员<%s>' % from_addr
msg['To'] = u'管理员<%s>' % to_addr
msg['Subject'] = Header(u'注册邮箱验证码@【高校论坛】', 'utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
