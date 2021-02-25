#!/usr/bin/python
# -*- coding: UTF-8 -*-


import MySQLdb

db=MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root123",db="test",charset='utf8')
cursor=db.cursor()


cursor.execute("select version()")
data=cursor.fetchone()
print "database version :%s"%data

sql="""create table t4(id int not null)"""
cursor.execute(sql)


sql2="""insert into t4 values(11,)"""
try:
    cursor.execute(sql2)
    db.commit()
except:
    db.rollback()
db.close()
