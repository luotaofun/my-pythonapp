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
