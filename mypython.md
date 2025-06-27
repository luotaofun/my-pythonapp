---
title: python
date: 2024-03-24 14:12:43
tags: python
---

```bash
# 使用 venv 模块来创建虚拟环境并放到.venv 目录下 -m 是 module 的缩写告诉 Python 解释器将后面的模块名当作一个脚本来执行。
python -m venv .venv

# 激活虚拟环境，使当前 shell 会话使用该虚拟环境中的 Python 解释器和包。
.venv/Scripts/activate
# 退出虚拟环境
deactivate 

# 读取 requirements.txt 文件中的内容，并根据其中列出的包名和版本号自动安装所有依赖。
pip install -r requirements.txt

# 删除虚拟环境
rm -r .venv/
```

```bash
# 生成一个包含当前环境所有依赖的 requirements.txt 文件。
pip freeze > requirements.txt
# 卸载requirements的依赖
pip uninstall -r requirements.txt 

```

## 代码模板

```json
{
	// Place your snippets for python here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	// "Print to console": {
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
	

	"Python Method Comment": {
		"prefix": "pydoc",
		"body": [
		  "\"\"\"",
		  " @Description $1",
		  " @Author LuoTao",
		  " @Date ${CURRENT_YEAR}-${CURRENT_MONTH}-${CURRENT_DATE}",
		  "\"\"\"",
		],
		"description": "Python方法注释模板"
	  },
	  "Python File Header": {
		"prefix": "pyheader",
		"body": [
		"\"\"\"",	
		" _*_ coding : utf-8 _*_",
		" @Time : ${CURRENT_YEAR}-${CURRENT_MONTH}-${CURRENT_DATE} ${CURRENT_HOUR}:${CURRENT_MINUTE}",
		" @Author : luotao",
		" @File : ${TM_FILENAME}",
		" @Description : $1",
		"\"\"\"",
		],
		"description": "Python文件头部模板"
	},
	 
}


```


## pycharm配置

code templates![code templates](./my-python/image-20240324134851480.png)

```python
# _*_ coding : utf-8 _*_
# @Time : ${DATE} ${TIME}
# @Author : luotao
# @File : ${NAME}
# @Project ${PROJECT_NAME}
```

## pip

> 包管理工具

```bash
pip -V //版本
pip uninstall ipython //卸载
pip list //包列表
pip install ipython -i https://pypi.douban.com/simple/ //指定下载源
```


## 设置环境

```bash
# 使用 venv 模块来创建虚拟环境并放到.venv 目录下
python -m venv .venv

# 激活虚拟环境，使当前 shell 会话使用该虚拟环境中的 Python 解释器和包。
.venv/Scripts/activate
# 退出虚拟环境
deactivate 

# 读取 requirements.txt 文件中的内容，并根据其中列出的包名和版本号自动安装所有依赖。
pip install -r requirements.txt

# 删除虚拟环境
rm -r .venv/
```

```bash
# 生成一个包含当前环境所有依赖的 requirements.txt 文件。
pip freeze > requirements.txt
# 卸载requirements的依赖
pip uninstall -r requirements.txt 

```

### 添加新依赖

1. 在您的虚拟环境中安装包：
   ```bash
   pip install package_name
   ```

2. 将其添加到 requirements.txt：
   ```bash
   pip freeze > requirements.txt
   ```
   
   或者手动将其添加到 requirements.txt 并指定版本：
   ```bash
   package_name==1.0.0
   ```

### 更新依赖

1. 在虚拟环境中更新包：
   ```bash
   pip install --upgrade package_name
   ```

2. 更新 requirements.txt：
   ```bash
   pip freeze > requirements.txt
   ```

### 最佳实践

1. 始终使用虚拟环境进行隔离
2. 保持 requirements.txt 更新
3. 为所有依赖指定版本号
4. 在 requirements.txt 中按类别分组依赖
5. 使用 pip-tools 或 Poetry 进行更高级的依赖管理

### 退出环境

```bash
deactivate
```

## int的缓存

> - 小整数在程序中使用频率极高，Python 缓存了范围在 **[-5, 256]** 之间的整数。
> - 这些整数在解释器启动时就会被预先创建，并在整个程序运行期间被复用，避免频繁地创建和销毁对象。

```python
x = 256
y = 256
print(id(x),id(y))
print(x is y)  # True
print(x == y)  # True
a = 257
b = 257
print(id(a),id(b))
print(a is b)  # False a和b不是同一个对象
print(a == b)  # True 对象的值是相同的

```

## 运算符

```python
'y'<'x'==False  # False
# 等价于：'y'<'x' and 'x'==False 
```



## 字符串

```python
str = str2= "123456789" 
# 等价于：str,str2="123456789","123456789"

print(str[::2]) # 13579
print(str[::-1]) # 123456789
print(str[-1:-10:-1]) # 123456789

```



## 流程控制

```python

"""
1.python中系统自动辨别数据类型,并不需要显示的去声明
2.标识符由字母/数字/下划线构成且大小写敏感
3.python中都是字符串才可加法拼接
"""
name_list = ["罗涛", "周超"]  # 列表
age_tuple = (18, 19)  # 元祖
person = {"name": "罗涛", "age": 18}  # 字典

# 强制类型转换.0或数据为空则为False
a = True
print(type(a))  # 判断数据类型
a1 = str(a)  # 布尔转字符串
print(type(a1))
print(a1)

b = " "  # 空格转布尔TRUE
# b = "" # 空字符串转布尔FALSE
print(type(b))
b1 = bool(b)
print(type(b1))
print(b1)

# 多变量赋值
a, b, c = 1, 2, 3

# 短路与\短路或
True and print(1)  # 1
False and print(2)  # 不执行

True or print(3)  # 3
False or print(4)  # 4

# 流程控制
score = int(input("请输入成绩:"))
if score >= 90:
    print("优秀")
elif score >= 60:
    print("合格")
else:
    print("不合格")


```



## 列表

```python

def listCRUD():
    #  -----------Create（创建）-----------
    nameList=list() # nameList=[]
    nameList.append("neko") # 追加元素
    nameList.append("旺财")
    print(f'{nameList.insert(1, ["番茄", "鸡蛋"])}插入一个列表==>{nameList}')  # ['neko', ['番茄', '鸡蛋'], '旺财']
    newList = nameList.copy() # 复制列表，生成新的列表

    goodsList1 = ["白象", "康师傅"]
    goodsList2 = ["烤鸭", "烤鱼"]
    print(goodsList1 + goodsList2)  # 生成了新列表['白象', '康师傅', '烤鸭', '烤鱼']
    goodsList1.extend(goodsList2)  # 将一个list中的元素逐一添加到目标列表（修改原来的列表）
    print(goodsList1)

    # 列表生成式
    lst = [item for item in range(1,11) if item%2==0] # 10以内的偶数序列
    import random
    lst2 =[random.randint(1,100) for item in range(10) ] # [1,100)的10个随机数序列
    # 4行5列的二维列表
    lst3 = [[j for j in range(5)] for i in range(4)]
    for row in lst3:
        for element in row:
            print(element, end=' ')
        print()
        
    # -----------Delete（删除）-----------
    # print(nameList.pop())  # 删除最后一个元素
    # print(nameList.pop(0))  # 删除第一个元素
    # print(nameList.clear())  # 清空元素
    # if 1 in nameList:
    #     print(nameList.remove("1")) # 删除匹配到的第一个指定元素


    # -----------Read（读取）-----------
    print(f'从索引位置 0 开始查找列表中第一个"旺财" 的索引===>{nameList.index("旺财", 0)}')  # 1 
    # for遍历
    for name in nameList: 
        print(name)
    print('-' * 50)
    # lambda匿名函数式遍历列表
    for i in range(len(nameList)):
        fun = lambda name:print(nameList[i]) 
        print(type(fun)) # <class 'function'>
        fun(i) # 调用匿名函数
    
    # for i遍历
    for i in range(len(nameList)): 
        print(nameList[i])
    # enumerate遍历,index是序号
    for index, item in enumerate(nameList):
        print(f"序号 {index} 的元素是：{item}") 
    # 指定序号从1开始    
    for index, item in enumerate(nameList,start=1):
        print(f"序号 {index} 的元素是：{item}") 

   # --------Update（更新）-----------
    # 列表切片：左闭右开区间取值
    ageList = [18, 19, 20]
    print(ageList[0:3])  # [18, 19, 20]
    print(ageList[1:])  # [19, 20]
    print(ageList[:3])  # [18,19, 20]
    name = "ABCDEF"
    print(name[1:])  # BCDEF
    # 字符串转列表
    print(list(name))  # ['A', 'B', 'C', 'D', 'E', 'F']

    # 列表排序
    orderList = ['a','c','b','d','e']
    # 排序规则为忽略大小写
    orderList.sort(key=str.lower)  # 列表.sort(key=None,reverse=False) # param1 排序规则默认None; param2 排序方式默认升序
    print(orderList)  # ['a', 'b', 'c', 'd', 'e']

    orderList = [2, 1, 3, 4, 5]
    # 内置函数sorted(iterable排序对象,key=None,reverse=False)
    newSortedList = sorted(orderList, reverse=True) # (只临时修改排序，不影响原列表)sorted临时排序(降序) [5, 4, 3, 2, 1] 

    orderList = [1, 2, 3, 4, 5]
    orderList.reverse()  # 反转
    print(orderList)  # [5, 4, 3, 2, 1]

if __name__ == '__main__':
    listCRUD()

```

## 元祖

```python
    # 元组中的所有元素都是不可变的，可以作为字典的键或集合的元素。
    d = {(1, 2): "value"}  
    # mytuple = (1,) # 元祖只有一个元素时，需要加逗号，否则会被识别为int
    mytuple= ("hello","hello", (2, 3), [4, 5])
    mytuple.count("hello") # 元素出现的次数
    mytuple.index(3) # 索引为3的元素
    mytuple[3] # 索引为3的元素

    # 元祖生成式
    t=tuple(
        (item for item in range(1,11))
    )
```

## 字符处理

```python
# 格式化输出
name = "罗涛"
age = 18
score=99.9
print("我的名字是%s,我的年龄是%d,成绩%.1f" % (name, age,score))
print(f"我的名字是{name},我的年龄是{age},成绩{score}")
print("我的名字是{1},我的年龄是{0},成绩{2}".format(age,name,score))

# 字符处理
s = "aa,bb "
print(s.find("b", 1))  # 从第二个开始找第一次出现的下标 3,找不到则返回-1
print(s.index("b"))  # 第一次出现下标 3,找不到则报错
print(s.count("b"))  # 出现次数 2
print(s.split(","))  # 切割为列表 ['aa', 'bb ']
print(s.strip(","))  # aa,bb移除字符串头尾指定的字符（默认为空格或换行符）
stringList = ["我", "爱", "你"]  # 列表
print("".join(stringList))  # 我爱你
print("".join(stringList[1:]))  # 爱你

str="helloworld"
print(str.center(20,"*"))
print(str.replace("o", "你好",1))  

# 拼接
print('*'.join(['hello','world']))
print('hello''world')

# 去重
str="helloworldhelloworld"
newStr=''
for item in str:
    if item not in newStr:
        newStr+=item
print(newStr)
# set去重
listStr = list(set(str))
print(''.join(sorted(listStr,key=str.index,reverse=False))) # 不修改原列表
listStr.sort(key=str.index) # 排序，会修改原列表
print(''.join(listStr)) 




```

## 正则表达式

| 元字符 | 描述说明                     | 举例               | 结果                                      |
|--------|------------------------------|--------------------|-------------------------------------------|
| `.`    | 匹配任意字符（除`\n`）       | `'p\ny\to\tn'`     | p、y、t、h、o、`\t`、n                   |
| `\w`   | 匹配字母、数字、下划线       | `'python\n123'`    | p、y、t、h、o、n、1、2、3                |
| `\W`   | 匹配非字母、数字、下划线     | `'python\n123'`    | `\n`                                      |
| `\s`   | 匹配任意空白字符             | `'python\t123'`    | `\t`                                      |
| `\S`   | 匹配任意非空白字符           | `'python\t123'`    | p、y、t、h、o、n、1、2、3                |
| `\d`   | 匹配任意十进制数             | `'python\t123'`    | 1、2、3                                   |

| 限定符 | 描述说明                           | 举例         | 结果                                      |
|--------|------------------------------------|--------------|-------------------------------------------|
| `?`    | 匹配前面的字符0次或1次             | `colou?r`    | 可以匹配`color`或`colour`                 |
| `+`    | 匹配前面的字符1次或多次            | `colou+r`    | 可以匹配`colour`或`colouuu...r`           |
| `*`    | 匹配前面的字符0次或多次            | `colou*r`    | 可以匹配`color`或`colouuu....r`           |
| `{n}`  | 匹配前面的字符n次                  | `colou{2}r`  | 可以匹配`colouur`                         |
| `{n,}` | 匹配前面的字符最少n次              | `colou{2,}r` | 可以匹配`colouur`或`colouuu...r`          |
| `{n,m}`| 匹配前面的字符最小n次，最多m次     | `colou{2,4}r`| 可以匹配`colouur`或`colouuur`或`colouuurr`|

| 其它字符       | 描述说明                           | 举例               | 结果                                      |
|----------------|------------------------------------|--------------------|-------------------------------------------|
| 区间字符[]     | 匹配[]中所指定的字符               | `[\.\?\!]`<br>`[0-9]` | - 匹配标点符号点、问号、感叹号<br>- 匹配0、1、2、3、4、5、6、7、8、9 |
| 排除字符^      | 匹配不在[]中指定的字符             | `[^0-9]`           | 匹配除0、1、2、3、4、5、6、7、8、9的字符 |
| 选择字符 \|    | 用于匹配\|左右的任意字符           | `\d{18}\|\d{15}`   | 匹配15位身份证或18位身份证                |
| 转义字符       | 同Python中的转义字符               | `\.`               | 将.作为普通字符使用                      |
| `[\u4e00-\u9fa5]` | 匹配任意一个汉字                   |                    |                                           |
| 分组()         | 改变限定符的作用                   | `six\|fourth`<br>`(six\|four)th` | - 匹配six或fourth<br>- 匹配sixth或fourth |

```python
import re

# match 从开始位置匹配
match=re.match(pattern='\d\.\d+', string='3.12python', flags=re.I)
print('匹配值的起始位置',match.start())
print('匹配值的结束位置',match.end())
print('匹配区间的位置元素',match.span())
print('待匹配的目标字符串',match.string)
print('匹配到的数据',match.group())

# search 在整个字符串搜索【第一个】匹配的值
match=re.search(pattern='\d\.\d+', string='3.12python python3.11', flags=re.I)
print('search匹配到的数据',match.group()) # 3.12

# findall 在整个字符串搜索所有匹配的值，返回一个list
lst=re.findall(pattern='\d\.\d+', string='python3.11 python3.12', flags=re.I)
print('findall匹配到的数据',lst) # ['3.11', '3.12']

# sub 对匹配的值替换
print(re.sub(pattern='黑客|破解',repl='***',string='我想作为一名黑客去破解'))

# split 对匹配的值进行分割,返回一个list
print(re.split(pattern='[?|&]',string='https://www.baidu.com/s?wd=java&status=1')) # ['https://www.baidu.com/s', 'wd=java', 'status=1']

```



## match

```python
data=eval(input("输入要匹配的数据："))
match data:
    case {'name':'neko','age':18}:
        print('dic')
    case [10,20,30]:
        print('list')
    case (10,20,30):
        print('tuple')
    case _:
        print('相当于if中的else')


nameList=['张三','李四','王五']
ageList=[18,19,20]
for n,a in zip(nameList,ageList):
    match n,a:
        case '张三',18:
            print('张三18')
        case '李四',19:
            print('李四19')
        case '王五',20:
            print('王五20')
        case _:
            print('其他')
```



## 字典

```python
def dicCRUD():
    d = dict()
    d["name"] = "张三" # 增加新键值对
    d["age"] = 25
    d["city"] = "北京"
    print(f"原始数据==>{d}")

    # 通过映射函数zip(lst1,lst2)创建字典
    zipObj=zip([10,20,30],['cat','dog','pig'])
    # print(list(zipObj)) # 转为列表后，每个元素都是元祖类型
    print(dict(zipObj))

    # 通过参数创建字典
    d1=dict(name='neko',age=18) 

    # 字典生成式
    import random
    dictA={item:random.randint(1,100) for item in range(10)}
    dictB={k:v for k,v in zip([1,2,3],['cat','dog','pig'])} # {1: 'cat', 2: 'dog', 3: 'pig'}
    # 对字典按值排序（降序）
    sorted_items = sorted(dictB.items(), key=lambda x: x[1], reverse=True) # 指定排序依据为每个元组的第2个元素，即 value
    print(sorted_items,type(sorted_items)) # [(3, 'pig'), (2, 'dog'), (1, 'cat')] <class 'list'>
    dictC = dict(sorted_items) # 还原为字典
    # 获取字典的所有键值对，返回 dict_items 对象，内容为 (key, value) 元组列表
    print({1: 'cat', 2: 'dog', 3: 'pig'}.items()) # dict_items([(1, 'cat'), (2, 'dog'), (3, 'pig')])

    # 合并字典
    mergedDic={'a':10,'b':20} | {'c':30,'d':40,'e':50}

    # 更新
    d["age"] = 26
    d.update({"email": "zhangsan@example.com","city": "深圳"}) # 批量更新/合并字典

    print(f'更新后==>{d}')

    # 查询
    print("姓名：", d.get("name"))
    print("性别：", d.get("gender", "默认值")) # 键不存在时返回设置的默认值

    # 删除
    del d["city"] # 删除指定 key
    # d.popitem() # 删除并返回字典中的最后一个kv
    d.pop("email","默认值") # 通过k删除kv并返回指定对应的value，如果k不存在则返回默认值

    # 遍历1
    for key in d:
        print(f"{key}: {d[key]}")

    # 遍历3
    for item in d.items():
        print(type(item)) # 每个item 都是 tuple类型
        print(f"{item[0]}: {item[1]}")

    # 遍历：将每个 tuple 类型的 item 拆开
    for key, value in d.items():
        print(f"{key}: {value}")

    # 遍历4
    for key in d.keys():
        print(f"{key}: {d[key]}")
    # 遍历5
    for value in d.values():
        print(f"{value}")


if __name__ == '__main__':
    dicCRUD()


```

## 集合

```python

def listCRUD():
    #  -----------Create（创建）-----------
    nameList=list() # nameList=[]
    nameList.append("neko") # 追加元素
    nameList.append("旺财")
    print(f'{nameList.insert(1, ["番茄", "鸡蛋"])}插入一个列表==>{nameList}')  # ['neko', ['番茄', '鸡蛋'], '旺财']
    newList = nameList.copy() # 复制列表，生成新的列表

    goodsList1 = ["白象", "康师傅"]
    goodsList2 = ["烤鸭", "烤鱼"]
    print(goodsList1 + goodsList2)  # 生成了新列表['白象', '康师傅', '烤鸭', '烤鱼']
    goodsList1.extend(goodsList2)  # 将一个list中的元素逐一添加到目标列表（修改原来的列表）
    print(goodsList1)

    # 列表生成式
    lst = [item for item in range(1,11) if item%2==0] # 10以内的偶数序列
    import random
    lst2 =[random.randint(1,100) for item in range(10) ] # [1,100)的10个随机数序列
    # 4行5列的二维列表
    lst3 = [[j for j in range(5)] for i in range(4)]
    for row in lst3:
        for element in row:
            print(element, end=' ')
        print()
        
    # -----------Delete（删除）-----------
    # print(nameList.pop())  # 删除最后一个元素
    # print(nameList.pop(0))  # 删除第一个元素
    # print(nameList.clear())  # 清空元素
    # if 1 in nameList:
    #     print(nameList.remove("1")) # 删除匹配到的第一个指定元素


    # -----------Read（读取）-----------
    print(f'从索引位置 0 开始查找列表中第一个"旺财" 的索引===>{nameList.index("旺财", 0)}')  # 1 
    # for遍历
    for name in nameList: 
        print(name)
    print('-' * 50)
    # lambda匿名函数式遍历列表
    for i in range(len(nameList)):
        fun = lambda name:print(nameList[i])  # lambda 参数列表: 函数体/返回值
        print(type(fun)) # <class 'function'>
        fun(i) # 调用匿名函数
    
    # for i遍历
    for i in range(len(nameList)): 
        print(nameList[i])
    # enumerate遍历,index是序号
    for index, item in enumerate(nameList):
        print(f"序号 {index} 的元素是：{item}") 
    # 指定序号从1开始    
    for index, item in enumerate(nameList,start=1):
        print(f"序号 {index} 的元素是：{item}") 

   # --------Update（更新）-----------
    # 列表切片：左闭右开区间取值
    ageList = [18, 19, 20]
    print(ageList[0:3])  # [18, 19, 20]
    print(ageList[1:])  # [19, 20]
    print(ageList[:3])  # [18,19, 20]
    name = "ABCDEF"
    print(name[1:])  # BCDEF
    # 字符串转列表
    print(list(name))  # ['A', 'B', 'C', 'D', 'E', 'F']

    # 列表排序
    orderList = ['a','c','b','d','e']
    # 排序规则为忽略大小写
    orderList.sort(key=str.lower)  # 列表.sort(key=None,reverse=False) # param1 排序规则默认None; param2 排序方式默认升序
    print(orderList)  # ['a', 'b', 'c', 'd', 'e']

    orderList = [2, 1, 3, 4, 5]
    # 内置函数sorted(iterable排序对象,key=None,reverse=False)
    newSortedList = sorted(orderList, reverse=True) # (只临时修改排序，不影响原列表)sorted临时排序(降序) [5, 4, 3, 2, 1] 

    orderList = [1, 2, 3, 4, 5]
    orderList.reverse()  # 反转
    print(orderList)  # [5, 4, 3, 2, 1]

if __name__ == '__main__':
    listCRUD()

```

## 函数

```python
def funByPos(*params): 
    """ 个数可变的位置传参的参数列表, 参数前加* ,参数类型为tuple"""
    print(type(params)) # <class 'tuple'>
    for param in params:
        print(param)
    return 6,7,8 # 返回多个值会自动封装成元组类型，可在调用处将返回的元祖解包赋值
print('-' * 50)
lst =(lambda *params: [item for item in params])(1,2,3,4,5)
print(lst) # [1, 2, 3, 4, 5]

def funBykv(**kwparams): 
    """ 个数可变的关键字传参的参数列表, 参数前加** ,参数类型为dict"""
    print(type(kwparams)) # <class 'dict'>
    for key,value in kwparams.items():
        print(key,'===>',value)
lst1=(lambda **kwparams: [f"{k}={v}" for k, v in kwparams.items()])(name='neko',age=18)
print(lst1) # ['name=neko', 'age=18']

def globleVar():
    global x # 定义全局变量，global声明与赋值不能在同一行,要先声明再赋值。
    x=100
    print(x) # 访问全局变量

def add(a,b):
    return a+b
funAdd=lambda a,b:a+b # lambda匿名函数式 等价于add函数
print(funAdd(1,2)) # 调用匿名函数

def fac(n):
    """ 递归计算n的阶乘 """
    if n==1:
        return 1 # 递归结束条件:1的阶乘为1
    else:
        return n*fac(n-1) # 自己调用自己
print(fac(5)) 



if __name__ == "__main__":
    a,b,c = funByPos(1,2,3,4,5) # 在调用处将返回的元祖解包赋值给a,b,c
    print(type(funByPos(1,2,3,4,5))) # <class 'tuple'>   
    funByPos(*[1,2,3,4,5]) # 通过*将列表中的元素解包成元祖的元素传递
    funBykv(name='neko',age=18)
    funBykv(**{'name':'neko','age':18}) # 通过**将字典中的元素解包成关键字参数传递

    # filter(function, iter) 通过指定条件过滤序列并返回一个迭代器对象 
    obj = filter(lambda x:x%2==1,range(10))
    print(list(obj)) # [1, 3, 5, 7, 9]

    # map(function, iter) 通过函数 function 对可迭代对象 iter 的操作返回一个迭代器对象
    obj= map(lambda x:x.upper(),['a','b','c'])
    print(list(obj)) # ['A', 'B', 'C']


    dictB={k:v for k,v in zip([1,2,3],['cat','dog','pig'])} # {1: 'cat', 2: 'dog', 3: 'pig'}
    # 对字典按值排序（降序）
    sorted_items = sorted(dictB.items(), key=lambda x: x[1], reverse=True) # 指定排序依据为每个元组的第2个元素，即 value
    print(sorted_items,type(sorted_items)) # [(3, 'pig'), (2, 'dog'), (1, 'cat')] <class 'list'>
    dictC = dict(sorted_items) # 还原为字典


    # reversed(sequence) 反转序列生成新的迭代器对象  
    sequence = [1, 2, 3, 4, 5]
    reversed_sequence = list(reversed(sequence))
    print(reversed_sequence)  # 输出: [5, 4, 3, 2, 1]

    # zip(iter1, iter2)   将 iter1 与 iter2 打包成元组并返回一个可迭代的 zip 对象 
    zipped = list(zip([1, 2, 3], ['a', 'b', 'c']))
    print(zipped)  # 输出: [(1, 'a'), (2, 'b'), (3, 'c')]


    # enumerate(iter)     根据 iter 对象创建一个 enumerate 对象       
    enumerated = list(enumerate(['apple', 'banana', 'cherry'],start=1)) # start=1表示序号从1开始，默认从0开始
    print(enumerated)  # 输出: [(1, 'apple'), (1, 'banana'), (3, 'cherry')]

    # all(iter)           判断可迭代对象 iter 中所有元素的布尔值是否都为 True  
    print(all([True, True, True]))    # 输出: True

    # any(iter)           判断可迭代对象 iter 中所有元素的布尔值是否都为 False 
    print(any([True, False, True]))    # 输出: False

    # next(iter)   获取迭代器的下一个元素    
    iter = iter([1, 2, 3])
    print(next(iter))  # 输出: 1
    print(next(iter))  # 输出: 2
    print(next(iter))  # 输出: 3
```

## 类

```python
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

```



## 多态

> 多态是面向对象设计思想中非常重要的一个特征。指的是多种形态，即便不知道一个变量所引用的对象到底是什么数据类型，依然可以通过这个变量去调用这个对象的方法，它会根据变量所引用对象的数据类型动态的决定要用哪个对象的方法，python中的多态不关心对象的数据类型，也不关心是否有继承，只关注对象的行为（方法），只要不同的类中具有同名的方法就可以实现多态。在java中，封装、继承和多态是必不可少的，要想实现多态必须得有继承去作前提。
>
> 封装-保护程序安全
>
> 继承-代码复用
>
> 多态-程序扩展

## 类的深拷贝与浅拷贝

![image-20250504160800008](./mypython/image-20250504160800008.png)



```python
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

```



## case-login

```python
import getpass  # 用于隐藏密码输入

users = [
    {"name": "张三", "password": "123", "status": 1},
    {"name": "李四", "password": "456", "status": 1},
    {"name": "王五", "password": "789", "status": 0}
]

def login():
    num_attempts = 3  # 最大尝试次数
    i=0
    # for attempt in range(num_attempts):
    while i<num_attempts:
        userName = input("请输入用户名（输入q退出）：").strip()
        if userName == 'q':  
            print("已退出登录")
            return #  i=4  改变循环变量以退出循环

        pwd = getpass.getpass("请输入密码：").strip()  

        # 查找用户
        user_found = False
        for user in users:
            if userName == user["name"]:
                user_found = True
                if pwd == user["password"]:
                    if user["status"] == 1:
                        print("登录成功！")
                        return  #  i=4  改变循环变量以退出循环
                    else:
                        print("用户被禁用，请联系管理员。")
                        return # i=4  改变循环变量以退出循环
                else:
                    attempts_left = num_attempts - 1 - i 
                    print(f"密码错误，还剩{attempts_left}次机会")
                    break  
        
        # 当用户不存在时显示提示
        if not user_found:
            print("用户不存在，请先注册。")
            # 不立即返回，给用户更多尝试机会
        i+=1 # 改变循环变量以退出循环
    else: # i=num_attempts时，即循环条件不成立时执行
        print("验证已锁定，请稍后再试。")

# 主程序入口
if __name__ == "__main__":
    login()

```

## 包

在 Python 中，如果一个文件夹（目录）中包含了一个名为 `__init__.py` 的文件，那么这个文件夹就会被当作一个 **Python 包（Package）**。

```python
my_package/
│
├── __init__.py      # 包初始化文件，当该包或其子模块被导入时，自动执行。
├── module_a.py      # 子模块A
└── module_b.py      # 子模块B
```

```python
# 假设 __init__.py 内容如下
print("包被导入！")
__all__ = ['module_a', 'module_b'] # 可定义 __all__ 来控制 from package import * 导入的内容
```



## 主程序

```python
print(f"当前模块名: {__name__}")
# 用于判断当前模块是作为主程序脚本直接运行还是被作为模块导入
if __name__ == '__main__':
   print('当前文件是直接运行的脚本，被导入的时候不会直接就运行')
else:
   print('__name__ 的值为模块名（文件名）,当前文件是被其他文件导入使用的模块，被导入的时候自动运行')
```

## 文件io

```python
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

```



## json

> 1. 文本格式，匹配编程语言的数据结构
>
> 2. 跨语言数据交换：用户使用python程序来向Java编写的后端接口请求数据，Java的数组和python的列表都可以转换为统一的json数组，经过转换又可以转换成python列表进行业务处理。

| JSON | Python | Java | 描述 |
|---------------|-----------------|---------------|------|
| 数组          | 列表list         | `List`（通常为 `ArrayList`）或Array | 一组有序的值       |
| 对象          | 字典dic          | `Map`（通常为 `HashMap`）    | 一组无序的键值对   |
| 数字          | 数字             | `int`, `double` 等         | 数值类型           |
| 字符串（两侧必须是双引号） | 字符串           | `String`                | 文本类型          |
| 布尔值(必须小写)  | 布尔值(必须大写)   | `boolean`               | 真或假             |
| 空值          | 空值             | `null`                  | 空值（JSON: `null`, Python: `None`, Java: `null`） |

| 操作                  | Python                                                       | Java                                                         |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 导入库                | `import json`                                                | `import org.json.JSONObject;` 或 `import com.google.gson.Gson;` |
| 序列化dic/map=>JSON   | `json.dumps(dictionary,ensure_ascii=False,indent=4) # <class 'str'>`<br>`json.dump(dictionary,open(json_filepath,'w'),ensure_ascii=False,indent=4)#持久化到json_filepath` | `new JSONObject(map).toString();` 或 `new Gson().toJson(map);` |
| 反序列化JSON=>dic/map | `obj = json.loads(json_string) # python的数据结构`<br>` obj = json.load(open(json_filepath, 'r', encoding='utf-8')) # 读取到json_filepath` | `new JSONObject(jsonString).toMap();` 或 `new Gson().fromJson(jsonString, Map.class);` |
| 对象=>JSON            | `json.dumps(object, default=str)`                            | `new Gson().toJson(object);`                                 |
| JSON=>对象            | `json.loads(json_string, object_hook=YourClass.from_dict)`   | `new Gson().fromJson(jsonString, YourClass.class);`          |

## 序列化

- 序列化：把内存中的数据转换为字节序列保存到文件
- 反序列化：从文件的字节序列恢复到内存中
- JSON（JavaScriptObjectNotation）,js对象简谱是轻量级的数据交换标准。

## case-点单系统

```python
orderList=["炒饭",10,"方便面",5]

toDo=input("===请选择操作指令:\nA添加,D删除,U修改,Q查询,E退出\n")
if toDo=="Q":
    goods=input("请输入要查询的商品：\n")
    if goods in orderList:
        index=orderList.index(goods) + 1
        print(f"{goods}的价格为{orderList[index]}")
    else:
        print("查无该商品")
elif toDo=="A":
    goods=input("===请输入要添加的商品及价格(中间用-隔开)\n")
    if goods not in orderList:
        orderList.append(goods.split("-")[0])
        orderList.append(int(goods.split("-")[1]))
        print("添加成功，添加后的菜单列表为：")
        print(orderList)
    else:
        print("不能重复添加")
elif toDo=="D":
    goods=input("===请输入要删除的商品及价格：\n")
    if goods in orderList:
        str=input("确定删除(Y/N)？" + goods + "\n")
        if str=="Y":
            indx=orderList.index(goods)
            orderList.pop(indx)
            orderList.pop(indx) # 删除后该索引的值为商品价格
            print(f"商品{goods}删除成功")
            print(orderList)
    else:
        print("删无该商品")
elif toDo=="U":
    goods=input("请输入要修改的商品名称：")
    goodsPrice=input("请输入要修改的商品的价格：")
    if goods in orderList:
        orderList[orderList.index(goods)+1]=int(goodsPrice)
        print(f"{goods}的价格已修改为{goodsPrice}")
        print(orderList)
    else:
        print("改无该商品")
elif toDo=="E":
    if input("确定退出系统(Y/N)?\n")=="Y":
        print("已成功退出系统")
```

## case-loopDemo

```python
def whileElse():
    orderList=["牛肉面","番茄鸡蛋面","炸酱面"]
    index=0
    target=input("请输入您要查找的菜品：")
    while index < len(orderList):
        if orderList[index] == target:
            print(f"找到目标值[{target}] 在索引 {index}")
            break
        index += 1
    else:  # while 循环正常结束(循环条件为假)且没有遇到 break时执行
        print("未找到目标值")

def forElse():
    orderList=["牛肉面","番茄鸡蛋面","炸酱面"]
    index=0
    target=input("请输入您要查找的菜品：")
    for order in orderList:
        if order == target:
            print(f"找到目标值[{target}] 在索引 {index}")
            break
    else: # for 循环正常结束(循环条件为假)且没有遇到 break时执行
        print("未找到目标值")

def forBreak():
    password="678876"
    num=3

    for i in range(num):
        pwd = input("请输入密码：\n")
        if pwd==password:
            print("验证通过")
            break 
        elif pwd != password and i <num-1:
            print(f"验证失败，还剩{num-1-i}次机会")
        else:
            print("验证已锁定，请稍后再试")

def whileBreak():
    password = "678876"
    num = 3
    
    i = 0
    while i < num:
        pwd = input("请输入密码：\n")
        if pwd == password:
            print("验证通过")
            break
        elif pwd != password and i < num - 1:
            print(f"验证失败，还剩{num - 1 - i}次机会")
            i += 1
        else:
            print("验证已锁定，请稍后再试")
            i += 1

def shop():
    goodsList=[]
    for i in range(5):
        goods=input("请输入商品编号和商品的名称入库(如1001手机)：")
        goodsList.append(goods)
    for item in goodsList:
        print(item)
    cart=[]
    while True:
        flag =False # 没有该商品
        num = input("请输入要购买的商品编号(q退出):")
        for item in goodsList:
            if num==item[0:4]:
                flag=True # 找到该商品
                cart.append(item)
                print(f'{item}已添加到购物车中')
                break # 退出for循环
        if not flag and num !='q':
            print("商品不存在")
        if num=='q':
            break # 退出while循环
    print('-' * 50 + '购物车中的商品有')
    cart.reverse()
    for item in cart:
        print(item)

```

## case-login

```python
import getpass  # 用于隐藏密码输入

users = [
    {"name": "张三", "password": "123", "status": 1},
    {"name": "李四", "password": "456", "status": 1},
    {"name": "王五", "password": "789", "status": 0}
]

def login():
    num_attempts = 3  # 最大尝试次数
    i=0
    # for attempt in range(num_attempts):
    while i<num_attempts:
        userName = input("请输入用户名（输入q退出）：").strip()
        if userName == 'q':  
            print("已退出登录")
            return #  i=4  改变循环变量以退出循环

        pwd = getpass.getpass("请输入密码：").strip()  

        # 查找用户
        user_found = False
        for user in users:
            if userName == user["name"]:
                user_found = True
                if pwd == user["password"]:
                    if user["status"] == 1:
                        print("登录成功！")
                        return  #  i=4  改变循环变量以退出循环
                    else:
                        print("用户被禁用，请联系管理员。")
                        return # i=4  改变循环变量以退出循环
                else:
                    attempts_left = num_attempts - 1 - i 
                    print(f"密码错误，还剩{attempts_left}次机会")
                    break  
        
        # 当用户不存在时显示提示
        if not user_found:
            print("用户不存在，请先注册。")
            # 不立即返回，给用户更多尝试机会
        i+=1 # 改变循环变量以退出循环
    else: # i=num_attempts时，即循环条件不成立时执行
        print("验证已锁定，请稍后再试。")

# 主程序入口
if __name__ == "__main__":
    login()

```



## case-店铺查询系统

```python
# 店铺查询系统
shop1 = {"地区": "北京", "面积": 100, "评分": 1}
shop2 = {"地区": "重庆", "面积": 200, "评分": 2}
shop3 = {"地区": "深圳", "面积": 300, "评分": 3}
shopList = [shop1, shop2, shop3]

while True:
    area = input("请输入要查询的地区（输入'退出'结束程序）：\n")

    # 提供退出机制
    if area == '退出':
        print("程序已退出。")
        break

    flag=False
    if area in str(shopList):
        for shop in shopList:
            if shop["地区"] == area:
                print(f"{area}地区面积{shop['面积']}，评分{shop['评分']}")
                flag=True
                break

    if not flag:
        print("没有该地区")
```

## random

```python
import random

orderList=[item for item in range(1,11)]
random.shuffle(orderList) # 打乱序列
print(random.choice(orderList)) # 随机抽卡
print(random.randint(10,50)) # 随机整数
print(random.uniform(10,50)) # 随机小数
print(random.random()) # 随机0-1
```

## time

```python
import time
# struct_time 转字符串
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) # 2025-05-04 17:46:12
print('%B月份的名称',time.strftime('%B',time.localtime())) # May
print('%A星期的名称',time.strftime('%A',time.localtime())) # Sunday
# 字符串转struct_time
print(time.strptime('2025-05-04 17:46:12','%Y-%m-%d %H:%M:%S'))

from datetime import datetime
t1 =datetime(year=2025,month=5,day=1,hour=0,minute=0,second=0) # <class 'datetime.datetime'>
t2 =datetime(year=2025,month=10,day=1,hour=0,minute=0,second=0)
print(t1<t2) # True
# datetime转字符串
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # 2025-05-04 17:59:07
# 字符串转datetime
print(datetime.strptime('2025-05-04 17:59:07','%Y-%m-%d %H:%M:%S'))

from datetime import timedelta
tsub = t2-t1
print(tsub,type(tsub)) # 153 days, 0:00:00 <class 'datetime.timedelta'>
tt=t1 + timedelta(days=10,seconds=0) #  往后10天
print(tt) # 2025-05-11 00:00:00
```



## case-饮料点单系统

```python
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

```

## 爬虫

使用程序模拟浏览器向服务器发送请求获取响应信息。

## 编码集的演变

![image-20250324180919054](./my-python/image-20250324180919054.png)

## urllib_get_post

* `user-agent`用户代理是特殊的字符串头使得服务器能识别客户使用的操作系统及版本等信息。
* 将ua放到请求对象中伪装浏览器发送请求

```bash
pip install urllib3
```

```python
import random
import urllib.request

def create_request(page):
    url_base = xxx
    # 请求参数字典
    requestParam = {
        'p': page, # 页码
        'search2': 'eelja3lfe1a1',
        'search': 'spermmania'
    }
    queryParam = urllib.parse.urlencode(requestParam)  # 将请求参数编码成查询字符串(URL编码，即%+十六进制)
    url = url_base + queryParam
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
        "Cache-Control": "max-age=0",
        "Cookie": "JSESSIONID=5E51C36C2E604BB3FCC6A6646920D35E",
        "Referer": "https//u001.25img.com/?search2=eelja3lfe1a1&search=%E5%90%88%E8%AE%A1",
        "User-Agent":
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
    }
    request = urllib.request.Request(url=url, headers=headers)  # 定义get请求对象
	""" 
	# 定义post请求对象
    data_paramEncode = urllib.parse.urlencode(param).encode('utf-8') # post请求的参数还要进行一次字节字符串编码，将 URL查询字符串转换为字节字符串
    request=urllib.request.Request(url=url_base,data=data_paramEncode,headers=headers)
	""" 
    return request


def get_content(request,proxies_pool=[{"http","117.42.94.76:19820"}]):
    if proxies_pool:
        while proxies_pool:
            # response = urllib.request.urlopen(request) # 传入定义的请求对象模拟浏览器向服务器发送请求
            # 用opener对象来发送请求并获取响应。
            # handler = urllib.request.HTTPHandler # 不用代理
            handler = urllib.request.ProxyHandler(proxies=random.choice(proxies_pool)) # 随机代理IP
            opener = urllib.request.build_opener(handler)
            try:
                response = opener.open(request)
                print(f'状态码==>{response.getcode()}') 
                # 读取所有行并连接成字节字符串并解码，然后写入文件
                content = b''.join(response.readlines()).decode('utf-8') 
                with open("u3c3.html",'w',encoding='utf-8') as fp:
                    fp.write(content)
                return content
            except Exception as e:
                print(f"请求失败，代理 {proxies} 失效: {e}")
                proxies_pool.remove(proxies)  # 移除失效的代理
        print("所有代理均失效，请检查代理池。")
        return None
    else:
        try:
            response = urllib.request.urlopen(request, timeout=10)  
            content = b"".join(response.readlines()).decode("utf-8")  
            return content
        except Exception as e:
            print(f"请求失败: {e}")
            return None
```

## requests_get_post

> 无需将请求参数编码成查询字符串(URL编码，即%+十六进制)，直接返回响应对象
>     http默认端口=80
>     http默认端口=443
>     url的组成=协议+域名+端口号+请求路径+请求参数+锚点

```bash
pip install requests
```

```python
def get_content(page,proxies_pool):
    import datetime
    import json
    import random
    import requests
    from pathlib import Path

    url_base = 'https://u001.25img.com/?'
    # 请求参数字典
    requestParam = {
        "p": page,  # 页码
        "search2": "eelja3lfe1a1",
        "search": "spermmania",
    }
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
        "Cache-Control": "max-age=0",
        "Cookie": "JSESSIONID=5E51C36C2E604BB3FCC6A6646920D35E",
        "Referer": "https//u001.25img.com/?search2=eelja3lfe1a1&search=%E5%90%88%E8%AE%A1",
        "User-Agent":
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
    }
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    ]
    headers["User-Agent"] = random.choice(user_agents) # 动态切换 User-Agent,避免被目标网站识别为爬虫

    # 目标输出
    output_dir = Path(".output")
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    output_filename = f"{timestamp}"

    # Session 对象会在底层重用 TCP 连接（通过连接池机制），减少每次请求时重新建立连接的开销，从而提升性能。
    # 在多次 HTTP 请求之间，Session 对象可以自动保存并复用 cookies。
    # 如果第一次请求登录成功后服务器返回了一个 session cookie，那么后续使用同一个 Session 对象发起的请求都会自动带上这个 cookie。
    session = requests.session() 
    print(f"session==>{session}\n{type(session)}")
    # proxies_pool=[{"http":"117.42.94.76:19820"}]
    if proxies_pool:
        while proxies_pool:
            try:
                proxies = random.choice(proxies_pool)
                response = session.get(url=url_base,params=requestParam,headers=headers,proxies=proxies, timeout=10) # 发送get请求
                # response = session.post(url=url_base,data=requestParam,headers=headers,proxies=proxies) # 发送post请求
            except Exception as e:
                print(f"请求失败，代理 {proxies} 失效: {e}")
                proxies_pool.remove(proxies)  # 移除失效的代理
            print("所有代理均失效，请检查代理池")
            return None
    else:
        response = session.get(url=url_base,params=requestParam,headers=headers) # 发送get请求
        # response = session.post(url=url_base,data=requestParam,headers=headers) # 发送post请求
    try:
        response.encoding = "utf-8"
        print(f'状态码==>{response.status_code}')
        print(f'响应头==>{response.headers}')
        print(f'二进制网页源码==>{response.content}')
        # 尝试解析 JSON 为python的数据结构
        data = response.json()
        json_str = json.dumps(data, ensure_ascii=False, indent=4)
        print(f'序列化为json字符串==>{json_str}')
        with open(output_dir / f'{output_filename}.json', 'w', encoding='utf-8') as f:  
            json.dump(data, f, ensure_ascii=False, indent=4) 
            print(f"json 已保存到 {output_dir / output_filename}.json")
        return data
    except json.JSONDecodeError:
        # 不是 JSON 格式
        print(f'网页源码==>{response.text}')
        with open(output_dir / f'{output_filename}.html', 'w', encoding='utf-8') as f:  
            f.write(response.text)  
            print(f"html 已保存到 {output_dir / output_filename}.html")
        return response.text
    except Exception as e:
        print(f"请求失败，代理 {proxies} 失效: {e}")
        return None

```

## xpath

```bash
pip install lxml 
```

```json
console.log(
    document.evaluate(
      '//mediaelementwrapper[@id="audio_player"]/audio[@id="audio_player_html5"]/@src',
      document, //查询上下文
      null,//命名空间解析器
      XPathResult.FIRST_ORDERED_NODE_TYPE, //结果类型
      null // 存储结果的对象
    ).singleNodeValue
  );
```

```js
javascript:(function(){var target=document.evaluate('//mediaelementwrapper[@id="audio_player"]/audio[@id="audio_player_html5"]/@src',document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue.value;prompt(200,target);})();
```

```python
def parse_content_xpath(content):
    """ 使用 XPath 解析 HTML 内容。 """
    tree = etree.HTML(content)  # 将响应数据解析为HTML树，并返回HTML树对象tree
    movie_name_with_rating = [text.strip() for text in tree.xpath('//*[@id="tablepress-4"]/tbody/tr/td[2]/text()') if text.strip()]  # 电影名称
    release_year_with_region = tree.xpath(
        '//*[@id="tablepress-4"]/tbody/tr/td[1]/text()'
    )  # 上映年份
    director = tree.xpath('//*[@id="tablepress-4"]/tbody/tr/td[3]/text()')  # 导演
    box_office = tree.xpath('//*[@id="tablepress-4"]/tbody/tr/td[4]//text()')  # 票房
    submitter = "luotaofun"  # 提交人



    movie_list = []
    for i in range(len(movie_name_with_rating)):
        # 提取电影名称和评分
        name_rating_text = movie_name_with_rating[i].strip() #获取单元格中的文本内容，并去除首尾空白字符。
        name_match = re.match(r'(.+?)\（(\d+\.\d+)\）', name_rating_text) 
        if name_match:
            name = name_match.group(1).strip() # (.+?)匹配任意字符（除了换行符），至少匹配一次。
            rating = name_match.group(2).strip() # (\d+\.\d+)\）匹配形如 x.y 的浮点数评分
        else:
            name = name_rating_text.strip()
            rating = None
        
        # 提取上映年份和地区
        year_region_text = release_year_with_region[i].strip()
        year_region_match = re.match(r'(\d{4})\s*(.*)', year_region_text)
        
        if year_region_match:
            year = year_region_match.group(1).strip() # (\d{4})匹配恰好 4 位数字的年份
            region = year_region_match.group(2).strip() # \s*:匹配零个或多个空白字符（包括空格、制表符等）用于处理年份和地区的间隔。(.*):匹配任意字符（除了换行符），提取地区信息。
        else:
            year = None
            region = None
        
        # 提取导演
        director_text = director[i].strip()
        
        # 提取票房并清理非数字字符
        box_office_text = box_office[i].strip()
        numeric_data = ''.join(filter(str.isdigit, box_office_text)) # #将筛选出的数字字符拼接成一个连续的字符串
        if numeric_data:
            box_office_value = int(numeric_data)
        else:
            box_office.pop(i)

        
        # 创建单部电影的信息字典
        movie_info = {
            "电影名称": name,           # 电影名称
            "上映年份": year,          # 上映年份
            "制片地区": region,        # 制片地区
            "评分": rating,        # 评分
            "导演": director_text,   # 导演
            "票房": box_office_value, # 票房
            "提交人": submitter      # 提交人
        }
        
        
        # 将当前电影信息添加到总列表中
        movie_list.append(movie_info)

    # print(movie_list)
    # 序列化为 JSON 字符串并保存
    json_str = json.dumps(movie_list, ensure_ascii=False) # 序列化才能写入：把内存中的数据转换为字节序列。ensure_ascii=False表示非 ASCII 字符保持原样

    # 保存json
    download(json_str,'./.output/movie_boxofficecn_xpath.json')

    # pandas数据处理
    columns = ["电影名称","上映年份", "制片地区", "评分", "导演",  "票房", "提交人"]
    create_table_sql = text(
        """
        CREATE TABLE `movie` (
            `id` INT not null ,
            `上映年份` text DEFAULT NULL,
            `制片地区` text DEFAULT NULL,
            `导演` text DEFAULT NULL,
            `提交人` text DEFAULT NULL,
            `电影名称` text DEFAULT NULL,
            `票房` text DEFAULT NULL,
            `评分` text DEFAULT NULL,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8
        """
    )
    print(movie_list, type(movie_list), sep="\n")
    df = pd.DataFrame(movie_list,columns=columns)
    df.index.name = "id"  # 重命名索引
    df.index = df.index + 1  # id索引从1开始
    # 创建国家代码到中文名称的映射字典
    country_code_to_chinese_name = {
        '🇨🇳': '中国',
        '🇺🇸': '美国',
        '🇮🇳': '印度',
        '🇯🇵': '日本',
        '🇫🇷': '法国',
        '🇬🇧': '英国',
        '🇫🇮': '芬兰',
        '🇦🇺': '澳大利亚',
        '🇱🇧': '莱索托'
    }
    df['制片地区'] = df['制片地区'].map(country_code_to_chinese_name).fillna(df['制片地区']) #.不能映射的 NaN 值会替换为原始 制片地区 列中的对应值。
    print(f"前几行==>\n{df.head()}")
    print(f"（行数，列数）==> {df.shape}")

    # 保存excel
    file_path = (
        f".output/yingdaomovie{str(datetime.datetime.now().strftime('%Y%m%d'))}.xlsx"
    )
    df.to_excel(file_path,index=False) # index=False 表示不保存索引

    conn_str = "mysql+mysqlconnector://root:kuroneko.678@127.0.0.1:3306/ydtest?charset=utf8mb4"
    engine = create_engine(
        conn_str
    )  # 创建sqlalchemy对象连接mysql,禁用 SQLAlchemy 在执行 SQL 语句时的输出
    with engine.connect() as conn:
        with conn.begin() as transaction:
            # # 检查表是否存在，存在则追加，否则替换
            if inspect(engine).has_table("movie"):
                # new_ids = df.index.tolist()
                # delete_sql = text(f"DELETE FROM ydtest.movie WHERE id IN ({','.join(map(str, new_ids))})")
                delete_sql = text("TRUNCATE TABLE ydtest.movie ")
                print(delete_sql)
                conn.execute(delete_sql)
                print(df.dtypes)
                print(df['制片地区'].unique())
                df.to_sql(name="movie", con=engine, if_exists="append")
            else:
                conn.execute(create_table_sql)
                df.to_sql(name="movie", con=engine, if_exists="append", index=True)
                print(conn.execute(text("show create table ydtest.movie")).first()[1])
            print(
                f"写入数据条数：{conn.execute(text('select count(id) from ydtest.movie ')).first()[0]}"
            )

    return json_str

```



## jsonpath_xpath

```
pip install jsonpath
```

| XPath                | JSONPath                    | 结果                                       |
|----------------------|-----------------------------|--------------------------------------------|
| `/store/book/author` | `$.store.book[*].author`    | 书点所有书的作者                           |
| `//author`           | `$..author`                 | 所有的作者                                 |
| `//book[3]` | `$..book[2]`     | 第三个书 |
| `//book[last()]` | `$..book[(@.length-1)]`         | 最后一本书                 |
| `//book[position()<3]` | `$..book[0,1]`<br>`$..book[:2]` | 前面的两本书。             |
| `//book[@isbn="java" and @price<60]` | `$..book[?(@.isbn=="java" && @.price<60)]` | 过滤出所有的包含isbn=java且价格小于60的书。 |
| `//book[1] | /library/book[4] `<br>`//book[position() = 1 or position() = 4]` | `$..book[0,3]` | 第一本和第四本书 |
| `//ul/li[@id="l1"]/text()` | `$..ul.li[@.id='l1']` | 找到id为`l1`的`li`标签 |
| `//ul/li[@id="l1"]/@class` | `$..ul.li[@.id='l1'].class` | 查找到id为`l1`的`li`标签的`class`属性值 |
| `//ul/li[contains(@id,"l")]/text()` | `$..ul.li[contains(@.id,'l')]` | 查询id中包含`l`的`li`标签 |
| `//ul/li[starts-with(@id,"l")]/text()` | `$..ul.li[starts-with(@.id,'l')]` | 查询id的值以`l`开头的`li`标签 |

## Beautiful Soup

```bash
pip install bs4
```

| 方法/属性                             | 描述                                                                 |
|---------------------------------------|----------------------------------------------------------------------|
| `soup = BeautifulSoup(open(html_file, encoding="utf-8"), 'lxml')` | 解析 HTML 文件                                                         |
| `soup.select('CSS选择器')[0].get_text(strip=True)` | 提取元素及其所有子元素中的所有文本内容，并将它们连接成一个字符串         |
| `soup.select('CSS选择器')[0].string`    | 仅提取元素的直接子节点中的文本内容。如果元素有多个子节点，则返回 `None`  |
| `soup.select('CSS选择器')[0].attrs`     | 获取元素的属性和属性值封装为字典                                       |
| `soup.select('CSS选择器')[0].attrs.get('元素属性')` | 通过元素的 `attrs` 属性字典获取属性值                                |
| `soup.select('CSS选择器')[0].get('元素属性')` | 通过元素对象取值                                                     |
| `soup.select('CSS选择器')[0]['元素属性']` | 通过字典的 key 取值                                                  |
| `soup.select('CSS选择器')[0].name`     | 获取元素的名称                                                       |
| `soup.a`                              | 获取第一个 `a` 标签                                                    |
| `soup.find('a')`                      | 获取第一个 `a` 标签                                                    |
| `soup.find_all('a', limit=2)`         | 返回所有 `a` 标签列表的前两个                                          |
| `soup.find_all(['a', 'b'])`           | 返回所有 `a` 标签和 `b` 标签列表                                       |
| `soup.a.attrs`                        | 获取 `a` 标签的属性和属性值封装为字典                                  |
| `soup.find('a', title='a2')`          | 获取 `title` 属性为 `a2` 的 `a` 标签                                   |
| `soup.find('a', class_='a2')`         | 获取 `class` 属性为 `a2` 的 `a` 标签，注意 `class` 需要转义              |

```python
def parse_content_bs4(content):
    """ 使用 BeautifulSoup 解析 HTML 内容。 """
    soup = BeautifulSoup(content, "lxml")
    # //*[@id="tablepress-4"]/tbody/tr/td[2]/text()
    movie_name_with_rating = soup.select('#tablepress-4 tbody tr td:nth-of-type(2)') 
    release_year_with_region = soup.select('#tablepress-4 tbody tr td:first-child') 
    director = soup.select('#tablepress-4 tbody tr td:nth-of-type(3)') 
    box_office = soup.select('#tablepress-4 tbody tr td:nth-of-type(4)') 
    submitter = "luotaofun"

    movie_list = []
    for i in range(len(movie_name_with_rating)):
        # 提取电影名称和评分
        name_rating_text = movie_name_with_rating[i].get_text(strip=True) #获取单元格中的文本内容，并去除首尾空白字符。
        name_match = re.match(r'(.+?)\（(\d+\.\d+)\）', name_rating_text) 
        if name_match:
            name = name_match.group(1).strip() # (.+?)匹配任意字符（除了换行符），至少匹配一次。
            rating = name_match.group(2).strip() # (\d+\.\d+)\）匹配形如 x.y 的浮点数评分
        else:
            name = name_rating_text.strip()
            rating = None
        
        # 提取上映年份和地区
        year_region_text = release_year_with_region[i].get_text(strip=True)
        year_region_match = re.match(r'(\d{4})\s*(.*)', year_region_text)
        
        if year_region_match:
            year = year_region_match.group(1).strip() # (\d{4})匹配恰好 4 位数字的年份
            region = year_region_match.group(2).strip() # \s*:匹配零个或多个空白字符（包括空格、制表符等）用于处理年份和地区的间隔。(.*):匹配任意字符（除了换行符），提取地区信息。
        else:
            year = None
            region = None
        
        # 提取导演
        director_text = director[i].get_text(strip=True)
        
        # 提取票房并清理非数字字符
        box_office_text = box_office[i].get_text(strip=True)
        numeric_data = ''.join(filter(str.isdigit, box_office_text)) # #将筛选出的数字字符拼接成一个连续的字符串
        if numeric_data:
            box_office_value = int(numeric_data)
        else:
            box_office_value = None
        
        # 创建单部电影的信息字典
        movie_info = {
            "name": name,           # 电影名称
            "year": year,          # 上映年份
            "region": region,        # 制片地区
            "rating": rating,        # 评分
            "director": director_text,   # 导演
            "box_office": box_office_value, # 票房
            "submitter": submitter      # 提交人
        }
        
        # 将当前电影信息添加到总列表中
        movie_list.append(movie_info)
        
    # print(movie_list)
    # 序列化为 JSON 字符串并保存
    json_result = json.dumps(movie_list, ensure_ascii=False,indent=4) # 序列化才能写入：把内存中的数据转换为字节序列。ensure_ascii=False表示非 ASCII 字符保持原样
    return json_result
   
```



## pandas-数据结构

- **DataFrame** 存储二维数据，整个表格，多行多列
  - `df.index`：表示 DataFrame 的索引（行标签）。
  - `df.columns`：表示 DataFrame 的列标签。

- **Series** 用于处理一维数据，是 DataFrame 中的一行或一列。

| Name     | Age  |
| -------- | ---- |
| luotao   | 18   |
| kuroneko | 20   |

![image-20250421200809793](./my-python/image-20250421200809793.png)

## openpyxl

```python
""" 
pip install openpyxl
"""
import openpyxl
import os
import datetime

def writeExcelByOpenpyxl():
    """ 通过openpyxl写入excel """
    workbook = openpyxl.Workbook() # 创建一个workbook对象
    del workbook['Sheet'] # 删除默认自带的sheet 等价于：workbook.remove(workbook['Sheet']) 
    sheet = workbook.create_sheet("student") # 创建一个sheet工作簿对象
    sheet.append(['姓名','年龄','成绩']) # 添加表头
    nameList=['张三','李四','王五']
    ageList=[18,19,20]
    scoreList=[i for i in range(3)]
    zipObj= zip(nameList,ageList,scoreList) # 将打包成元组并返回一个可迭代的 zip 对象 
    for name,age,score in zipObj:
        sheet.append([name,age,score]) # 迭代添加每个列表，一个列表对应工作簿的一行

    # 创建输出目录
    output_path = ".output"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    filepath = os.path.join(output_path,  f"学生信息-{(datetime.datetime.now().strftime('%Y%m%d'))}.xlsx")  # 拼接完整的文件保存路径
    workbook.save(filepath)

def readExcelByOpenpyxl():
    """ 通过openpyxl读取excel """
    workbook = openpyxl.load_workbook(filename=r"D:\workspace\python-projects\my-pythonapp\.output\学生信息-20250504.xlsx") #raw string，不处理转义字符
    sheet = workbook['student'] # 获取工作簿对象
    rowList=[] # 存储行数据,最后是一个二维列表
    for row in sheet.rows: # 遍历工作簿的每一行
        # rowList.append(row)
        # print(row,type(row)) # (<Cell 'student'.A1>, <Cell 'student'.B1>, <Cell 'student'.C1>) <class 'tuple'>
        rowData = [cell.value for cell in row] # 获取行数据: 每个单元格数据组成的列表 ['张三', 18, 0]
        print(rowData)
        rowList.append(rowData)
    for row in rowList:
        print(row)



```

## PyInstaller

```bash
pip install pyinstaller
```

```bash
# -F 等同于 --onefile，创建单个可执行文件
pyinstaller -F your_script.py

# -w 等同于 --noconsole/--windowed，隐藏控制台窗口（适用于GUI程序）
pyinstaller -w your_script.py

# -i 等同于 --icon，指定应用程序图标
pyinstaller -i icon.ico your_script.py

# -n 等同于 --name，指定输出的应用程序名称
pyinstaller -n AppName your_script.py

# -D 等同于 --onedir，创建包含多个文件的目录（默认选项）
pyinstaller -D your_script.py

# -c 等同于 --console，创建控制台应用程序（默认选项）
pyinstaller -c your_script.py

# 组合使用简写选项示例
pyinstaller -F -w -i icon.ico -n MyApp your_script.py

# 添加启动画面（实验性功能）
pyinstaller --splash=splash_image.png your_script.py

```



# Selenium 元素定位

> Selenium 可以模拟人在浏览器上的操作，比如点击按钮、输入文字。通过driver驱动真实浏览器测试，模拟浏览器自动执行网页中的js，实现动态加载。

**准备工作：** 在使用这些方法前，通常需要先导入 `By` 类：

```python
def setup_driver():
    """ 初始化并返回 Selenium WebDriver 实例。 """
    from pathlib import Path
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.common.exceptions import WebDriverException
    try:
        driver_path = Path("crawler/chromedriver.exe").resolve()
        if not driver_path.exists():
            print(f"错误：ChromeDriver 未找到：{driver_path}")
            print(
                "请下载与您的 Chrome 浏览器版本匹配的 ChromeDriver 并放置在 crawler 目录下。"
            )
            return None
        service = Service(executable_path=str(driver_path))

        # 配置无头模式
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # 无头模式
        options.add_argument("--disable-gpu")  # 禁用 GPU 加速（在某些系统上需要）
        options.add_argument("--window-size=1920x1080")  # 设置窗口大小
        browser = webdriver.Chrome(service=service, options=options)
        # browser = webdriver.Chrome(service=service)
        print("WebDriver 初始化成功。")
        return browser
    except WebDriverException as e:
        print(f"初始化 WebDriver 时出错: {e}")
        return None
    except Exception as e:
        print(f"初始化 WebDriver 时发生未知错误: {e}")
        return None

```

**核心方法：**

```python
driver.find_element(By.定位策略, "定位值")	# 找到第一个匹配的元素。如果找不到会报错。
driver.find_elements(By.定位策略, "定位值")# 找到所有匹配的元素，返回一个列表。如果找不到，返回空列表。
```

**常用定位策略：**

```python
# By.ID	
# 假设网页有个输入框 <input type="text" id="username">
element = driver.find_element(By.ID, "username")

# By.NAME 
# 通过元素的 name 属性定位。一个页面上可能有多个元素 name 相同。find_element 只会找到第一个。
# 假设网页有个输入框 <input type="password" name="password">
element = driver.find_element(By.NAME, "password")

# By.CLASS_NAME
# 假设网页有几个按钮 <button class="submit-button">提交</button>
element = driver.find_element(By.CLASS_NAME, "submit-button") #	找第一个
elements = driver.find_elements(By.CLASS_NAME, "submit-button")	# 找所有

# By.TAG_NAME	
# 通过元素的 HTML 标签名定位，比如 <div>, <p>, <a>, <img> 等。通常会找到很多个。
elements = driver.find_elements(By.TAG_NAME, "p")	# 找到页面上所有的段落 <p>这是一个段落。</p>

# By.LINK_TEXT
# 精确匹配链接 <a> 标签的完整可见文本。专门用来定位超链接。
# 假设网页有个链接 <a href="#">点击这里查看详情</a>
element = driver.find_element(By.LINK_TEXT, "点击这里查看详情")

# By.PARTIAL_LINK_TEXT
# 模糊匹配链接 <a> 标签的部分可见文本。如果链接文字很长，或者只想通过其中几个字定位时很有用。
# 还是上面的链接 <a href="#">点击这里查看详情</a>
element = driver.find_element(By.PARTIAL_LINK_TEXT, "查看详情")

# By.CSS_SELECTOR
element = driver.find_element(By.CSS_SELECTOR, "#username")	# 等同于 By.ID
element = driver.find_element(By.CSS_SELECTOR, ".submit-button") # 等同于 By.CLASS_NAME
element = driver.find_element(By.CSS_SELECTOR, "button.submit-button")
element = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]') # 等同于 By.NAME
element = driver.find_element(By.CSS_SELECTOR, "div > p") # 找 div 下的直接子元素 p

# By.XPATH
element = driver.find_element(By.XPATH, "//input[@id='username']") # 找 id 为 username 的 input 元素
element = driver.find_element(By.XPATH, "//a[contains(text(), '详情')]") # 找文本包含"详情"的 a 标签

```

# Selenium 元素操作

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 使用显式等待等待某个元素出现
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "su"))  # 等待搜索按钮出现
)

# 截取当前浏览器视口的内容，并将截图保存为指定的文件
driver.set_window_size(1920, 1080)  # 设置窗口大小
driver.save_screenshot('baidu.png')
```



```python
# 提取元素属性
attribute_value = driver.find_element_by_id('su').get_attribute('class')

# 提取元素标签名
tag_name = driver.find_element_by_id('su').tag_name

# 提取链接文本
link_text = driver.find_element_by_link_text('新闻').text

# 在文本框中输入
driver.find_elements(By.TAG_NAME, "input")[0].send_keys('kuroneko') 

# 点击按钮
driver.find_elements(By.TAG_NAME, "search")[0].click()

# 使用 JavaScript 将页面滚动到底部
time.sleep(2)
driver.execute_script('document.documentElement.scrollTop=100000')
time.sleep(2)

# 点击下一页
driver.find_element(By.PARTIAL_LINK_TEXT, "下一页").click()

# 模拟浏览器的"后退"操作，返回到上一个页面
driver.back()

# 模拟浏览器的"前进"操作，回到下一个页面
driver.forward()

# js注入
print("注入js代码...")
        time.sleep(2)
        js_script = """
        // 查找包含登录信息的表单
        const loginForm = document.querySelector('form.js-loginFormModal.js-loginForm');

        if (loginForm) {
            // 创建一个空对象来存储数据
            const formData = {};

            // 查找指定 name 属性的 input 元素并获取 value
            const fieldsToExtract = ['redirect', 'user_id', 'intended_action', 'token', 'from'];

            fieldsToExtract.forEach(fieldName => {
                const inputElement = loginForm.querySelector(`input[name="${fieldName}"]`); // 模板字符串语法嵌入表达式
                // 如果找到了 input 元素，就获取它的 value，否则设为 null
                // 用方括号表示法表示fieldName 是一个动态的变量来设置formData 对象的属性，而不是点表示法,如果直接formData.fieldName 表示为 formData 对象添加一个名为 fieldName 的属性，而不是根据 fieldName 的值动态地设置属性。
                formData[fieldName] = inputElement ? inputElement.value : null;
            });

            // 返回包含提取数据的对象 (Selenium 会自动转为 Python 字典)
            return formData;
        } else {
            // 如果没有找到表单，返回 null
            console.error('Login form not found!');
            return null;
        }
        """
        formData = driver.execute_script(
            js_script
        )  # Selenium 会自动处理 JS 对象到 Python 字典的转换
        print(f"formData==>{formData}")
```

# 无头浏览器（Headless）

> 1. PhantomJS 或 Headless Chrome
> 2. 不进行css和gui渲染，运行效率比真实浏览器高

```python
def setup_driver():
    from pathlib import Path
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.common.exceptions import WebDriverException

    """初始化并返回 Selenium WebDriver 实例。"""
    try:
        driver_path = Path("crawler/chromedriver.exe").resolve()
        if not driver_path.exists():
            print(f"错误：ChromeDriver 未找到：{driver_path}")
            print("请下载与您的 Chrome 浏览器版本匹配的 ChromeDriver 并放置在 crawler 目录下。")
            return None
        service = Service(executable_path=str(driver_path))

        # 配置无头模式
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # 无头模式
        options.add_argument('--disable-gpu')  # 禁用 GPU 加速（在某些系统上需要）
        options.add_argument('--window-size=1920x1080')  # 设置窗口大小
        browser = webdriver.Chrome(service=service, options=options)
        # browser = webdriver.Chrome(service=service)
        print("WebDriver 初始化成功。")
        return browser
    except WebDriverException as e:
        print(f"初始化 WebDriver 时出错: {e}")
        return None
    except Exception as e:
        print(f"初始化 WebDriver 时发生未知错误: {e}")
        return None
```

```python
def parse_content_with_selenium(driver, url):
    """js注入登录"""
    from pathlib import Path
    import datetime
    import time
    import json
    from selenium.common.exceptions import (
        NoSuchElementException,
        JavascriptException,
        WebDriverException,
    )
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import requests

    """
    使用 Selenium 加载 URL并注入js

    Args:
        driver: 已初始化的 Selenium WebDriver 实例。
        url (str): 要加载和解析的目标网页 URL。

    Returns:
        None: 如果找不到则返回 None。
    """
    if not driver:
        print("错误：WebDriver 未成功初始化，无法解析。")
        return None

    print(f"正在加载页面: {url} ...")
    try:
        driver.get(url)
        # 保存网页源码
        page_source = driver.page_source
        output_dir = Path(".output")
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{timestamp}_page_source.html"
        with open(output_dir / output_filename, "w", encoding="utf-8") as f:
            f.write(page_source)
        print(f"网页源码已保存到==>{output_dir / output_filename}")

        """ p1=f'{output_dir / "1点击同意#modalWrapMTubes-div-div-button.png"}'
        print(f"1点击同意==>{p1}")
        # 截取当前浏览器视口的内容，并将截图保存为指定的文件
        driver.set_window_size(1920, 1080)  # 设置窗口大小
        driver.save_screenshot(p1)
        driver.find_element(By.CSS_SELECTOR, "#modalWrapMTubes > div > div > button").click()

        headerLoginLink = driver.find_element(By.CSS_SELECTOR, "#headerLoginLink.removeAdLink.signIn")
        # 使用显式等待等待某个元素出现
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "headerLoginLink"))  # 等待元素出现
        )
        p2=f'{output_dir / "2点击登录菜单#headerLoginLink.removeAdLink.signIn.png"}'
        print(f"2点击登录菜单==>{p2}")
        driver.save_screenshot(p2)
        headerLoginLink.click()
        
        p3=f'{output_dir / "3点击登录按钮#headerLoginLink-span.png"}'
        print(f"3点击登录按钮==>{p3}")
        driver.save_screenshot(p3)
        driver.find_element(By.CSS_SELECTOR, "#headerLoginLink > span").click() """

        # 等待页面加载一些时间，特别是对于依赖 JavaScript 渲染内容的页面
        print("4注入js代码==>")
        time.sleep(2)
        js_script = """
        signinbox.show({step:'signIn'}); // 直接呼出登录表单
        // 查找包含登录信息的表单
        const loginForm = document.querySelector('form.js-loginFormModal.js-loginForm');

        if (loginForm) {
            // 创建一个空对象来存储数据
            const formData = {};

            // 查找指定 name 属性的 input 元素并获取 value
            const fieldsToExtract = ['redirect', 'user_id', 'intended_action', 'token', 'from'];

            fieldsToExtract.forEach(fieldName => {
                const inputElement = loginForm.querySelector(`input[name="${fieldName}"]`); // 模板字符串语法嵌入表达式
                // 如果找到了 input 元素，就获取它的 value，否则设为 null
                // 用方括号表示法表示fieldName 是一个动态的变量来设置formData 对象的属性，而不是点表示法,如果直接formData.fieldName 表示为 formData 对象添加一个名为 fieldName 的属性，而不是根据 fieldName 的值动态地设置属性。
                formData[fieldName] = inputElement ? inputElement.value : null;
            });

            // 返回包含提取数据的对象 (Selenium 会自动转为 Python 字典)
            console.log(formData);
            return formData; // return 给 Selenium 的 Python 字典
        } else {
            // 如果没有找到表单，返回 null
            console.error('Login form not found!');
            return null;
        }
        """
        js_data = driver.execute_script(
            js_script
        )  # Selenium 会自动处理 JS 对象到 Python 字典的转换
        # 添加登录信息
        js_data['email'] = '3452255853@qq.com'
        js_data['password'] = 'kuroneko.678'
        print(f"formData==>{js_data}\n{type(js_data)}")  # <class 'dict'>
        # --------------------------------
        headers = {
            "sec-ch-ua-full-version-list": '"Microsoft Edge";v="135.0.3179.98", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.115"',
            "sec-ch-ua-platform": '"Windows"',
            "Cache-Control": "no-cache",
            "sec-ch-ua": '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            "sec-ch-ua-model": '""',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-arch": '"x86"',
            "sec-ch-ua-full-version": '"135.0.3179.98"',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
            "Content-Type": "application/x-www-form-urlencoded",
            "sec-ch-ua-platform-version": '"19.0.0"',
            "Accept": "*/*",
            "Origin": "https://cn.pornhub.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://cn.pornhub.com/",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7",
            "Cookie": "__l=680D0CEA-42FE722901BB2C04B0-1297BE1F; ua=99d149899c4f2f3d79df1f8e73f539ef; platform=pc; bs=00000000000000001046530daa2c8e45; bsdd=00000000000000001046530daa2c8e45; ss=764865985519956585; sessid=259701793721818004; comp_detect-cookies=90419.100000; fg_afaf12e314c5419a855ddc0bf120670f=25143.100000; fg_757a7e3b2b97e62caeae14647b10ab8a=62121.100000; fg_7d31324eedb583147b6dcbea0051c868=28882.100000; __l=680D1632-42FE722901BB30C02F-13267C46; tj_UUID=ChCXGChb6Z9GrqcIgA3tuJNjEgwI8dGcwAYQ_JyOrQEYAQ==; tj_UUID_v2=ChCXGChb6Z9GrqcIgA3tuJNjEgwI8dGcwAYQ_JyOrQEYAQ==; _ga=GA1.1.1873696124.1745688120; accessAgeDisclaimerPH=1; d_uidb=ab7a7d3d-7022-a0a6-0375-30a472f64ca4; d_uid=ab7a7d3d-7022-a0a6-0375-30a472f64ca4; d_uidb=ab7a7d3d-7022-a0a6-0375-30a472f64ca4; vlc=527373886271609987; __s=680DFB54-42FE722901BB228F06-120784D2; d_fs=1; _ga_B39RFFWGYY=GS1.1.1745746775.4.0.1745746775.60.0.0",
        }
        session = requests.session()
        response = session.post(
            url='https://cn.pornhub.com/front/authenticate', data=js_data, headers=headers
        )  # 发送post请求登录https://cn.pornhub.com/front/authenticate
        output_filename = f"{timestamp}_login_source.html"
        print(f"登录源码==>{response.text}")
        with open(output_dir / f"{output_filename}", "w", encoding="utf-8") as f:
            f.write(response.text)
            print(f"登录源码已保存到 {output_dir / output_filename}")
        # if player_data:
        #     print("js注入成功。结构如下:")
        #     # 打印部分数据结构以帮助调试 (避免打印过多内容)
        #     print(json.dumps(player_data, indent=2, ensure_ascii=False)[:1000] + "...") # 完整打印可能很大
        #     # limited_data_repr = str(player_data)[:500] + ('...' if len(str(player_data)) > 500 else '')
        #     # print(limited_data_repr)

        #     print("\n正在解析数据，查找链接...")
        #     # --- 在 Python 字典中查找链接 ---
        #     # 下面的访问路径需要根据上面打印出的实际数据结构进行调整
        #     media_definitions = player_data.get('mediaDefinitions')
        #     print(f"{type(media_definitions)}\n{media_definitions}")
        #     if media_definitions and isinstance(media_definitions, list):
        #         hub_list=[]
        #         for media in media_definitions:
        #             # .get() 方法更安全，避免因 key 不存在而报错
        #             quality = str(media.get('quality', ''))
        #             video_url = media.get('videoUrl')
        #             format_info = str(media.get('format', ''))

        #             # 打印检查的条目信息，方便调试
        #             print(f"  检查: quality='{quality}', format='{format_info}', url_exists={bool(video_url)}")
        #             movie_info={
        #                 "质量":quality,
        #                 "格式":format_info,
        #                 "链接":video_url
        #             }

        #             # 检查条件：质量是 '1080'
        #             if quality in ['1080'] and video_url and  format_info:
        #                 # print(f"\n*** 成功找到链接: {video_url} ***")
        #                 hub_list.append(movie_info)

        #         print(hub_list, type(hub_list), sep="\n")
        #         df = pd.DataFrame(hub_list,columns=movie_info.keys())
        #         df.index.name = "id"  # 重命名索引
        #         df.index = df.index + 1  # id索引从1开始。
        #         print(f"前几行==>\n{df.head()}")
        #         print(f"（行数，列数）==> {df.shape}")

        #         # 保存excel
        #         file_path = (
        #             f".output/hub{(datetime.datetime.now().strftime('%Y%m%d'))}.xlsx"
        #         )
        #         df.to_excel(file_path,index=False) #

        #         print(f"\n已经将结果保存到{file_path}")

        #         return hub_list
        #     # --- 查找结束 ---

        # else:
        #     print("js注入失败")

    except JavascriptException as e:
        print(f"执行 JavaScript 时出错: {e}")
    except WebDriverException as e:
        print(f"与 WebDriver 交互时出错 {e}")
    except Exception as e:
        print(f"解析过程中发生未知错误: {e}")

    return None

```

# scrapy

> 提取网页结构化数据的框架，数据挖掘、信息处理、存储历史数据等。

```bash
pip install scrapy

# 创建项目
scrapy startproject my_scrapy

# 进入spiders目录
cd my_scrapy\my_scrapy\spiders

# 创建爬虫文件
scrapy genspider zhipin www.zhipin.com/web/geek/jobs?city=101280600&query=erp 

# 运行
scrapy crawl zhipin 

# 在settings中配置不遵守robots.txt
ROBOTSTXT_OBEY = False

# shell调试
scrapy shell https://www.zhipin.com/web/geek/jobs?city=101280600'&'query=erp
```

**目录结构**

```bash
my_scrapy/
│
├── scrapy.cfg             # 项目的配置文件
│
└── my_scrapy/             # 项目的Python模块
    │
    ├── __init__.py        # 模块初始化文件
    │
    ├── items.py           # 项目中的item文件（定义爬取的数据结构）
    │
    ├── middlewares.py     # 中间件文件（处理请求和响应）
    │
    ├── pipelines.py       # 项目中的管道文件（处理爬取的数据）
    │
    ├── settings.py        # 项目的设置文件（配置爬虫行为）
    │
    └── spiders/           # 放置爬虫的目录
        │
        ├── __init__.py    # 爬虫包的初始化文件
        │
        └── zhipin.py      # Boss直聘爬虫
```

### Scrapy工作流程

> Scrapy是一个强大的Python爬虫框架，专为高效抓取网页和提取结构化数据设计。它采用事件驱动的非阻塞架构，这使它在处理并发请求时特别高效。
>
> 从架构上看，Scrapy主要由六个核心组件组成：
>
> 1. 引擎(Engine)：作为整个框架的中枢，协调其他组件间的数据流动。
> 2. 调度器(Scheduler)：负责接收引擎发来的请求并排队，同时进行去重处理，确保不会重复爬取相同URL。
> 3. 下载器(Downloader)：负责获取网页内容并返回给引擎。
> 4. Spiders：我们自定义的爬虫类，负责处理特定网站的响应，并从中提取所需数据或新的URL。
> 5. 项目管道(Item Pipeline)：处理Spider提取的数据，执行清洗、验证和存储等操作。
> 6. 中间件系统：包括下载器中间件和Spider中间件，允许我们拦截并修改请求和响应。
>
> Scrapy的工作流程是一个完整的闭环：
>
> * 首先，引擎从Spider获取初始URL，传给调度器；
> * 调度器将URL请求排队后，引擎请求这些URL并通过下载器发送实际HTTP请求；
> * 下载器获取网页后返回给引擎，引擎再将响应提供给Spider；
> * Spider解析响应，提取数据项和新URL；
> * 提取的数据被送往管道处理，新URL则返回给引擎重新进入调度器；
> * 这个过程循环进行，直到没有更多请求。
>
> 我在实际项目中使用Scrapy时，特别欣赏它的几个技术优势：
>
> * 异步架构使其能高效处理大量并发请求；
> * 强大的中间件系统让我们可以轻松扩展功能，比如添加代理、处理Cookie等；
> * 内置的去重功能避免了爬虫陷入循环；
> * 自动化的数据处理管道简化了数据存储流程。
>
> 比如，在一个电商数据分析项目中，我使用Scrapy实现了对多个网站的并发爬取，通过自定义中间件解决了反爬验证问题，并利用管道系统将数据直接存入数据库，整个过程既高效又易于维护。

![image-20250427221612928](./mypython/image-20250427221612928.png)

## CrawlSpider

> CrawlSpider 是一个特殊的爬虫，它使用我们定义的 Rule 来自动发现和跟踪链接。非常适合爬取结构化网站，CrawlSpider 内部其实有一个非常重要的方法，也叫做 parse。它用这个内部的 parse 方法来检查每个下载下来的页面，看看符不符合我们定义的 Rule，如果符合（比如找到了“下一页”链接），就自动生成新的请求去爬取。

假设我们要爬取一个虚构的在线商店 `books.toscrape.com`（这是一个常用的 Scrapy 练习网站）。我们想：

1.  提取所有分类页面的链接。
2.  提取所有书籍详情页的链接，并交给 `parse_book` 函数处理。
3.  自动翻页，提取"下一页"的链接并继续爬取。

```bash
scrapy startproject u3c3_crawlspider

cd .\u3c3_crawlspider\u3c3_crawlspider\spiders\

# -t 是 --template 的缩写，表示指定爬虫模板的类型。
# crawl 是一种模板名称，表示生成一个基于 CrawlSpider 类的爬虫模板，这种模板支持更复杂的爬取逻辑，例如通过链接提取器（LinkExtractor）自动爬取页面中的链接。
scrapy genspider -t crawl u3c3 https://u001.25img.com/

scrapy shell "https://u001.25img.com/?p=1"
# 导入 LinkExtractor
from scrapy.linkextractors import LinkExtractor
# 提取链接
links = LinkExtractor(restrict_xpaths='//ul[@id="pageLimit"]//a[contains(@title, "Go to next page")]').extract_links(response)
# 打印提取到的链接 URL
print(f"提取到的链接数量: {len(links)}")
for link in links:
print(link.url)
```

```python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# 假设我们有一个 Item 来存储书籍信息
# from ..items import BookItem 

class BooksSpider(CrawlSpider):
    name = 'books_crawler'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    # --- 定义规则rules 元组: 每个 Rule 定义一种链接提取和处理模式。---
    rules = (
        # 规则 1: 提取书籍详情页链接
        # - 使用 LinkExtractor 查找符合特定模式的链接
        #   - restrict_css: 只在 '.product_pod .image_container' 区域内查找 a 标签
        #   - allow: 链接 URL 必须包含 'catalogue/' 且后面不是 'category/' 或 'page-'
        # - callback='parse_book': 匹配到的链接交给 parse_book 方法处理
        # - follow=False: 不再从书籍详情页继续提取链接 (通常详情页没有我们需要跟进的链接)
        Rule(
            LinkExtractor(
                restrict_css='.product_pod .image_container a',
                allow=r'catalogue/(?!category/|page-)', # 正则表达式：匹配 catalogue/ 但排除 category/ 和 page-
            ),
            callback='parse_book',
            follow=False
        ),

        # 规则 2: 提取并跟进"下一页"链接
        # - 使用 LinkExtractor 查找"下一页"按钮
        #   - restrict_css: 只在 '.pager .next' 区域内查找 a 标签 (更精确)
        # - callback=None (或省略): 使用默认的 parse 方法处理 (CrawlSpider 默认会继续应用所有 rules)
        # - follow=True (默认): 跟进这些链接，在新页面继续应用所有规则
        Rule(
            LinkExtractor(
                restrict_css='.pager .next a'
            ),
            follow=True # 默认就是 True
        ),

        # 规则 3: 提取并跟进"分类"链接 
        Rule(
            LinkExtractor(
                restrict_css='.side_categories ul li ul li a',
                allow=r'catalogue/category/books/'
            ),
            follow=True # 跟进分类链接，在分类页面继续应用规则
        ),
    )

    def parse_book(self, response):
        """
        处理从规则 1 提取到的书籍详情页响应。
        """
        self.logger.info(f'Parsing book page: {response.url}')

        # 在这里提取书籍的具体信息，例如标题、价格、评分等
        item = BookItem()
        item['title'] = response.css('h1::text').get()
        item['price'] = response.css('.price_color::text').get()
        #... 其他字段 ...
        yield item


# --- Item 定义 ---
# 在 items.py 文件中定义
# import scrapy
# class BookItem(scrapy.Item):
#     title = scrapy.Field()
#     price = scrapy.Field()
#     upc = scrapy.Field()
#     # ... 其他字段 ...
```

## Playwright

> Scrapy Playwright 是一个 Scrapy 的下载处理器 (Download Handler)，利用了微软的 Playwright 库。Playwright 可以驱动一个真实的浏览器内核（如 Chromium, Firefox, WebKit）来加载网页，执行 JavaScript，就像真实用户在浏览器中看到的那样。
> Scrapy Playwright 会在后台启动一个浏览器，加载请求的 URL，等待 JavaScript 执行完毕（包括 bootstrapPaginator 生成分页链接），然后将渲染后的完整 HTML 交给 Scrapy 的后续流程（比如LinkExtractor 和 parse 方法）

```bash
分页链接是由 JavaScript 动态生成的： 这是最可能的情况。网页先加载一个基本的 HTML 框架（包含空的 <ul id="pageLimit"></ul>），然后浏览器执行页面中的 JavaScript 代码，这些代码再去计算总页数、当前页等，最后才把生成的 <li><a>1</a></li>, <li><a>2</a></li>, <li><a title="Go to next page">></a></li> 等内容添加到那个空的 <ul> 里面去
```

```bash
pip install scrapy-playwright
# 安装 Playwright 需要的浏览器核心
playwright install
```

```bash
    # settings.py

    # --- 添加 Playwright 下载处理器 ---
    DOWNLOAD_HANDLERS = {
        "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    }

    # --- 添加 Twisted Reactor (Playwright 需要 asyncio) ---
    TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

    # --- （可选）配置 Playwright ---
    PLAYWRIGHT_BROWSER_TYPE = "chromium"  # 可以是 'firefox' 或 'webkit'
    # PLAYWRIGHT_LAUNCH_OPTIONS = {         # 比如设置无头模式 (默认就是 True)
    #     "headless": True,
    # }
    # 增加默认超时时间 (单位：毫秒)，如果页面加载或 JS 执行较慢
    # PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = 30000 # 默认 30 秒
```

## 网络编程

![image-20250505173523563](./mypython/image-20250505173523563.png)

## TCP

> `Transmission Control Protocol`传输控制协议在四层协议中的传输层。建立在IP协议基础上，保证两台计算机之间数据包按顺序到达并建立连接。是面向连接的，即需要先连接目标服务器。
>
> 传输效率比`UDP`低，连接对象数量只能是一对一。
>
> eg：打电话，请求对方建立连接，若对方没有接听就无法连通，就不可以通信。
>
> 网络接口层、网际层、传输层、应用层
>
> 三次握手：确保双方都确认自己的发送和接收能力
>
> 1. 客户端发送一个SYN=1的同步信号并随机生成序列号seq=x，表示客户端是已发送状态
> 2. 服务器收到SYN=1的同步信号后回复给客户端一个确认信号ACK=1和SYN=1同步信号并随机生成序列号seq=y,然后将ACK更新为客户端的序列号+1,表示服务端为已接受状态
> 3. 客户端回复一个确认信号ACK=1并将其跟新为服务器的序列号+1，表示双方的连接正式建立
>
> ```
> Client                        Server
> SYN=1, seq=x         --->
>                      <--     SYN=1, ACK=1, ack=x+1, seq=y
> ACK=1, ack=y+1       --->
> 
> ```
>
> 四次挥手：
>
> 1. 客户端发送一个FIN=1的结束信号并随机生成序列号seq=x，此时客户端是已发送状态
> 2. 服务器收到FIN=1的结束信号后回复给客户端一个确认信号ACK=1,然后将ACK更新为客户端的序列号+1,此时服务器可能还有未发送完的数据
> 3. 等服务端将数据发送完毕后，回复一个结束信号FIN=1并生成随机序列号seq=y
> 4. 客户端回复一个确认信号ACK=1并将其跟新为服务器的序列号+1，表示客户端才真正进入关闭
>
> ```
> Client                        Server
> FIN=1, seq=x          --->
>                       <--     ACK=1, ack=x+1
>                       <--     FIN=1, seq=y
> ACK=1, ack=y+1        --->
> 
> ```
>
> 

![image-20250505175252881](./mypython/image-20250505175252881.png)

![image-20250505175801141](./mypython/image-20250505175801141.png)

![image-20250505180112519](./mypython/image-20250505180112519.png)

![image-20250505225919595](./mypython/image-20250505225919595.png)

```python
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
```

```python
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
```



## UDP

> `User Datagram Protocol`是面向无连接的传输层协议，无法保证数据一定到达接受方。只要知道目标IP和端口，即可发送数据包，无需先连接目标服务器。
>
> 支持一对一、一对多、多对多的交互通信。
>
> 传输效率比TCP高。网站那种咨询、实时消息，基本都是用UDP实现的。
>
> eg：发短信，不需要知道对方是否在线也不需要手机号码是否正确，你只要发送即可，但不能保证数据一定能到达接受方。

![image-20250505225935488](./mypython/image-20250505225935488.png)

```python
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
```

```python
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
```



## 端口号

> 区分计算机中运行的应用程序的整数。
>
> 范围：[0,65535]
>
> 80分配给HTTP服务，21分配给FTP服务，3306分配给mysql

## socket

> 描述IP和端口号的。

![image-20250505181826456](./mypython/image-20250505181826456.png)

## 多线程

> 一个应用程序多任务的方式采用的是多进程，一个进程多任务的方式采用的是多线程。
>
> 线程是CPU调度的最小单位，属于进程，是进程的运作单位。进程是指启动后的应用程序，操作系统会为进程分配内存空间。一个进程中可拥有多个线程并发执行，每个线程并行执行不同的任务。一个进程内的所有线程共享这个进程的资源。


## 并发模式：生产者消费者

**示例代码:** (`python-base/生产者消费者.py`)

```python
import threading
import queue
import time
import random

# 共享的缓冲区（队列）作为生产者和消费者之间的中介，允许它们异步工作。生产者不需要等待消费者处理完，消费者也不需要等待生产者生成。
# 队列可以作为缓冲区，平衡生产者和消费者的速度差异，避免任务丢失。
# 设置最大容量为 5，就像一个最多只能放 5 个面包的货架
shared_queue = queue.Queue(maxsize=5)

# 特殊的结束信号，告诉消费者没有更多任务了
SENTINEL = None # 哨兵

class Producer(threading.Thread):
    """
    生产者线程：负责生成数据或任务，并将其放入一个共享的缓冲区（队列）
    就像面包师，不停地烤面包放到货架上
    """
    def __init__(self, queue, name="Producer", items_to_produce=10): # items_to_produce:要生产的总物品数量
        super().__init__(name=name)
        self.queue = queue
        self.items_to_produce = items_to_produce

    def run(self):
        print(f"{self.name}: 开始生产...")
        for i in range(self.items_to_produce):
            item = f"产品-{i}"
            # 模拟生产需要时间
            time.sleep(random.uniform(0.1, 0.5))
            print(f"{self.name}: 生产了 -> {item}")
            # 将产品放入队列，如果队列满了，put() 会阻塞等待
            self.queue.put(item)
            print(f"{self.name}: 放入队列 <- {item} (队列大小: {self.queue.qsize()})")
        print(f"{self.name}: 生产结束。")
        # 注意：这里不直接放 SENTINEL，由主线程统一放置

class Consumer(threading.Thread):
    """
    消费者线程：从共享缓冲区中获取数据或任务，并进行处理。
    就像顾客，从货架上拿面包吃,模拟从队列中取出物品并消费
    """
    def __init__(self, queue, name="Consumer"):
        super().__init__(name=name)
        self.queue = queue

    def run(self):
        print(f"{self.name}: 开始消费...")
        while True:
            # get:从队列中取出产品，如果队列空了，get() 会阻塞等待
            item = self.queue.get()
            if item is SENTINEL:
                # 如果收到结束信号，就告诉队列这个任务完成了，然后退出
                print(f"{self.name}: 收到结束信号，停止消费。")
                self.queue.task_done() # task_done：消费者从队列中取出一个任务后，当队列为空时，会唤醒调用 join() 的线程。相当于java中的notify()
                break
            else:
                # 模拟消费需要时间
                print(f"{self.name}: 拿到队列 -> {item} (队列大小: {self.queue.qsize()})")
                consume_time = random.uniform(0.2, 1.0)
                print(f"{self.name}: 正在消费 {item} (预计 {consume_time:.2f} 秒)...")
                time.sleep(consume_time)
                print(f"{self.name}: 消费完成 <- {item}")
                # 告诉队列这个任务处理完了
                self.queue.task_done()
        print(f"{self.name}: 消费结束。")

if __name__ == "__main__":
    # 设置要生产的总物品数量
    total_items = 15
    # 设置消费者数量
    num_consumers = 3

    # 创建一个生产者线程
    producer = Producer(shared_queue, items_to_produce=total_items)

    # 创建多个消费者线程
    consumers = []
    for i in range(num_consumers):
        consumer = Consumer(shared_queue, name=f"Consumer-{i+1}")
        consumers.append(consumer)

    # 启动生产者线程
    producer.start()

    # 启动所有消费者线程
    for consumer in consumers:
        consumer.start()

    # 等待生产者完成所有生产任务
    producer.join()
    print("主线程：生产者已经完成生产。")

    # 生产者完成后，向队列中放入相应数量的结束信号，确保每个消费者都能收到
    print(f"主线程：向队列放入 {num_consumers} 个结束信号...")
    for _ in range(num_consumers):
        shared_queue.put(SENTINEL) # put:入队，如果队列已满，put() 会阻塞等待

    # 等待队列中的所有任务都被处理完毕
    # join() 会阻塞，直到队列中所有放入的 item 都被 get() 并且其 task_done() 被调用
    print("主线程：等待队列为空...")
    shared_queue.join() # join:若队列不为空，join() 会阻塞等待，直到队列为空
    print("主线程：队列中的所有任务已被处理完毕。")

    # 等待所有消费者线程结束（虽然 join() 保证任务完成，但等待线程退出是好习惯）
    # for consumer in consumers:
    #     consumer.join()
    # print("主线程：所有消费者线程已结束。") # 这行通常不需要，因为 queue.join() 已经确保消费者处理完并收到 SENTINEL

    print("主线程：程序结束。")

```



## case-多人聊天室

![image-20250506202449116](./mypython/image-20250506202449116.png)

### 客户端

```python
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

```

### 服务端

```python
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

```

