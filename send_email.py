import json
import requests
import pandas as pd
import time
import numpy as np
import os
import re
import datetime
from requests import Request,Session
from matplotlib import font_manager as fm, rcParams
from requests.exceptions import ConnectionError,Timeout,TooManyRedirects
import matplotlib.pyplot as plt
import seaborn as sns
import hashlib
import random
from PIL import Image, ImageDraw, ImageFont
import cv2
from watermarker.marker import add_mark


#======自动发邮件
date_now = datetime.datetime.utcnow()
data_value = str(date_now)[0:10]

# 调用smtplib模块。
import smtplib
# 从email包下的text模块引入MIMEText类，用于构建邮件正文内容。
from email.mime.text import MIMEText
# 从email包下的multipart模块引入MIMEMultipart类，用于构建邮件。
from email.mime.multipart import MIMEMultipart
# 从email包下的application模块引入MIMEApplication类，用于封装附件。
from email.mime.application import MIMEApplication
# 从email包下的header模块引入Header类，用于构建邮件头。
from email.header import Header

# 发件邮箱账号。
sender ='lee_daowei@163.com'
# 发件邮箱开启SMTP服务生成的授权码。
pwd = 'GKXGKVGTYBGRMAVE'
# 收件邮箱账号。
receiver=['lee_daowei@163.com','peng_6149@163.com','2953231494@qq.com','416458731@qq.com']

# mail()函数用来构建邮件。
def mail():
    #创建一个带附件的实例。可通过attach()方法把构造的内容传入到邮件的整体内容中。
    #如果一封邮件中含有附件，那邮件中必须定义multipart/mixed类型。
    #MIMEMultipart()构造方法中的第一个参数，默认值为mixed。定义mixed实现构建一个带附件的邮件体。
    msg=MIMEMultipart('mixed')
    # 定义邮件头信息。发件人、收件人、邮件主题。
    msg['From']=sender
    msg['To']=receiver[0]
    subject=f'{data_value}MMC研究猿比特币现货报告'
    # 为msg对象的Subject属性赋值。
    # 实例化了一个Header邮件头对象，并赋值给msg对象的Subject属性。
    msg['Subject']=Header(subject,'utf-8')
    # 邮件正文内容。
    main_body='此邮件为自动邮件，请勿回复！'
    # 通过attach()方法把构造的内容传入到邮件的整体内容中。
    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain为纯文本)，第三个参数为编码。
    msg.attach(MIMEText(main_body,'plain','utf-8'))
    # 以二进制只读模式打开word文档。
    with open('btc.doc','rb') as docs_file:
        # read()方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。
        # MIMEApplication()构造方法创建附件对象。
        docs_part=MIMEApplication(docs_file.read())
        # 重命名附件为XXX.docx。
        docs_part.add_header('Content-Disposition','attachment',filename=f'{data_value}BTC现货策略数据.docx')
        # 通过attach()方法把构造的内容传入到邮件的整体内容中。
        msg.attach(docs_part)
        # 返回实例。
        return msg

# send_mail()函数用来发送邮件。
def send_mail(content):
    # qq邮箱SMTP服务器。
    mailhost='smtp.163.com'
    # 开启发信服务，这里使用的是加密传输。
    server=smtplib.SMTP_SSL(mailhost)
    server.connect(mailhost,465)
    # 登录指定邮箱。
    server.login(sender,pwd)
    # 获取邮件的内容。
    msg=content
    try:
        # 发送邮件。
        server.sendmail(sender,receiver,msg.as_string())
        print('邮件发送成功！')
    except:
        print('邮件发送失败！')
    # 退出登录。
    server.quit()

# 在 if __name__ == 'main': 下的代码只有在文件作为脚本直接执行时才会被执行，
# 而 import 到其他脚本中是不会被执行的。
if __name__=='__main__':
    send_mail(mail())