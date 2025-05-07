""" 
聊天室服务端 GUI (使用 wxPython)
需要先安装 wxPython: pip install wxPython 
"""
# coding:utf-8
import wx
from socket import socket
from socket import AF_INET # 用于internet之间的进程通信
from socket import SOCK_STREAM #  用于TCP协议编程
import threading
import time

class SessionThread(threading.Thread):
    """ 继承式创建线程，需要重写run方法。会话线程来处理每个客户端的会话 """
    def __init__(self,clientSocket,clientAddr,clientTitle,server): # server：服务器对象,clientSocket: 服务器用来与客户端通信的 socket。
        threading.Thread.__init__(self)
        self.clientSocket=clientSocket
        self.clientAddr=clientAddr
        self.clientTitle=clientTitle
        self.server=server
        self.isOn=True # 会创建一个会话线程对象就表示服务器已经启动

    def run(self) -> None: # -> None 表示对函数返回类型的“承诺”，如果实际返回值不是 None，运行时不会报错，但类型检查工具会警告你。
        print(f'服务器启动了一个会话线程')
        while self.isOn:
            data=self.clientSocket.recv(1024).decode('utf-8') # 接收客户端发送的数据
            if data=='bye': # 如果客户端发送bye，则关闭连接
                self.isOn=False
                # 显示客户端断开连接信息
                self.server.showInfoAndSendToClient(self.clientTitle,f'{self.clientTitle}已离线',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
            else:
                # 广播消息
                self.server.showInfoAndSendToClient(self.clientTitle,data,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

        self.clientSocket.close() # 关闭客户端socket对象

# 定义服务端主窗口类，继承自 wx.Frame
class ServerFrame(wx.Frame):
    def __init__(self, title):
        """
        初始化窗口
        :param title: 窗口标题栏显示的文字
        """
        # 调用父类 wx.Frame 的构造函数创建窗口
        wx.Frame.__init__(self, id=1002, parent=None, title=title, size=(400, 450), pos=wx.DefaultPosition)

        # 创建主面板
        panel = wx.Panel(self)
        
        # 创建主垂直 Sizer
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # --- 1. 顶部控制按钮区域 ---
        # 创建水平 Sizer 用于放置按钮
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.startServerButton = wx.Button(panel, label="启动服务")
        self.saveRecordButton = wx.Button(panel, label="保存聊天记录")
        self.stopServerButton = wx.Button(panel, label="停止服务")

        # 将按钮添加到水平 Sizer，让它们平分空间并带边距
        button_sizer.Add(self.startServerButton, 1, wx.EXPAND | wx.ALL, 5)
        button_sizer.Add(self.saveRecordButton, 1, wx.EXPAND | wx.ALL, 5)
        button_sizer.Add(self.stopServerButton, 1, wx.EXPAND | wx.ALL, 5)

        # 将按钮 Sizer 添加到主 Sizer (不垂直扩展)
        main_sizer.Add(button_sizer, 0, wx.EXPAND)

        # --- 2. 服务器状态/日志显示区域 ---
        # 创建只读的多行文本控件用于显示信息
        self.show_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_SUNKEN )
        # 将显示区添加到主 Sizer (占据主要垂直空间)
        main_sizer.Add(self.show_text, 1, wx.EXPAND | wx.ALL, 5)
        
        # --- 3. 事件绑定 ---
        self.Bind(wx.EVT_BUTTON, self.on_start_server, self.startServerButton)
        self.Bind(wx.EVT_BUTTON, self.on_save_record, self.saveRecordButton)
        self.Bind(wx.EVT_BUTTON, self.on_stop_server, self.stopServerButton)
        
        # --- 4. 应用布局 ---
        panel.SetSizer(main_sizer)

        # --- 添加属性 --- 
        self.isOn=False # 服务器的启动状态
        self.hostPort=('127.0.0.1',8888) # 服务器地址和端口
        # 1.创建服务端socket对象
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        # 2.绑定IP和端口
        ip,port='127.0.0.1',8888
        self.serverSocket.bind((ip,port))

        # 3.监听
        self.serverSocket.listen(5) # 参数为最大连接数
        print('监听端口：',port)
        # 创建一个字典，用于存储每个客户端的会话线程对象{客户端名称clientTitle：会话线程对象sessionThread}
        self.sessionThreadDict={} 


    def showInfoAndSendToClient(self,clientTitle,data,dataTime):
        """ 提示信息,广播信息给客户端 """
        dataformat=f'\n[{dataTime}] {clientTitle}：{data}\n'.encode('utf-8')
        self.show_text.AppendText(dataformat) # 只读文本框显示信息
        # 遍历字典，广播信息给每个客户端
        for clientTitle,sessionThread in self.sessionThreadDict.items():
            if sessionThread.isOn:
                sessionThread.clientSocket.send(dataformat) # 通过会话线程对象的clientSocket对象发送数据

    # --- 事件处理方法定义 --- 

    def on_start_server(self, event):
        """处理"启动服务"按钮点击事件"""
        print("启动服务按钮被点击")
        if not self.isOn: # 服务器没启动时启动
            self.log_message("[系统] 准备启动服务器...")
            self.isOn=True
            # 创建主线程对象来启动会话线程。函数式创建线程：threading.Thread(target函数名)
            mainThead=threading.Thread(target=self.startServer)
            # 设置为守护线程: self.startServer() 是一个无限循环，用于监听客户端连接。
            # 关闭窗口后即Python 主线程结束，守护线程mainThread将被强制结束，不会等待startServer的无线循环自然结束。
            mainThead.daemon=True 
            mainThead.start()

    def startServer(self):
        """启动服务器"""
        self.log_message("[系统] 服务器启动成功")
        self.log_message("[系统] 等待客户端连接...")
        # 无限循环，用于监听客户端连接。
        while self.isOn:
            # 4.等待客户端连接
            clientSocket,clientAddr = self.serverSocket.accept() # 将元祖拆包赋值 ，clientSocket: 服务器用来与客户端通信的 socket。
            print('client连接成功，client地址：',clientAddr)
            # 5.接收客户端发送的数据,客户端连接服务器后客户端需要马上发送客户端名称
            clientTitle = clientSocket.recv(1024).decode('utf-8') # 接收1024字节的数据，解码
            # 创建一个会话线程对象来启动服务。继承式创建线程
            print(self) # ServerFrame object
            sessionThread = SessionThread(clientSocket,clientAddr,clientTitle,self) # self是服务器对象
            self.sessionThreadDict[clientTitle]=sessionThread # 添加会话对象到字典中保存
            sessionThread.start()
            self.showInfoAndSendToClient(clientTitle,f'欢迎{clientTitle}进入聊天室',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

        # 当self.isOn=False时，结束会话线程
        self.clientSocket.close()


    def on_save_record(self, event):
        """处理"保存聊天记录"按钮点击事件"""
        print("保存聊天记录按钮被点击")
        recordData = self.show_text.GetValue()
        if recordData:
             self.log_message("[系统] 准备保存聊天记录...")
             # 可以使用 wx.FileDialog 来让用户选择保存位置和文件名
             try:
                 with open("聊天记录.txt", "w",encoding="utf-8") as f:
                     f.write(recordData)
                 self.log_message("[系统] 聊天记录保存成功！")
             except Exception as e:
                 self.log_message("[系统] 聊天记录保存失败！")



    def on_stop_server(self, event):
        """处理"停止服务"按钮点击事件"""
        print("停止服务按钮被点击")
        self.log_message("[系统] 准备停止服务器...")
        try:
            self.isOn=False
            self.log_message("[系统] 服务器已停止！")
        except Exception as e:
            self.log_message("[系统] 服务器停止失败！")
        
    def log_message(self, message):
        """在显示区域安全地追加日志信息"""
        # 从非 GUI 线程更新 GUI 控件时，应使用 CallAfter
        # 但如果是在事件处理器（本身就在 GUI 线程）中调用，可以直接更新
        # 为了统一和安全，这里可以使用 CallAfter (尽管在此处非必需)
        wx.CallAfter(self.show_text.AppendText, message + "\n")
        # 或者直接调用:
        # self.show_text.AppendText(message + "\n")

# Python 标准入口点
if __name__ == "__main__":
    # 创建 wxPython 应用对象
    app = wx.App()
    # 创建服务器窗口实例
    server = ServerFrame('我的聊天服务器')
    # 显示窗口
    server.Show()
    # 启动事件循环
    app.MainLoop()
