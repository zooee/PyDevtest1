#coding=utf-8
'''
Created on 2016年5月12日

@author: Administrator
'''
def application(environ, start_response):
    start_response('200 OK', [('content_type', 'text/html')])
    body = '<h1>First web by %s~</h1>' % (environ['PATH_INFO'][1:] or 'web') 
    return [body.encode(encoding='utf_8', errors='strict')]