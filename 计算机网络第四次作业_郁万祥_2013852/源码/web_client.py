# TCP客户机程序：web_client.py

import time
from socket import *
import numpy as np
serverName = "192.168.149.1"  # 服务器主机
serverPort = 6121         # 端口号
clientsocket = socket(AF_INET,SOCK_STREAM)      # 创建客户机套接字
clientsocket.connect((serverName,serverPort))   # 建立连接
## 发送请求报文并接收服务器的回复
fetch_file = "/myfile1.html"  # 需要请求的文件
requestRow = "Get "+fetch_file+" HTTP/1.1\r\n"   # 请求行
firstRow = "Host:10.10.1.218\r\nUser-agent:Microsoft Edge/100.0.1185.36\r\nConnection:open\r\nAccept-language:ch\r\n\r\n"  # 首部行
requestMessages = requestRow+firstRow   # 请求报文（请求行+首部行）
print("请求报文发出时间:",time.strftime("%Y-%m-%d %H:%M:", time.localtime(time.time())),np.mod(time.time(),60),sep="")

start = time.perf_counter()
clientsocket.send(requestMessages.encode())   # 发送请求报文
responseMessage = clientsocket.recv(1024)     # 接收服务器的回复
end = time.perf_counter()
print("RTT:",end-start,"s")

print("响应报文：\n",responseMessage.decode(),sep = "")
## 生成本地html文件
f = open('localHtml.html','w')
message = responseMessage.decode()   # 报文解码
message = message.split("\r\n")      # 解析报文
content = message[-1]                # 获取向服务器申请的文件
f.write(content)      # 保存到本地文件中
f.close()
## 关闭套接字
clientsocket.close()
