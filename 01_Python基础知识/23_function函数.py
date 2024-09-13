def say_hello():
    """打招呼
    """
    print("Hello World!")
    print("Hello World!")
    print("Hello World!")
    # shift + tab 向前缩进
        

def sum(a, b):
    """求和函数
    
    :param a: 第1个数字
    :param b: 第2个数字
    :return: 两数之和
    """
    return a + b

def my_min(x, y):
    """计算两个数较小值

    :param a: 第1个数字
    :param b: 第2个数字
    :return: 两数较小值
    """
    if x < y:
        return x
    return y

def my_max(x, y): # x = 3, y = 8
    """计算两个数较大值

    :param a: 第1个数字
    :param b: 第2个数字
    :return: 两数较小值
    """
    return x if x > y else y

def calc(a, b):
    """计算两个数的积和商
    如果第二个变量是0，商返回 None
    """
    multiply = a * b
    
    # 如果b不是0，返回 a / b ，否则返回None
    divide = a / b if b != 0 else None
    
    return multiply, divide

print(say_hello())

print("sum: ", sum(3, 8))
print("min: ", my_min(3, 8))
print("max: ", my_max(3, 8))

x, y = calc(5, 0)
print("x: {} y: {}".format(x, y))
