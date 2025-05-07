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

