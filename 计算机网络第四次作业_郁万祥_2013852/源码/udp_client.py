# -*- coding: UTF-8 -*-
from socket import*
import time
#客户端调用socket()创建套接字
clientSocket=socket(AF_INET,SOCK_DGRAM)
#使用settimeout函数限制recvfrom()函数的等待时间为1秒
clientSocket.settimeout(1)
count=0#计数接收pong报文失败次数
start=0#第一次成功接收pong报文后用于计算RRT
totaltime=0#用于计算平均RRT
#发送10次ping报文
for i in range(10):
    #报文内容
    print("test_"+str(i))
    t1=time.time()#RRT开始计数时间
    #将信息转换为byte后发送到指定服务器端
    clientSocket.sendto("ping".encode("utf-8"),("172.25.240.1",10000))
    try:
        #调用recvfrom()函数接收服务器发来的应答数据
        message,address=clientSocket.recvfrom(1024)
        #超时处理，等到时间超过1秒，捕获抛出的异常后打印丢失报文，进行下一步操作
    except:
        print("out of time!!!")
        count=count+1
        continue
    t2=time.time()#RRT结束计数时间
    #计算ping消息的最小、最大和平均RRT，并计算丢包率
    if(start==0):
        mintime=(t2-t1)/2
        maxtime=(t2-t1)/2
        start=1
    elif((t2-t1)/2<mintime):
        mintime=(t2-t1)/2
    elif((t2-t1)/2>maxtime):
        maxtime=(t2-t1)/2
    totaltime=totaltime+(t2-t1)/2
    print('%.15f'%((t2-t1)/2))
print('min_RRT:'+str(mintime))
print('max_RRT:'+str(maxtime))
print('average_RRT:'+str(totaltime/(10-count)))
print('packet loss rate:'+str(count/10))