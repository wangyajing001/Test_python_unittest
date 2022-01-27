# -*- coding:utf-8 -*-
import os

#数据库配置
backend = dict(host='rm-2ze0bl5fv0r771lemno.mysql.rds.aliyuncs.com', user='yangjing', passwd='c5221b65f5421626', port=3306,db='tc_rongyi', charset='utf8')

#邮件配置
sender = ''#发送方
receiver=''#接受方
emailusername = ''#登陆邮箱的用户名
emailpassword = ''#登陆邮箱的授权码
server = ''#smtp服务器

#数据目录
datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data')

# os.path.abspath(path) #返回绝对路径
# os.path.basename(path) #返回文件名
# os.path.dirname(path) #返回文件路径
# os.path.join(path1[, path2[, ...]])  #把目录和文件名合成一个路径

#项目配置
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#日志配置
import logging
logpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'log')
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%y-%m-%d %H:%M',
                    filename=os.path.join(logpath,'log.txt'),
                    filemode='a')



