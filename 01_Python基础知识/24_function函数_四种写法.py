import random

# 无参无返回值
def say_hello():
    print("Hello")
    
# 无参有返回值
def get_rand():
    return random.randint(10, 100)

# 有参无返回值
def say_hi(name):
    print("丸辣，泥嚎：", name)
    
# 有参有返回值
def sum(a, b):
    return a + b

say_hello()
print(get_rand())
say_hi("黑悟空")
print(sum(3, 5))