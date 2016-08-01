#coding=utf-8
'''
Created on 2016年4月22日

@author: Administrator
'''

import hashlib
#注册
db={}
username = input('请输入用户名：')
password = input('请输入密码：')

def get_md5(password):
    psdmd5=hashlib.md5()
    psdmd5.update(password.encode('utf-8'))
    return(psdmd5.hexdigest())

def register():
    db[username] = get_md5(password + username + 'the-Salt')
    print('注册成功')


register()

#登陆
username1 = input('请输入登陆用户名：')
password1 = input('请输入登陆密码：')
def login():
    if username1 in db:
        if db[username1] == get_md5(password1 + username1 + 'the-Salt'):
            print('登陆成功！')
        else:
            print('登陆密码错误！')
    else:
        print('登陆用户名错误！')

login()