
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
