"""
计算n的阶乘

1 * 2 * 3 * 4 * 5 = 5!

5! = 5 * (5 - 1)!  
4! = 4 * (4 - 1)!
...
1! = 1
"""
def calc(n):
    # 结束条件
    if n == 1 or n == 0:
        return 1
    
    return n * calc(n - 1)


print(calc(5)) # calculate
print("-------------")
print(calc(0)) # calculate
# print("-------------")
# print(calc(-1)) # calculate RecursionError: maximum recursion depth exceeded while calling a Python object

# 斐波那契数列数组
def fibnacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib = fibnacci(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib
    
    
print(fibnacci(100))