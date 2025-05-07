def setCRUD():
    s = set() # s={} # 无序、不重复、存储不可变元素

    # 集合生成式
    sa={item for item in range(1,11) if item %2==0}

    # 增
    s.add(1)
    s.add(2)
    s.update([3, 4, 5],{6,7,8}) # 添加多个元素
    print("添加后:", s)

    # 改（先删后加）

    print("修改后:", s)

    # 删
    # s.pop()  # 删除任意一个元素（因为无序）并返回一个元素
    # s.clear() 
    s.remove(1) # 删除指定元素（若不存在会抛出 KeyError）
    s.discard(100)  # 删除指定元素,不会报错
    print("删除后:", s)


    for item in s:
        print(item)


    # 并集 & 交集 
    s1 = {20,30,50,10,40}
    s2 = {20,30,50,88,76}
    print("s1 并集 s2:", s1 | s2)         # 或 s1.union(s2)
    print("s1 交集 s2:",  s1 & s2)  # 或 s1.intersection(s2)
    print("s1 差集 s2:",  s1 - s2)  
    print("s1 补集 s2:",  s1 ^ s2)  

    # 用set去重
    d=dict()
    score=[60,60,90,100,100]
    for s in set(score):
        d[s]=score.count(s)
    for k,v in d.items():
        print(f"{k} 出现了 {v} 次")

if __name__ == '__main__':
    setCRUD()