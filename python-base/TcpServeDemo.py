""" TcpServerDemo """
from socket import socket
from socket import AF_INET # 用于internet之间的进程通信
from socket import SOCK_STREAM #  用于TCP协议编程

# 1.创建socket对象
serverSocket = socket(AF_INET, SOCK_STREAM)

# 2.绑定IP和端口
ip,port='127.0.0.1',8888
serverSocket.bind((ip,port))

# 3.监听
serverSocket.listen(5) # 参数为最大连接数
print('server启动成功，监听端口：',port)

# 4.等待客户端连接
clientSocket,clientAddr = serverSocket.accept() # 将元祖拆包赋值，clientSocket: 服务器用来与客户端通信的 socket。
print('client连接成功，client地址：',clientAddr)

# 5.接收客户端发送的数据
data = clientSocket.recv(1024).decode('utf-8') # 接收1024字节的数据，解码
while data!='bye':
    if data:
        print('client:',data)
    if data=='bye': # 如果客户端发送bye，则关闭连接
        break 
    serverData = input('请输入要发送给client的数据：')
    clientSocket.send(serverData.encode('utf-8'))# 回复给客户端
    if serverData=='bye': # 如果服务端也发送bye，则关闭连接
        break
    data = clientSocket.recv(1024).decode('utf-8') # 接收客户端发送的数据更新循环条件

# 6.关闭socket对象
serverSocket.close()
clientSocket.close()