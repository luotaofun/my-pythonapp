""" UdpClientDemo """
from socket import socket
from socket import AF_INET # 用于internet之间的进程通信
from socket import SOCK_DGRAM #  用于UDP协议编程

# 1.创建socket对象
clientSocket = socket(AF_INET,SOCK_DGRAM)

ip,port='127.0.0.1',8888

# 2.发送数据
data=''
while data!='bye':
    sendData=input('请输入要发送给server的数据：')
    clientSocket.sendto(sendData.encode('utf-8'),(ip,port))
    if sendData=='bye': # 退出客户端
        break
    data,addr = clientSocket.recvfrom(1024) # 接收服务端发送的数据来更新循环条件
    print('server:',data.decode('utf-8'))
    print(addr) # ('127.0.0.1', 8888)


# 4.关闭socket对象
clientSocket.close()