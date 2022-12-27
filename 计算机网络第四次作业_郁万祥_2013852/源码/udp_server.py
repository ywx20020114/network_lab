# UDP服务器程序：udp_server.py
import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)#服务端调用socket()创建套接字来启动服务器
serverSocket.bind(('', 10000))#服务端调用bind()指定服务器的套接字地址
#print("服务开启，监听端口:10000")
while True:
    rand = random.randint(0, 10)#返回参数1和参数2之间的任意整数， 闭区间
    message, address = serverSocket.recvfrom(1024)#服务端调用recvfrom()等待接收数据，此时阻塞
    message = message.upper()#upper()方法将字符串中的所有小写字符转换为大写字符并返回
    print("接收的消息{}\n".format(message))
    
    print("接收的地址{}\n".format(address))
    #成功接受消息后继续运行
    if rand < 4:#模拟丢失30%的客户端数据包
        print("数据包丢失")
        continue#跳过本次循环体中余下尚未执行的语句，立即进行下一次的循环条件判定，可以理解为仅结束本次循环
    serverSocket.sendto(message, address)##服务器接收到客户端发来的数据后，调用sendto()向客户发送应答数据


