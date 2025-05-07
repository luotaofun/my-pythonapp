""" 变量的赋值：只是形成两个变量，实际上还是指向同一个对象。 """
class CPU():
    pass

class Disk():
    pass

class Computer():
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
com=Computer(CPU(),Disk())
com1=com 
print(com,'子对象的地址是：',com.cpu,com.disk)      # 4150 40D0 4110
print(com1,'子对象的地址是：',com1.cpu,com1.disk)   # 4150 40D0 4110



""" 浅拷贝：产生一个新对象，子对象不会产生新的 """
print('-'*50)
import copy
com2=copy.copy(com) # com2是新产生的对象，com2的子对象cpu和disk不变
print(com,'子对象的地址是：',com.cpu,com.disk)      # 4150 40D0 4110
print(com2,'子对象的地址是：',com1.cpu,com1.disk)   # 4E30 40D0 4110

""" 深拷贝：产生一个新对象，子对象也会产生新的 """
print('-'*50)
import copy
com3=copy.deepcopy(com) # com3是新产生的对象，com3的子对象cpu和disk也会重新递归创建
print(com,'子对象的地址是：',com.cpu,com.disk)      # 4150 40D0 4110
print(com3,'子对象的地址是：',com3.cpu,com3.disk)   # 5100 5E80 67E0




 
