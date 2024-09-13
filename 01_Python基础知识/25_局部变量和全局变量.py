m = 666

def func():
    # 局部变量
    a = 10
    
    # 声明全局变量
    global m
    
    # 修改全局变量
    m = 888 # 无法直接修改，直接改相当于创建了一个同名局部变量m
    
    print("a1 = ", a)
    print("m1 = ", m)
    
    
def func2():
    # 局部变量
    a = 123
    
    print("a2 = ", a)
    print("m2 = ", m)
    
func()
func2()

# print("a:", a)