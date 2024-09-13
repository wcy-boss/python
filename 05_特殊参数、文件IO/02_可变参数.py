"""
可变参数 args
可变参数 kwargs (keyword)
"""


# 求N个数之和
def sum_nums(*args): 
    print(args, type(args)) # ! *元组

    rst = 0
    for i in args:
        rst += i
    return rst


# 求N个数之和
def sum_nums1(name, *args):  # keyword-only argument: 'name'
    print(name, type(name))
    print(args, type(args))

    rst = 0
    for i in args:
        rst += i
    return rst


print(sum_nums1("zhangsan", 3, 5, 1, 12, 4, 6))


def keyword_args(aaa, **kwargs):
    print(kwargs, type(kwargs)) # ! **字典
    print(kwargs["age"])
    print(kwargs["name"])
    print(aaa)


keyword_args(name="黑猴", aaa="haha", age=500, height=160.2)
