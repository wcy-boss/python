print("----------------------------------sys")
import sys

print(sys.argv)  # 模块执行参数
print(sys.argv[1:])
# print(sys.path)

print("----------------------------------time")
import time

start = (
    time.time()
)  # Unix 时间戳是从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数，不考虑闰秒。
# 用于计算间隔时间
# print(start)
# time.sleep(1)

print("duration: {}".format(time.time() - start))

print("----------------------------------datetime")
from datetime import datetime

now = datetime.now()  # 获取当前日期时间对象
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

# 将datetime格式化为字符串 f->format (格式化)
str_time = datetime.strftime(now, "%Y-%m-%d %H:%M:%S")
print(str_time, type(str_time))

# 将字符串格式化为datetime p->parse (解析)
tar_time = datetime.strptime("2024-09-05 12:21:22", "%Y-%m-%d %H:%M:%S")
print(tar_time, type(tar_time))

print("-------------------------------- 内置函数")
arr = [2, 3, 8, 3, 5, 6, 2, 1]
print(max(arr))
print(min(arr))
print(sum(arr))
print(len(arr))
print(sorted(arr))  # 得到了新的排序后的数组
print(sorted(arr, reverse=True))  # 得到了新的排序后的数组
print(arr)

print("--------------------------------- math")
import math

# 幂
print(math.pow(5, 2))
# 取整
# 向下取整
print(math.floor(1.76543))
# 向上取整
print(math.ceil(1.23456))
# 四舍五入
print(round(2.414))
print(round(3.618))

# 正余弦 PI:3.1415926 -> sin(30) -> cos(60)
# -> 30/180
print(math.pi)
print(math.sin(math.pi / 6))  # 0.5
print(math.cos(math.pi / 3))  # 0.5

print("-------------------------------------- random")
import random

# 随机整数
print(random.randint(10, 20))  # [10, 20]
# 随机小数[0, 1)
print(random.random())
# 随机浮点数
print(random.uniform(1.3, 3.2))

# 随机从列表里选数据
lst = [13, 5, 31, 12, 5, 2, 76, 32, 16]
print(random.choice(lst)) # 选择一个随机的值
print(random.choices(lst)) # 选择一个随机的值, 放到新列表里