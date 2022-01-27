#coding=utf-8
from datetime import datetime

from pymongo import MongoClient

class QueryMongo(object):

    def __init__(self):
        self._conn = MongoClient('192.168.214.132', 27017)
        self._db = self._conn.che001
        self._db.authenticate("platform", "platform2018")

    # 根据用户的userid查询用户user信息
    def querySsoId(self, userId):
        print("the userId is: ", userId)
        connection = self._db.user
        user = connection.find_one({"id": userId})
        if user is not None:
            print("the ssoId is: ", user["ssoId"])
        return user

    # 根据用户的ssoId查询用户user信息
    def queryUserId(self, ssoId):
        print("the ssoId is: ", ssoId)
        connection = self._db.user
        user = connection.find_one({"ssoId": ssoId})
        if user is not None:
            print("the userId is: ", user["id"])
        return user

    # 查询用户手机号查询用户user信息
    def queryUserByPhone(self, phone):
        print("the phone is: ", phone)
        connection = self._db.user
        user = connection.find_one({"primaryPhone": phone})
        if user is not None:
            print("the userId is: ", user["id"])
            print("the ssoId is: ", user["ssoId"])
        return user

    # 根据userId、type查询用户的账单日信息
    def queryBillingPlan(self, userId, type):
        connection = self._db.billingPlan
        params = {"userId": userId, "type": type}
        bills = connection.find_one(params)
        if bills is not None:
            print("the id is: ", bills["id"])
        return bills

    # 根据msgid,修改某个字段值
    def updateMsginfo(self, id, key):
        connection = self._db.message
        connection.update ({"id": id}, {'$set': {key: 0}})
        return "10000"


    # 根据ssoId,修改Mongo.user的手机号
    def updatePhone(self, ssoId, primaryPhone):
        connection = self._db.user
        connection.update({"ssoId": ssoId}, {'$set':{primaryPhone: primaryPhone}})
        return primaryPhone


