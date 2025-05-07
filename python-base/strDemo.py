
# 格式化输出
name = "neko"
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



