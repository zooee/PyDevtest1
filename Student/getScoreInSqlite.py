#coding=utf-8
'''
Created on 2016年5月9日

@author: Administrator
'''
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)
# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('select * from user where score between ? and ? order by score', (low, high))
    result = cursor.fetchall()
    print (result)
    result = sorted(result, key = lambda t:t[2])
    names = [row(1) for row in result]
    #print (names)
    cursor.close()
    conn.close() 
print (get_score_in(60, 100))   
