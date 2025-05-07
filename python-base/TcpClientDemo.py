""" TcpClientDemo """
from socket import socket
from socket import AF_INET # 用于internet之间的进程通信
from socket import SOCK_STREAM #  用于TCP协议编程

# 1.创建socket对象
clientSocket = socket()

# 2.连接服务器IP和端口
ip,port='127.0.0.1',8888
clientSocket.connect((ip,port))
print('--------与server连接成功--------')

# 3.发送数据
data=''
while data!='bye':
    sendData=input('请输入要发送给server的数据：')
    clientSocket.send(sendData.encode('utf-8'))
    if sendData=='bye': # 退出客户端
        break
    data = clientSocket.recv(1024).decode('utf-8') # 接收服务端发送的数据来更新循环条件
    print('server:',data)


# 4.关闭socket对象
clientSocket.close()