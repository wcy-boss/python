# 使用别名
from hello import say as say_hello
from hi import say as say_hi, Nice

say_hello()
say_hi()
print(Nice().name)