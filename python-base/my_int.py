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
