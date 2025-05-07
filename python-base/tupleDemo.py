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