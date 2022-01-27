# -*- coding: utf-8 -*-
import smtplib
import base64
from email.mime.text import MIMEText#发送纯文本信息
from email.mime.multipart import MIMEMultipart#混合信息
from config import config
import os
import zipfile
import time

def zip_report(input_path,output_path,output_name):
    """将测试报告生成压缩文件"""
    f = zipfile.ZipFile(output_path+'/'+output_name,'w',zipfile.ZIP_DEFLATED)
    files = os.listdir(input_path)
    for file in files:
        if (os.path.splitext(file)[1] == ".html"):
            f.write(input_path + '/' + file)
            f.close()
    return output_path+r"/"+output_name

def send_mail_report(title):
    """将测试报告发送到邮件"""

    """获取测试报告邮件服务器、发件人、收件人等信息"""
    sender = config.sender  # 测试报告邮件发件人邮件地址
    receiver = config.receiver # 测试报告邮件收件人
    server = config.server # 测试报告邮箱服务器smtp服务器
    username = config.emailusername  #测试报告邮件发件人邮箱账户
    password = config.emailpassword # 测试报告邮件发件人邮箱密码


    """获取最新测试报告"""
    reportPath=config.basedir+"/report/"
    newReport = ""
    for root, subdirs, files in os.walk(reportPath):
        for file in files:
            if os.path.splitext(file)[1] == ".html":  # 判断该目录下的文件扩展名是否为html
                newReport=file

    #改变当前的相对路径由 testSuite变更为report,然后压缩report下面的测试报告Report.html文件
    os.chdir(reportPath)
    cwd = os.getcwd()
    print("cwd is:"+cwd)
    zip_report(r"./", './', 'APITestReport.zip') # 将Report.html文件压缩成.zip文件，存放路径为./report

    """生成邮件的内容"""
    msg=MIMEMultipart()
    msg["subject"] = title
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    with open(os.path.join(reportPath, newReport), 'rb') as f:
        mailbody = f.read()
    html = MIMEText(mailbody, _subtype='html', _charset='utf-8')
    msg.attach(html)

    # """生成邮件附件.html文件"""
    # att1 = MIMEText(mailbody, 'base64', 'utf-8')
    # att1["Content-Type"] = 'application/octet-stream'
    # att1["Content-Disposition"] = 'attachment; filename="DFBTestReport.html"' # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    # msg.attach(att1)

    """将测试报告压缩文件添加到邮件附件"""
    att = MIMEText(open('./DFBAPITestReport.zip', 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header("Content-Disposition", "attachment", filename="APITestReport.zip")
    msg.attach(att)

    """发送邮件"""
    msg['from'] = sender
    try:
        smtp = smtplib.SMTP_SSL(server, 465)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver.split(','), msg.as_string())
        smtp.close()
        print ("邮件发送成功")
    except Exception:
        print ("Error :无法发送邮件")
        raise


def send_mail(title,msg):
    # 发件人
    sender = config.sender
    # 收件人
    receiver = config.receiver
    # smtp服务器
    server = config.server
    # 标题
    title = title
    #内容
    message = msg
    # 账户
    username = config.emailusername
    # 密码
    password = config.emailpassword

    msg = MIMEText(message)
    msg["Subject"]= title
    msg["From"] = sender
    msg["To"] = receiver
    # 建立连接
    s = smtplib.SMTP_SSL(server)
    # 认证
    s.login(username,password)
    #发送邮件
    s.sendmail(sender,receiver.split(","),msg.as_string())
    s.quit()
