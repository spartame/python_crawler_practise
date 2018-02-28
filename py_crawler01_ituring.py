import http.client
import socket    #gaierror用
import re     #正则表达式用

conn = http.client.HTTPConnection('www.ituring.com.cn')#主机地址

try:
    conn.request('GET', '/book?tab=book&sort=new')    #请求方法和资源路径
    response = conn.getresponse()    #获得回复
    #print(response.status, '\n', response.reason)    #回复的状态码和状态描述
    content = response.read()    #回复的主体内容
    
    #print(content.decode('utf-8'))
    content = content.decode('utf-8')    #将回复内容转码成utf-8
    content = content.split('\r\n')
    #print(content)
    
    pattern = '<h4 class="name"><a href="/book/([0-9]*)" title="(.+)">'    #使用正则表达式提取出书名, 编号
    #<h4 class="name"><a href="/book/2020" title="HTTP/2基础教程">
    
    print('编号         书名')
    
    for line in content:
        m = re.search(pattern, line)
        if m != None:
            #print(m.group(0))
            print(m.group(1), ' ', m.group(2))
        
except socket.gaierror as e:
    print('Please check your Internet connection!')
    print('无法连接至网络，请重试')