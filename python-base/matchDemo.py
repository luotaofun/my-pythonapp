data=eval(input("输入要匹配的数据："))
match data:
    case {'name':'neko','age':18}:
        print('dic')
    case [10,20,30]:
        print('list')
    case (10,20,30):
        print('tuple')
    case _:
        print('相当于if中的else')


nameList=['张三','李四','王五']
ageList=[18,19,20]
for n,a in zip(nameList,ageList):
    match n,a:
        case '张三',18:
            print('张三18')
        case '李四',19:
            print('李四19')
        case '王五',20:
            print('王五20')
        case _:
            print('其他')