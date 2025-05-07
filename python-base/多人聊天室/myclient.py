""" 
聊天室客户端 GUI (使用 wxPython)
需要先安装 wxPython: pip install wxPython 
"""
# coding:utf-8
import wx
from socket import socket
from socket import AF_INET # 用于internet之间的进程通信
from socket import SOCK_STREAM #  用于TCP协议编程
import threading
import time
# 定义客户端主窗口类，继承自 wx.Frame
class ClientFrame(wx.Frame):
    def __init__(self, title):
        """
        初始化窗口
        :param title: 窗口标题栏显示的文字
        """
        # 调用父类 wx.Frame 的构造函数来创建窗口
        # id: 窗口的唯一标识符，-1 表示由系统自动分配
        # parent: 父窗口，None 表示这是一个顶级窗口
        # title: 窗口标题
        # size: 窗口初始大小 (宽度, 高度)
        # pos: 窗口初始位置，wx.DefaultPosition 表示由系统决定
        wx.Frame.__init__(self, id=1001, parent=None, title=title, size=(400, 450), pos=wx.DefaultPosition)
        
        # 创建一个面板 (Panel) 作为窗口内容的容器
        # 所有其他的控件都应该放在这个面板上
        panel = wx.Panel(self)
        
        # 创建一个垂直方向的 BoxSizer，用于管理主界面元素的垂直排列
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # --- 1. 顶部连接/断开按钮区域 ---
        # 创建一个水平方向的 BoxSizer 用于排列顶部按钮
        top_button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.connButton = wx.Button(panel, label="连接") # 创建"连接"按钮
        self.disConnButton = wx.Button(panel, label="断开") # 创建"断开"按钮
        # 将按钮添加到水平 Sizer 中
        # 参数1: 要添加的控件
        # 参数2 (proportion): 控件在 Sizer 方向上所占空间的比例。1 表示与其他比例为 1 的控件均分空间。
        # 参数3 (flag): 控制控件的对齐、边框和扩展行为。
        #   wx.EXPAND: 让控件填充其在 Sizer 方向上分配到的空间。
        #   wx.ALL: 在控件四周都添加边框。
        # 参数4 (border): 边框的像素大小。
        top_button_sizer.Add(self.connButton, 1, wx.EXPAND | wx.ALL, 5) 
        top_button_sizer.Add(self.disConnButton, 1, wx.EXPAND | wx.ALL, 5)
        # 将顶部按钮的 Sizer 添加到主垂直 Sizer 中
        # proportion=0 表示这个 Sizer 在垂直方向上不扩展，只占据它所需的高度。
        main_sizer.Add(top_button_sizer, 0, wx.EXPAND) 

        # --- 2. 聊天显示区域 ---
        # 创建一个多行文本控件 (TextCtrl) 用于显示聊天记录
        # style 参数设置控件样式:
        #   wx.TE_MULTILINE: 允许多行文本。
        #   wx.TE_READONLY: 设置为只读，用户不能直接编辑。
        #   wx.BORDER_SUNKEN: 添加一个凹陷效果的边框。
        self.show_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_SUNKEN)
        # 将显示区添加到主 Sizer
        # proportion=1 表示它将占据主 Sizer 垂直方向上大部分可用的额外空间。
        main_sizer.Add(self.show_text, 1, wx.EXPAND | wx.ALL, 5) 

        # --- 3. 聊天输入区域 ---
        # 创建一个多行文本控件用于用户输入聊天内容
        # (没有 wx.TE_READONLY，所以用户可以输入)
        self.chat_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.BORDER_SUNKEN)
        # 将输入区添加到主 Sizer
        # proportion=0 表示它只占据固定的、能容纳其内容的高度。
        # 我们希望输入框高度固定，而不是随窗口拉伸变化。
        # **注意**: 如果希望输入框高度也随窗口拉伸，可以将 proportion 改为非 0 值，比如 0.5 或 1。
        #            但通常聊天输入框高度是固定的。
        main_sizer.Add(self.chat_text, 0, wx.EXPAND | wx.ALL, 5) 

        # --- 4. 底部重置/发送按钮区域 ---
        # 创建一个水平方向的 BoxSizer 用于排列底部按钮
        bottom_button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.resetButton = wx.Button(panel, label="重置") # 创建"重置"按钮
        self.sendButton = wx.Button(panel, label="发送")   # 创建"发送"按钮
        # 将按钮添加到水平 Sizer，布局参数同顶部按钮
        bottom_button_sizer.Add(self.resetButton, 1, wx.EXPAND | wx.ALL, 5)
        bottom_button_sizer.Add(self.sendButton, 1, wx.EXPAND | wx.ALL, 5)
        # 将底部按钮的 Sizer 添加到主垂直 Sizer 中 (proportion=0)
        main_sizer.Add(bottom_button_sizer, 0, wx.EXPAND)


        # --- 5. 事件绑定 ---
        # 将按钮的点击事件 (wx.EVT_BUTTON) 与相应的处理方法关联起来
        # 当按钮被点击时，对应的 on_xxx 方法就会被调用
        self.Bind(wx.EVT_BUTTON, self.on_connect, self.connButton)
        self.Bind(wx.EVT_BUTTON, self.on_disconnect, self.disConnButton)
        self.Bind(wx.EVT_BUTTON, self.on_reset, self.resetButton)
        self.Bind(wx.EVT_BUTTON, self.on_send, self.sendButton)

        # --- 6. 应用布局 --- 
        # 将主 Sizer 应用到面板上，这样 Sizer 就会负责管理面板内控件的布局
        panel.SetSizer(main_sizer)

        # --- 添加属性 --- 
        self.clientName=title
        self.isConected=False # 客户端连接服务器的状态
        self.clientSocket=None # 客户端socket对象

    # --- 事件处理方法定义 --- 
    # 这些方法会在对应的按钮被点击时执行

    def on_connect(self, event):
        """处理"连接"按钮点击事件"""
        print("连接按钮被点击")
        if not self.isConected:
            # 1.创建客户端socket对象
            self.clientSocket = socket()

            # 2.连接服务器IP和端口
            ip,port='127.0.0.1',8888
            self.clientSocket.connect((ip,port))
            # 客户端连接服务器后客户端需要马上发送客户端名称给服务器，服务器会将客户端名称和客户端socket对象用字典保存起来。
            self.clientSocket.send(self.clientName.encode('utf-8'))
            # 创建一个会话线程对象来对话服务器。函数式创建线程：threading.Thread(target函数名)
            sessionThread=threading.Thread(target=self.sessionThread)
            # 将客户端会话线程设置为守护线程：关闭窗口后即Python 主线程结束，守护线程sessionThread将被强制结束。
            sessionThread.daemon=True
            self.isConected=True # 创建一个会话线程对象就表示客户端成功连接服务器
            sessionThread.start()
    def sessionThread(self):
        while self.isConected:
            # 接受来自服务器的数据
            data=self.clientSocket.recv(1024).decode('utf-8')
            # 将数据显示在客户端只读文本框中
            self.show_text.AppendText(f'\n{data}\n')
            

    def on_disconnect(self, event):
        """处理"断开"按钮点击事件"""
        print("断开按钮被点击")
        self.clientSocket.send('bye'.encode('utf-8')) # 发送断开的信号
        self.isConected=False

    def on_reset(self, event):
        """处理"重置"按钮点击事件"""
        print("重置按钮被点击")
        # 清空聊天输入框的内容
        self.chat_text.SetValue("") 

    def on_send(self, event):
        """处理"发送"按钮点击事件"""
        # 获取输入框中的文本
        data = self.chat_text.GetValue()
        print(f"发送按钮被点击, 消息: {data}")
        # 如果消息不为空
        if data and self.isConected:
            self.clientSocket.send(data.encode('utf-8')) # 向服务器发送消息

            # 发送后清空输入框
            self.chat_text.SetValue("") 

# Python 的标准入口点检查
# 当这个脚本被直接运行时，下面的代码才会执行
# 如果这个脚本被其他模块导入，则不会执行
if __name__ == "__main__":
    # 创建一个 wxPython 应用程序对象
    app = wx.App()
    # 创建我们自定义的 ClientFrame 窗口实例
    client = ClientFrame('Tao')
    # 显示窗口
    client.Show()
    # 进入 wxPython 的主事件循环
    # 这个循环会监听用户的操作（如点击按钮、输入文字等）并分发事件
    # 程序会一直停留在这里直到窗口被关闭
    app.MainLoop()
