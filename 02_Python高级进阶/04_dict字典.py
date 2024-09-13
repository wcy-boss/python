ages = {
    "Tom" : 18,
    "Jack": 19,
    "Alex": 35,
}

print("增删改查-----------------------")
# 新增
ages["张三丰"] = 65 
ages.setdefault("zhangsan", 26)

# 删除
ages.pop("Jack") # Python 3.+
del ages["Tom"]  # Python 2.+

# 修改
ages["张三丰"] = 16 

# 查询
print(ages["Alex"])
print("zhangsan" in ages) # 判断是否包含

print(ages, type(ages))