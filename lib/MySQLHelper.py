#coding=utf-8

import pymysql
import config.config as config
from lib.log import logger
import json
class MySQLHelper(object):

    def __init__(self, dbName):
        if dbName == "backend":
            self.conn = config.backend


    #查询返回只有一条结果
    def get_one(self, sql, params):
        conn = pymysql.connect(**self.conn)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        print('the sql is :', sql)
        print('the params is : ', params)
        #cur = conn.cursor()
        cur.execute(sql, params)
        data = cur.fetchone()
        cur.close()
        conn.close()
        print('the result data is :', data)
        return data

    def get_many(self, sql, params):
        conn = pymysql.connect(**self.conn)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        print('the sql is :', sql)
        print('the params is : ', params)
        cur.execute(sql, params)
        data = cur.fetchall()
        cur.close()
        conn.close()
        print('the result data is :', data)
        return data

    def insert_one(self, sql, params):
        conn = pymysql.connect(**self.conn)
        cur = conn.cursor()
        print('the sql is :', sql)
        print('the params is : ', params)
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()
        return u'插入数据库成功'

    def insert_many(self, sql, params):
        conn = pymysql.connect(**self.conn)
        print('the sql is :', sql)
        print('the params is : ', params)
        cur = conn.cursor()
        cur.executemany(sql, params)
        conn.commit()
        cur.close()
        conn.close()
        return u'批量插入数据库成功'

    def update_one(self,sql,params):
        conn = pymysql.connect(**self.conn)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        print('the sql is :', sql)
        print('the params is : ', params)
        ret = cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()
        return u'更新数据库成功'

    def delete_one(self, sql, params):
        conn = pymysql.connect(**self.conn)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        print('the sql is :', sql)
        print('the params is : ', params)
        ret = cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()
        return u'删除数据库成功'


    def selectsql(self,sql):
        con = pymysql.connect(**self.conn)
        cursor = con.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        con.close()
        return data

    def updatesql(self,sql):
        con = pymysql.connect(**self.conn)
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            logger.info(sql)
            con.commit()
        except Exception as e:
            con.rollback()
            logger.error(e.message)




    def selectsql_json(self, sql):
        con = pymysql.connect(**self.conn)
        cursor = con.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        con.close()
        return data


if __name__ == '__main__':
    sql="select * from pm_park where park_name='YJ停车场'"
    result1 = MySQLHelper("backend").selectsql(sql)
    print(result1[0])

