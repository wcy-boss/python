"""
需求：
判断登录密码hhew2383dW_fkf&E@^是否合法。
1. 密码必须是数字、字母(大小写都可以)、和下划线，否则不合法
2. 如果密码合法,就输出"密码合法"

分析：
1. 定义容器，保存所有合法内容：数字 字母 _
2. for循环遍历密码中每一个元素
3. 判断每一个元素是否合法
4. 如果不合法，执行break
"""
# 1. 定义容器，保存所有合法内容：数字 字母 _
container = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

# 获取用户输入的密码
password = input("请输入密码：")

# 2. for循环遍历密码中每一个元素
for ele in password:
    # 密码必须是数字、字母(大小写都可以)、和下划线，否则不合法
    if ele not in container:
        print("密码不合法，包含非法字符：", ele)
        break
else:
    # 当循环顺利结束，没有执行break时，校验通过
    print("密码合法：", password)

