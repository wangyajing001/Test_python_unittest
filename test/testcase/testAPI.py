#coding=utf-8
# Author: Wendy
import json
import  requests
from config import url
import unittest
from lib.generateTestCases import __generateTestCases

class testAPI(unittest.TestCase):
    u"入位接口"
    def setUp(self):
        print("———————入位开始————————-")

    def getTest(self,tc_data):#定义的函数，最终生成的测试用例的执行方法
        tc_num=tc_data["tc_num"]
        tc_name=tc_data["tc_name"]
        print(tc_num+" "+tc_name)
        status_code1=int(tc_data["code"])
        print(status_code1)
        # info = json.JSONDecoder().decode(tc_data["params"])
        # reqUrl =url.url+"/sbdevice/dataEvt/receive"
        # headers = {'content-type': 'application/json'}
        # req = requests.post(reqUrl, json=info,headers=headers)
        # json_data = json.loads(req.text)
        # print(json_data)
        # self.assertEqual(json_data["isSuccess"], str(status_code1))

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            """ 单例模式"""
            self.getTest(arg1)
        return func

    def tearDown(self):
        print("------人位结束------")


__generateTestCases(testAPI,"testAPI","testAPI.xlsx","testAPI")

if __name__ == '__main__':
    unittest.main()


