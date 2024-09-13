# 定义变量
name = "张三外挂！"

# 定义函数
def add(a, b):
    return a + b

# 声明Person类
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): # 覆写，重写
        return f"姓名:{self.name} 年龄:{self.age}"
    
# 如果__name__不是__main__，说明本文件是被别人调用了
# 如果此文件被别人导入，__name__是本模块名
# print("__name__", __name__)

if __name__ == "__main__":
    # 写主函数的入口，写一些模块测试代码
    print("软件名：", name)
    print("正常运行")
    print(add(3, 5))
# else:
#     print("本作者是王八蛋，小姨子跟老板跑路了！！！")
#     exit()
    