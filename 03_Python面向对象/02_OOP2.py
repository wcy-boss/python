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



# 根据类创建对象
p = Person("桑尼", 16)
# print(p)
# 读取对象的属性值
print(p.name)
print(p.age)
print(p.version)
# 调用对象的方法
p.eat()
p.run()
p.say_hello("小兰")

print("-----------------------")

p2 = Person("小红", 13)
# print(p)
# 读取对象的属性值
print(p2.name)
print(p2.age)