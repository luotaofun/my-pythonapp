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
