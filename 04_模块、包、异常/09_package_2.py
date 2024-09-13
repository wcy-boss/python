# 引入包中模块的功能方法二（推荐）
# from 包名 import 模块名

from pkg import hello

# 访问模块里的变量
print(hello.name)
# 访问模块里的函数
hello.say()
# 访问模块里的类
nice = hello.Nice()
print(nice.name)