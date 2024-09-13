# 无序，不重复
sss = { "孙悟空", "猪八戒", "唐三藏", "猪八戒" ,"沙悟净" }

print(sss, type(sss))

for item in sss:
    print(item) 
    
sss.add("白骨精") 
sss.add("孙悟空") 

sss.remove("猪八戒")

sss.discard("牛魔王") # 丢弃，抛弃

sss.pop() # 随机

# 清空
sss.clear()

print(sss, type(sss))
print("----------------------")