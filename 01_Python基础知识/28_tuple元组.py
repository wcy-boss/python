names = ("柯南", ) # 如果元组只有一个元素，需要添加逗号
print(names, type(names))

names = ("柯南", "毛利", "柯南", "古巨基")
print(names, type(names))

# API
print(names.count("柯南"))
print(names.index("毛利"))

print("------------------------------------ 组包和解包")

names = "鸣人", "小樱", "佐助"
print(names, type(names))

# 组包
stu = "黑猴", 99, 165.6
# 解包
name, age, height = stu

print("name: {} age: {} height: {}".format(name, age, height))

print("-------------------------------------- 数据交换")
a = 3
b = 5

# temp = a
# a = b
# b = temp
# print(a, b)

b, a = a, b
print(a, b)

print("-------------------------------------- 是否可修改")
names = "鸣人", "小樱", "佐助"
names = list(names) # 变为list，可修改
names[1] = "纲手" # assignment赋值
print(names, type(names))

names = tuple(names) # 变为tuple，不修改
names[1] = "卡卡西" # assignment赋值
print(names, type(names))
