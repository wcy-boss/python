ages = {
    "Lucy": 19,
    "Tom" : 18,
    "Alex": 35,
    "Jack": 19,
}

# 1. 直接遍历(所有的key)
for key in ages:
    print(key, ages[key])
    
print("------------------------")
# 2. 获取所有的key，遍历
for key in ages.keys():
    print(key, ages[key])
    
print("------------------------")

# 3. 获取所有的value
for value in ages.values():
    print(value)

print("------------------------")
# 4. 获取所有键值对
for item in ages.items():
    print(item, type(item))
    
for (key, val) in ages.items():
    print(key, val)
    
    
# 声明空集合或字典时，怎么区分
# aaa = { }
aaa = dict()
print(aaa, type(aaa))

bbb = set()
print(bbb, type(bbb))