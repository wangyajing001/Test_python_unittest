# -*- coding: utf-8 -*-
import hashlib
import requests
from datetime import datetime

host1="http://172.16.100.22:8052"


def sendWX(content):
    hash = hashlib.md5(bytes("content="+content+"&signature=sig-jiankong"+"&touser=loadkernel|jonekoko"+"&toparty=@all"+"&totag=@all"+"05689958-f643-4c9c-b869-21501459260e", encoding='utf-8'))
    print(hash.hexdigest())
    # print(sign.digest())
    #sign = hashlib.md5("content="+content+"&signature=sig-jiankong"+"&touser=loadkernel|jonekoko"+"&toparty=@all"+"&totag=@all"+"05689958-f643-4c9c-b869-21501459260e")
    # print(sign.hexdigest())
    url1 = "/callservice/sender/weiChatTxt?content="+content+"&signature=sig-jiankong&touser=loadkernel|jonekoko&toparty=@all&totag=@all&sign="
    r=requests.post(host1+url1+hash.hexdigest())
    print(r.json())

def GetMiddleStr(content,startStr,endStr):
  startIndex = content.index(startStr)
  if startIndex>=0:
    startIndex += len(startStr)
    endIndex = content.index(endStr)
  return content[startIndex:endIndex]

if __name__ =="__main__":
    # files = open("D:\\SmokeApiTest20170804\\report\\Report.html", 'r',encoding="utf-8")
    files = open("C:\\Users\\Administrator\\.jenkins\\jobs\\DFB_Smoke_API_Test\\workspace\\report\\Report.html", 'r',encoding="utf-8")
    lines = files.read().encode('utf-8')
    # print(lines)
    passed = lines.decode("utf-8").split("<tr id='total_row'>")[1].split("class=\"text text-success\">")[1].split("</td>")[0]
    failed = lines.decode("utf-8").split("<tr id='total_row'>")[1].split("class=\"text text-danger\">")[1].split("</td>")[0]
    errors = lines.decode("utf-8").split("<tr id='total_row'>")[1].split("class=\"text text-warning\">")[1].split("</td>")[0]
    # print(failed)
    #[1].split("<td>")[3].split("<")[0]
    # failed = lines.decode("utf-8").split("<tr id='header_row'>")[1].split("<td>")[4].split("<")[0]
    # errors = lines.decode("utf-8").split("<tr id='header_row'>")[1].split("<td>")[5].split("<")[0]

    #print passed,failed

    sendWX("环境:【Ultimate环境】\n平台:垫付宝\n类型:自动化测试\n时间:"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\n"+"执行结果:成功="+passed+" 错误= "+errors+" 失败="+failed)