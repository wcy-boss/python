"""
需求
● 用户名和密码格式校验程序
● 要求从键盘输入用户名和密码，分别校验格式是否符合规则
  ○ 如果符合，打印用户名合法，密码合法
  ○ 如果不符合，打印出不符合的原因，并提示重新输入
● 用户名长度6-20，用户名必须以字母开头
● 密码长度至少6位，不能为纯数字，不能有空格

if 20 >= len(username) >= 6:
"""

while True:
    username = input("用输入用户名：")
    # 用户名长度6-20，用户名必须以字母开头
    # 不符合continue
    if len(username) < 6 or len(username) > 20:
        print("用户名长度不符合要求[6, 20]")
        continue
    
    if not username[0].isalpha():
        print("用户名必须以字母开头")
        continue

    print("用户名合法")
    # 符合break
    break
        
while True:
    password = input("请输入密码：")
    # 密码长度至少6位，不能为纯数字，不能有空格
    if len(password) < 6:
        print("密码长度至少6位")
    elif password.isdecimal():
        print("密码不能为纯数字")
    elif " " in password:
        print("密码不能有空格")
    else:
        print("密码合法：", password)
        break
    
    # 别的事情