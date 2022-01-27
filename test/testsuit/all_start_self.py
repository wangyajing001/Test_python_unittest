# -*- coding: utf-8 -*-
import unittest
import os
import time
basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sys
sys.path.append(basedir)
print(basedir)
from lib.HTMLTestRunner3 import HTMLTestRunner
from lib import send_email
from lib.log import logger

def allAPI():
    suite = unittest.defaultTestLoader.discover(basedir + '/test/testcase/', pattern='*.py')
    with open(basedir + "/report/Report.html", "wb") as fp:
        runner = HTMLTestRunner(
        stream=fp,
        title='Api Test Report',
        description='API测试结果'
        )
        runner.run(suite)
    time.sleep(1)
    #send_email.send_mail_report("DFB of Api Test Report!!!")

if __name__ == "__main__":
    logger.info("start to run test case!!!")
    allAPI()
    logger.info("stop to run test case!!!")
