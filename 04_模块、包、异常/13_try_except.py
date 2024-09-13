a = 10  # 被除数
b = 3   # 除数 

try:
    rst = a / b     # ZeroDivisionError: division by zero

    print("1---------计算后代码:", rst)
except ZeroDivisionError as e:
    print("2---------除数不能为0:", e)

print("3---------末尾代码")
