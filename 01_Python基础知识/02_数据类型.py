# 字符串类型 str
name = "黑马喽"
# 整型变量 int 
age = 600
# 浮点类型变量 float
height = 156.42
# 布尔类型 bool
handsome = True
# 复数类型 complex j^2 = -1
# a = -3+4j

print("height->", height)
print("type:", type(height))

# 修改数值就可以改类型
height = 170
print("height->", height)
print("type:", type(height))

print("------------------------------------------")
# 非法变量名
# 123abc = 123
# abc-cdf = 123
# break = 123
# icheima.com = 123

# 合法的（字母数字下划线_）
user_name_1 = "abc"   # 下划线分割
userName2 = "bcd"      # 小驼峰
UserName3 = "def"      # 大驼峰
USERNAME4 = "234"      # 全大写

print(userName2)
print(UserName3)
print(USERNAME4)

print("--------------------------------------")
a = 5
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)    # 包含小数
print(a // b)   # 整除（不包含小数）
print(a % b)    # 取模，取余数
print(a ** b)   # 求a的b次方（次幂）

print("-" * 50)
pwd = "abc12345678"
# 字符串可以拼接
print(pwd + userName2)
# 字符串可以和数字相乘：重复N次
print(pwd * 3)

# 字符串不可以进行其他运算
# print(pwd + a)
# print(pwd - a)
