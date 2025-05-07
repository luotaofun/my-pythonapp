""" UdpServerDemo """
from socket import socket
from socket import AF_INET # 用于internet之间的进程通信
from socket import SOCK_DGRAM #  用于UDP协议编程

# 1.创建socket对象
serverSocket = socket(AF_INET, SOCK_DGRAM)

# 2.绑定IP和端口
ip,port='127.0.0.1',8888
serverSocket.bind((ip,port))


# 3.接收客户端发送的数据
data,addr = serverSocket.recvfrom(1024)# 接收1024字节的数据
data = data.decode('utf-8')
while data!='bye':
    if data:
        print('client:',data)
    if data=='bye': # 如果客户端发送bye，则关闭连接
        break 
    serverData = input('请输入要发送给client的数据：').encode('utf-8')
    serverSocket.sendto(serverData,addr)# 回复给客户端
    if serverData=='bye': # 如果服务端也发送bye，则关闭连接
        break
    data,addr = serverSocket.recvfrom(1024) # 接收客户端发送的数据更新循环条件
    data=data.decode('utf-8')

# 4.关闭socket对象
serverSocket.close()