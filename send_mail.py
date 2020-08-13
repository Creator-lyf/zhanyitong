# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header

# 用于构建邮件头

def send_notice_mail(to_addr,name,timesss,cishu,timessss): # timesss到秒，timessss到日 to_addr是被发送的邮箱地址
    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = '写邮箱'
    password = '写密码(此密码非彼密码，这里写授权码)'


    # 发信服务器
    smtp_server = 'smtp.qq.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    text = name + '同学，您好，\n 据悉，截止'+ timesss + '，您还没有完成'+timessss+'的战役通打卡，您的累计未打卡次数为'+str(cishu)+'。\n 请尽快完成打卡并注意明日及时打卡(应学工办要求，希望每位同学都能在每日早10：30前完成打卡)。辛苦了。\n【银河二号】'
    msg = MIMEText(text, 'plain', 'utf-8')

    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('【战役通打卡温馨提醒】')

    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL('smtp.qq.com')
    server.connect(smtp_server, 465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()
    pass


def send_user_mail(text):
    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = '写邮箱'
    password = '写密码(此密码非彼密码，这里写授权码)'

    # 收信方邮箱
    to_addr = '收件方邮箱'

    # 发信服务器
    smtp_server = 'smtp.qq.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText(text, 'plain', 'utf-8')

    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('【发给老师的】')

    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL('smtp.qq.com')
    server.connect(smtp_server, 465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()
    pass

