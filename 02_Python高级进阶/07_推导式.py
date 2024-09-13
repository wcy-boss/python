"""
                 2       1      3
列表 推导式： [计算公式 for循环 if判断]
"""
# lst = []
# for i in range(10):
#     if i % 2 == 0:
#        lst.append(i ** 2)

# ● 列表推导式
lst = [ ele for ele in range(10) ]
lst = [ ele for ele in range(10) if ele % 2 == 0] # 加了条件（只要偶数）
lst = [ ele ** 2 for ele in range(10) if ele % 2 == 0] # 加了条件（只要偶数的平方）
print(lst)
 
# ● 元组推导式
tup = (ele ** 2 for ele in range(2,15) if ele % 2 == 1)
print(tuple(tup))

# ● 集合推导式
ss = {ele ** 2 for ele in range(2,15) if ele % 2 == 1}
print(ss)

# ● 字典推导式 {1: "1", 3: "9", 5: "25" ... 9: "91"} 
_dict = { key: str(key**2) for key in range(1, 11) if key % 2 == 1 }
print(_dict, type(_dict))

lst1 = ["张三", "李四", "王五"]
lst2 = [13, 14, 15, 224, 41, 12]
# {"张三":13, "李四":14, "王五":15}
# 把两个数据打包
print(list(zip(lst1, lst2)))

_dict = { k: v for k, v in zip(lst1, lst2) }
print(_dict)


lst3 = [" 张三  ", " 李四  ", "    王五  "]
lst = [name.strip() for name in lst3]