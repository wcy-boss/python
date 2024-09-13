age = input("年龄：")

# 强制类型转换，否则是字符串
age = int(age)

# 必须要正确缩进 tab (有语法意义) IndentationError: unexpected indent
if age >= 18:
    print("去网吧！")
else:
    print("回家写作业去！")
