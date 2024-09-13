# 声明Person类
class Person:
    
    def __init__(self, name, age):
        """初始化函数
        """
        # print('执行了init方法')
        self.name = name
        self.age = age
        self.version = 1.0
        # print("init: ", self)

    def eat(self):
        print(self.name, "吃饭")
        
    def run(self):
        print(self.name, "跑步")
        
    def say_hello(self, target):
        print("hello: ", target)

    def __str__(self): # 覆写，重写
        # return "姓名:{} 年龄:{}".format(self.name, self.age)
        return f"姓名:{self.name} 年龄:{self.age}"

p2 = Person("小红", 13)
print(p2)

print("-----------------------")
p = Person("桑尼", 16)
print(p)
p.say_hello(p2.name)
