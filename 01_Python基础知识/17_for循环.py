string = "Hello World"
for c in string:        # 遍历字符串
    print(c, end=",")
print()

# in作用, 判断元素是否在某个容器里
print("e" in string)
print("E" in string)
print("X" in string)
print("X" not in string)