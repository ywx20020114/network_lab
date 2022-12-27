# TCP服务器程序：web_Server.py


import time
import numpy as np
from socket import *
import os
serverSocket = socket(AF_INET,SOCK_STREAM)    # 生成服务器的TCP连接套接字
serverPort = 6121     # 端口号
serverSocket.bind(("",serverPort))  # 绑定服务器套接字和端口号
serverSocket.listen(10)
print("服务器已启动，正在提供服务......")
while True:
    connectionSocket,address = serverSocket.accept()   # 根据客户创建一个TCP连接
    try :
        # 接收请求报文并读取文件
        message = connectionSocket.recv(1024).decode()  # 接收客户机的请求报文
        print("接收到请求报文的时间:",time.strftime("%Y-%m-%d %H:%M:", time.localtime(time.time())),np.mod(time.time(),60),sep="")
        print("已接收到请求报文：\n", message)
        filename = message.split()[1] # split('') 把一个字符串分割成字符串数组把数据拆分为一个数组,括号里的' '是把数据拆分为每个字符串解析请求报文，获取文件名
        # print(message.split())
        # print("该请求请求文件：{}".format(filename))
        print(filename)
        with open(filename[1:], "r") as f:
            content = f.read()     # 根据文件名读取文件内容
        ## 生成响应报文（状态行+首部行+文件内容）
        stateRow = "HTTP/1.1 200 OK\r\n"     # 状态行
        firstRow = "Connection open\r\nDate:"+time.strftime("%Y-%m-%d",time.localtime(time.time()))+"\r\n服务器:Apache/1.3.0 (Windows)\r\nLast-Modified:monday,28 November 2022\r\nContent-Length:"+str(len(content))+"\r\nContent-Type:html\r\n\r\n"  # 首部行
        outputdata = stateRow+firstRow+content  # 响应报文=状态行+首部行+文件内容
        connectionSocket.send(outputdata.encode())   # 返回响应报文字节流
        connectionSocket.close()   # 关闭TCP连接
    except IOError:   # 抛出异常
        print("[ERROR]The file being fetched is not existed.")
        with open("error.html","r") as f:   # 异常则打开异常响应文件（404）
            content = f.read()
        ## 生成响应报文（状态行+首部行+文件内容）
        stateRow = "HTTP/1.1 404 Not Found\r\n"  # 状态行
        firstRow = "Connection close\r\nDate:" + time.strftime("%Y-%m-%d", time.localtime(
            time.time())) + "\r\n服务器:Apache/1.3.0 (Windows)\r\nLast-Modified:Wedn,13 April 2022\r\nContent-Length:" + str(
            len(content)) + "\r\nContent-Type:html\r\n\r\n"  # 首部行
        outputdata = stateRow + firstRow + content  # 响应报文=状态行+首部行+文件内容
        connectionSocket.send(outputdata.encode())  # 返回错误响应字节流
        connectionSocket.close()   # 关闭TCP连接
