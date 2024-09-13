scores = [83, 92, 100, 95, 67, 76]

def average(*args):
    print(args, type(args))
    rst = 0
    for i in args:
        rst += i
        
    return rst / len(args)

print(average(3,5,7,9))
print(average(*scores)) # 把scores拆成多个元素 （拆包）

print(*scores)
# 等同于
print(83,92,100,95,67,76)

def show_info(**kwargs):
    print(kwargs, type(kwargs))
    
stu = {
    "name": "Tom",
    "age": 20,
    "score": 90
}

show_info(name="abc", age=12)
show_info(**stu)