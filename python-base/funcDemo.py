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