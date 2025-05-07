# _*_ coding : utf-8 _*_
# @Time : 2025/2/23 13:16
# @Author : luotao
# @File : demo
# @Project 饮料点单系统


class Drunk:
    sweet = 7
    temperature = "常温"

    # 构造函数
    def __init__(self, name, modle):
        self.name = name
        self.modle = modle

    # 加糖
    def addSweet(self):
        self.sweet += 1

    # 加冰
    def addTemperature(self, type):
        self.temperature = type

    def show(self):
        print(
            f"您点了一杯{self.temperature}{self.modle}的{self.name},甜度为{self.sweet}"
        )

# try-except-else-finally
try:
    nameAndType = input("您需要什么饮料？请输入名称和杯型(中间用横杆隔开):\n")
    if not nameAndType:
        raise Exception("输入错误")
    cola = Drunk(nameAndType.split("-")[0], nameAndType.split("-")[1])
except Exception as e: # 相当于java的catch
    print(e)
else: # 如果没有发生异常，则执行此块中的代码
    while True:
        cola.show()
        str = input("请问您还有其他需求吗？Y/N\n")
        if str == "N":
            print("好的，饮品马上来")
            break
        else:
            strOther = input("请问需要A加糖还是B加冰？")
            if strOther == "A":
                cola.addSweet()
            else:
                type = input("请问需要什么冰量？A:去冰，B少冰，C多冰")
                try:
                    cola.addTemperature({"A": "去冰", "B": "少冰", "C": "多冰"}[type])
                except KeyError as e:
                    print("选项有误，请重新输入")
finally:
    print("欢迎下次再来")
