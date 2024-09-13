"""-----------------------定义Person类------------------------"""

class Person(object):
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age  = age
        
    def say_hello(self):
        print('say hello from', self.name)
    
    def eat(self):
        print(self.name, 'eat')        
        
    def __str__(self) -> str:
        return "name: {} age: {}".format(self.name, self.age)

"""----------------- 定义Student类继承Person类-----------------"""
class Student(Person):
    
    def __init__(self, name, age, score) -> None:
        # 必须要调用父类的初始化方法，传递参数
        super().__init__(name, age)
        # 定义自己的属性
        self.score = score
        
    def play_game(self):
        print(f"{self.name}打游戏")

    def __str__(self) -> str:
        return "学生 name: {} age: {} score: {}".format(self.name, self.age, self.score)
    
    
# 创建学生对象
stu = Student("小马楼", 15, 95)
print(stu) # 子类如果重写，走子类函数
# 调用父类提供的函数
stu.say_hello() 
# 调用子类自己的函数
stu.play_game()