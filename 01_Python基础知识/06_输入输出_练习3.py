# 定义5个变量接收用户输入
name = input("姓名:")
company = input("公司:")
title = input("职位:")
telephone = input("电话:")
email = input("邮箱:")

print("*" * 30)
print(company)
print()  # 空行
print("%s (%s)" % (name, title))
print()  # 空行
print("电话：", telephone)
print("邮箱：", email)

print("*" * 30)