class Person: # 父类默认继承了object
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print(f'我叫{self.name},今年{self.age}岁')

    def __str__(self):
        """ 重写__str__方法，打印对象时，会自动调用该方法。相当于java的toString方法 """
        return f'姓名:{self.name},年龄:{self.age}'

class Teacher(Person): # 继承Person。
    def __init__(self,name,age,title):
        super().__init__(name,age) # 调用父类的构造函数，相当于： Person.__init__(self,name)
        self.title=title

    def show(self):
        """ 重写父类的show方法 """
        print(f'我叫{self.name},今年{self.age}岁,我是老师,我的职位是{self.title}')


class Student(Person): # 继承Person。 访问父类Person的show方法：Student("neko1",10,100).show()
    name="neko"

    def __init__(self,xm,age,score):
        """ 相当于java的构造函数 """
        self.name=xm
        self.age=age
        self.__score=score
 
    @property
    def score(self):
        """ 相当于java的getter方法。用@property将score方法“伪装”成属性调用： print(student.score)  # 访问getter,无需加括号"""
        return self.__score

    # getter 和 setter 名称必须相同
    @score.setter
    def score(self, value):
        """ 相当于java的setter方法。student.score = 95  # 调用 setter 方法"""
        if value < 0 or value > 100:
            raise ValueError("成绩必须在0到100之间！")
        self.__score = value

    def run(self):
        """ 相当于java的成员方法 """
        print(f'{self.name}正在跑步')

    @classmethod
    def classMethod(cls):
        """ 类方法:自带一个cls参数,即class的缩写,可以通过类名或实例来调用。相当于java的static方法 """
        print(cls.name) # 访问类属性,静态方法不可以这样访问，静态方法要显示指定类名访问：Student.name
        print(Student().name) # 通过实例访问类属性
        cls.otherClassMethod()  # 调用其它类方法
        
    @classmethod
    def otherClassMethod(cls):
        print("Other class method")

    @staticmethod
    def staticMethod():
        """ 静态方法:,可以通过类名或实例来调用。相当于java的static方法"""
        print(Student.name) # 静态方法要显示指定类名访问：Student.name
        print(Student().name) # 通过实例访问类属性
        print(f'我是静态方法')

    def _funByProtected(self):
        """ 一个下划线开头定义protected权限，只能在本类和子类中访问 """
        print('我是protected的方法')

    def __funByPrivate(self):
        """ 两个个下划线开头定义私有化权限，访问方式： Student("neko1",10,100)._Student__funByPrivate()"""
        print('我是private的方法')

# 动态绑定属性:  给实例绑定一个属性，该属性只对当前实例有效，其他实例将不能访问该属性。
stu1 = Student("neko1",10,100)
stu1.gender="男" 
print(stu1.gender) # 访问绑定的属性

# 动态绑定方法:  给实例绑定一个方法，该方法只对当前实例有效，其他实例将不能调用该方法。
def stu1Say():
    print('hello')
stu1.fun = stu1Say
stu1.fun() # 调用绑定的方法






