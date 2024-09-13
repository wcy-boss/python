a = 5
b = 2
print("-------------------------------- 赋值运算符")
a += b
print(a) # 71.0

a /= b
print(a) # 3.5

a //= b  # 整除
print(a) # 3.5 // 2 == 1.0

print(5 % 2)

print(5 ** 2)

print("------------------------------ 比较运算符")
a = 5
b = 2
print(a >= b)
print(a != b)
print(a <  b)
print(a == b)

print("------------------------------- 逻辑运算符")

# && -> and 同时为真结果为真
print("True and False: ", True and False)

# || -> or 任意为真结果为真
print("True or  False: ", True or False)

# 非 ! -> not 取反
print("not True: ", not True)