import getpass  # 用于隐藏密码输入

users = [
    {"name": "张三", "password": "123", "status": 1},
    {"name": "李四", "password": "456", "status": 1},
    {"name": "王五", "password": "789", "status": 0}
]

def login():
    num_attempts = 3  # 最大尝试次数
    i=0
    # for attempt in range(num_attempts):
    while i<num_attempts:
        userName = input("请输入用户名（输入q退出）：").strip()
        if userName == 'q':  
            print("已退出登录")
            return #  i=4  改变循环变量以退出循环

        pwd = getpass.getpass("请输入密码：").strip()  

        # 查找用户
        user_found = False
        for user in users:
            if userName == user["name"]:
                user_found = True
                if pwd == user["password"]:
                    if user["status"] == 1:
                        print("登录成功！")
                        return  #  i=4  改变循环变量以退出循环
                    else:
                        print("用户被禁用，请联系管理员。")
                        return # i=4  改变循环变量以退出循环
                else:
                    attempts_left = num_attempts - 1 - i 
                    print(f"密码错误，还剩{attempts_left}次机会")
                    break  
        
        # 当用户不存在时显示提示
        if not user_found:
            print("用户不存在，请先注册。")
            # 不立即返回，给用户更多尝试机会
        i+=1 # 改变循环变量以退出循环
    else: # i=num_attempts时，即循环条件不成立时执行
        print("验证已锁定，请稍后再试。")

# 主程序入口
if __name__ == "__main__":
    login()
