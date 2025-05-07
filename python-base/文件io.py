def fileIo():
    with open(file='a.txt', mode='w+', encoding='utf-8') as f:
        # | r              | 以只读模式打开，文件指针在文件的开头，如果文件不存在，程序抛异常 |
        # | rb             | 以只读模式打开二进制文件，如图片文件 |
        # | w              | 覆盖写模式，文件不存在创建，文件存在则内容覆盖 |
        # | wb             | 覆盖写模式写入二进制数据，文件不存在则创建，文件存在则覆盖 |
        # | a              | 追加写模式，文件不存在创建，文件存在，则在文件最后追加内容 |
        # | +              | 与w/r/a等一同使用，在原功能的基础上增加同时读写功能 |
        # f.write(''.join(['hello\n','world\n']) )   
        f.writelines(['hello\n','world\n'])  #将内容为字符串的列表写入文件  

        f.seek(0) # 将文件指针移动到文件开头,因为写完后文件指针在文件末尾
        strList = f.readlines()#读取所有内容返回一个列表,内容的一行为列表的一个元素
        # str = f.read() 
        print(strList)

def copyFile(src='a.txt', dst='b.txt'):
    with open(file=src, mode='r', encoding='utf-8') as f:
        with open(file=dst, mode='w', encoding='utf-8') as f1:
            f1.write(f.read())

def osDemo():
    import os
    import time
    # os.chdir('D:/pythonTest') # 设置工作目录
    print('当前工作目录的绝对路径:', os.getcwd())  # D:/pythonTest
    print('指定路径下所有目录及文件，返回一个列表：:', os.listdir('D:/'))  
    print('获取目录或文件的绝对路径：',os.path.abspath(r'./python-base/文件io.py'))
    output_path = ".output"
    if not os.path.exists(output_path): # 用于检查 path 是否存在，不区分是文件还是目录。
        os.makedirs(output_path) # 创建多级目录
    filepath = os.path.join(output_path,  f"学生信息-{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())}.xlsx")  # 拼接完整的文件保存路径

    if  os.path.exists('./你好'):
        os.rmdir('./你好') # 删除目录

    fileName,extensionName=os.path.splitext(r'D:\workspace\python-projects\my-pythonapp\python-base\文件io.py') # 分离文件名和扩展名,元祖类型
    print('文件名:',fileName,'扩展名:',extensionName)

    print('提取文件名：',os.path.basename(r'D:\workspace\python-projects\my-pythonapp\python-base\文件io.py'))
    print('提取路径：',os.path.dirname(r'D:\workspace\python-projects\my-pythonapp\python-base\文件io.py'))

    print('是否是有效路径：',os.path.isdir(r'D:\workspace\python-projects\my-pythonapp\python-base'))
    print('是否是有效文件：',os.path.isfile(r'D:\workspace\python-projects\my-pythonapp\python-base\文件io.py'))

    # os.rename(src='src.txt', dst='dst.txt') # 重命名文件

    # os.remove(path='./dst.txt') # 删除文件

    # 获取文件信息
    info=os.stat(path=r'D:\workspace\python-projects\my-pythonapp\python-base\文件io.py') # 获取文件的最近一次访问时间（时间戳）
    print(type(info),dir(info))
    print('最近一次访问时间:', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(info.st_atime))) 
    print('在win系统中显示的文件的创建时间:', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(info.st_birthtime)))
    print('最后一次修改时间:', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(info.st_mtime)))
    print('文件的字节大小:',info.st_size)

    # 启动python解释器
    # os.startfile('python.exe')

def create_filename(path=r'C:\Users\T\Desktop\.output'):
    import os
    import random
    filenameList=[]
    lst=['水果', '蔬菜', '肉类', '蛋类', '酒水', '茶酒', '饮料', '其他']
    code = [hex(i)[2].upper() for i in range(16)]  # 从 0 到 15 的整数序列转换为十六进制数字部分的第一个字符。
    # code = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in range(1,101): # 10个文件名
        filename=''
        # 合成3位数的序号
        if i<0:
            filename+='00'+str(i)
        elif i<10:
            filename+='0'+str(i)
        else:
            filename+=str(i)
        filename+='-' + random.choice(lst)
        # 合成10位数的code码
        codeStr=''
        for i in range(1,11):
            codeStr+=random.choice(code)
        filename+='-'+codeStr
        filenameList.append(filename)

    # 创建文件
    # path=r'C:\Users\T\Desktop\.output'
    if not os.path.exists(path): 
        os.mkdir(path)
    for filename in filenameList:
        file=os.path.join(path, filename+'.txt')
        with open(file=file, mode='w', encoding='utf-8') as f:
            pass

    return filenameList


def showInfo():
    print('0：退出 1.查看登录日志')

def writeLog(username):
    import time
    with open('log.txt','a',encoding='utf-8') as f:
        data= f'用户名:{username},登录时间:{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())}\n'
        f.write(data)

def readLog():
    with open('log.txt','r',encoding='utf-8') as f:
        while True:
            data=f.readline()
            if not data:
                break
            print(data)

def find_answer(question):
    """ java:Write onece,run anywhere """
    with open(r'D:\workspace\python-projects\my-pythonapp\python-base\replay.txt', 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            keyword, answer = line.split(':')
            if keyword in question:
                print(answer)
                return answer
        return False  
               

if __name__ == '__main__':
    # fileIo()
    # copyFile()
    # osDemo()

    # create_filename()
    find_answer("java")

    username=input('请输入用户名：')
    pwd=input('请输入密码：')
    if username=='admin' and pwd=='admin':
        print('登录成功')
        writeLog(username)
        showInfo()
        num = eval(input('请输入操作序号：'))
        while True:
            if num==0:  #退出
                break
            elif num==1: # 查看登录日志
                readLog()
                showInfo()
            else:
                print('输入操作序号有误')
                showInfo()
            num = eval(input('请输入操作序号：')) #
    else:
        print('登录失败')
