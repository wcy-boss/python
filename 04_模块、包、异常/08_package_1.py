# 引入包中模块的功能方法一
# import 包名.模块名

import pkg.hello

print(pkg.hello.name)
pkg.hello.say()
nice = pkg.hello.Nice()

print(nice.name)