---
title: python
date: 2024-03-24 14:12:43
tags: python
---

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

"""
列表处理
"""
nameList = ["罗涛", "周超"]
print(nameList.index("罗涛", 0))  # 从第一个位置开始取索引
nameList.append("1")  # 追加元素
nameList.insert(1, ["番茄", "鸡蛋"])  # 插入一个列表
print(nameList)  # ['罗涛', ['番茄', '鸡蛋'], '周超', '1']
print(nameList.pop())  # 删除最后一个元素
print(nameList.pop(0))  # 删除第一个元素
print(nameList.clear())  # 清空元素
if 1 in nameList:
    print(nameList.remove("1"))

nameList1 = [1, 2, 3]
# for i in nameList1: # 遍历追加
#     nameList.append(i)
# print(nameList)
nameList.extend(nameList1)  # 将一个list中的元素逐一添加到目标列表（修改原来的列表）
print(nameList)
goodsList1 = ["白象", "康师傅"]
goodsList2 = ["烤鸭", "烤鱼"]
print(goodsList1 + goodsList2)  # 生成了新列表['白象', '康师傅', '烤鸭', '烤鱼']

# 列表切片：左闭右开区间取值
ageList = [18, 19, 20]
print(ageList[0:3])  # [18, 19, 20]
print(ageList[1:])  # [19, 20]
print(ageList[:3])  # [18,19, 20]
name = "ABCDEF"
print(name[1:])  # 字符串转列表
print(list(name))  # ['A', 'B', 'C', 'D', 'E', 'F']

# 列表排序
orderList = [2, 1, 3, 4, 5]
orderList.sort()  # 会直接修改原始列表的排序
print(orderList)  # [1, 2, 3, 4, 5]

orderList = [2, 1, 3, 4, 5]
print(sorted(orderList, reverse=True))  # sorted临时排序(降序) [5, 4, 3, 2, 1]
print(orderList)  # 只临时修改排序，不影响原列表 [2, 1, 3, 4, 5]

orderList = [1, 2, 3, 4, 5]
orderList.reverse()  # 反转
print(orderList)  # [5, 4, 3, 2, 1]
```

## 字符处理

```python
# 格式化字符串
age = 18
print(type(age))
print(f"年龄是: {age}岁")

# 格式化输出
name = "罗涛"
age = 18
print("我的名字是%s,我的年龄是%d" % (name, age))

# 字符处理
s = "aa,bb "
print(s.find("b", 1))  # 从第二个开始找第一次出现的下标 3,找不到则返回-1
print(s.index("b"))  # 第一次出现下标 3,找不到则报错
print(s.count("b"))  # 出现次数 2
print(s.replace("b", "c"))  # aa,cc
print(s.split(","))  # 切割为列表 ['aa', 'bb ']
print(s.strip(","))  # aa,bb移除字符串头尾指定的字符（默认为空格或换行符）
print(s.join("cc"))  # caa,bb c 将字符串cc中的每个成员以字符'aa,bb '分隔开再拼接成一个字符串
stringList = ["我", "爱", "你"]  # 列表
print("".join(stringList))  # 我爱你
print("".join(stringList[1:]))  # 爱你

```



## 字典

```python
# 字典
dic = {"name": "neko", "age": 18}
print(dic["name"])
print(dic.get("hobby"), "没有该键")
dic["hobby"] = "唱跳rap"
dic.pop("name")  # 删除键
dic.popitem()  # 删除一组键值对
dic.clear()  # 清空字典

for item in dic.items():
    print(item)  # 返回元祖 ('name', 'neko')

for k, v in dic.items():
    print(f"{k}是{v}")  # name是neko
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
| 序列化dic/map=>JSON   | `json.dumps(dictionary,ensure_ascii=False,indent=4)`<br>`json.dump(dictionary,open(json_filepath,'w'),ensure_ascii=False,indent=4)#持久化到json_filepath` | `new JSONObject(map).toString();` 或 `new Gson().toJson(map);` |
| 反序列化JSON=>dic/map | `obj = json.loads(json_string)`<br>` obj = json.load(open(json_filepath, 'r', encoding='utf-8')) # 读取到json_filepath` | `new JSONObject(jsonString).toMap();` 或 `new Gson().fromJson(jsonString, Map.class);` |
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

## case-forDemo

```python
password="678876"
# N次验密机会
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
```

## case-whileDemo

```pythob
orderList=["牛肉面","番茄鸡蛋面","炸酱面"]
index=0
while index < len(orderList):
    print(orderList[index])
    index+=1

while True:
    str=input("请输入\n")
    if str=="下机":
        print("下机成功")
        break
    else:
        print(str)
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

orderList=[1,2,3,4,5]
random.shuffle(orderList) # 打乱序列
print(random.choice(orderList)) # 随机抽卡
print(random.randint(10,50)) # 随机整数
print(random.uniform(10,50)) # 随机小数
print(random.random()) # 随机0-1
```

## case-饮料点单系统

```python
# _*_ coding : utf-8 _*_
# @Time : 2025/2/23 13:16
# @Author : luotao
# @File : demo
# @Project 饮料点单系统

class Drunk:
    sweet=7
    temperature="常温"
    # 构造函数
    def __init__(self,name,modle):
        self.name=name
        self.modle=modle
    # 加糖
    def addSweet(self):
        self.sweet +=1
    # 加冰
    def addTemperature(self,type):
        self.temperature=type
    def show(self):
        print(f"您点了一杯{self.temperature}{self.modle}的{self.name},甜度为{self.sweet}")

try:
    nameAndType=input("您需要什么饮料？请输入名称和杯型(中间用横杆隔开):\n")
    if not nameAndType:
        raise Exception("输入错误")
    cola=Drunk(nameAndType.split("-")[0],nameAndType.split("-")[1])
except Exception as e:
    print(e)
else:
    while True:
        cola.show()
        str=input("请问您还有其他需求吗？Y/N\n")
        if str=="N":
            print("好的，饮品马上来")
            break
        else:
            strOther=input("请问需要A加糖还是B加冰？")
            if strOther=="A":
                cola.addSweet()
            else:
                type=input("请问需要什么冰量？A:去冰，B少冰，C多冰")
                try:
                    cola.addTemperature({"A":"去冰","B":"少冰","C":"多冰"}[type])
                except KeyError as e:
                    print("选项有误，请重新输入")
finally:
    print("欢迎下次再来")

```

## 爬虫

使用程序模拟浏览器向服务器发送请求获取响应信息。

## 编码集的演变

![image-20250324180919054](./my-python/image-20250324180919054.png)

## u3c3_18_urllib_crawler

* `user-agent`用户代理是特殊的字符串头使得服务器能识别客户使用的操作系统及版本等信息。
* 将ua放到请求对象中伪装浏览器发送请求

## get和post请求

```python
# _*_ coding : utf-8 _*_
# @Time : 2025/3/24 16:39
# @Author : luotao
# @File : urllibDemo
# @Project pythonDemo
import json
import urllib.request
'''
    http默认端口=80
    http默认端口=443
    url的组成=协议+域名+端口号+请求路径+请求参数+锚点
'''
url_base = 'https://fanyi.baidu.com/sug'
# url_base = 'http://www.baidu.com/s?'
# url_base = 'https://u001.25img.com/?'
headers = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
}
# param = urllib.parse.quote('合集')#将请求参数编码成查询字符串(URL编码，即%+十六进制)
param={
    # 'wd':'合集'
    # 'search2':'eelja3lfe1a1',
    # 'search':'合集'
    'kw':'spider'
}
'''
    #get请求方式：将参数字典编码为查询字符串
    paramEncode = urllib.parse.urlencode(param) 
    url =url_base +  paramEncode
'''

paramEncode = urllib.parse.urlencode(param).encode('utf-8') # post请求的参数还要进行一次字节字符串编码，将 URL查询字符串转换为字节字符串
request=urllib.request.Request(url=url_base,data=paramEncode,headers=headers) # 请求对象
response = urllib.request.urlopen(request) # 模拟浏览器向服务器发送请求。
print(response.getcode()) # 状态码
print(response.geturl()) # url
content = b''.join(response.readlines()).decode('utf-8')# 读取所有行并连接成一个单一的字节字符串，然后解码
# 下载网页
# urllib.request.urlretrieve(url, "u3c3.html")
with open("u3c3.html",'w',encoding='utf-8') as fp:
    fp.write(content)
# print(json.loads(content))


```

## xpath

```bash
pip install lxml 
```

## jsonpath

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
