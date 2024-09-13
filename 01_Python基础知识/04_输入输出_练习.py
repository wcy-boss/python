"""
需求:
● 用户输入整型变量a
● 用户输入整形变量b
● 计算输出a+b=?

int() 参数是个字符串，要求必须是纯数字
否则：ValueError: invalid literal for int() with base 10: 'Bf'
"""

# ● 用户输入整型变量a, 再类型转换
a = int(input("请输入第一个数："))
# ● 用户输入整形变量b, 再类型转换
b = int(input("请输入第二个数："))

print(type(a), type(b))

# ● 计算输出a+b=?
print(a + b)

