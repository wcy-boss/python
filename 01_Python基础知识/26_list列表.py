name_list = ["流川枫", "佐助", "纲手", "路飞", "柯南", "路飞"]

# CRUD 

# 查询
print(name_list[2])
# 查询指定元素的位置（索引）
# 如果元素不存在，报异常：ValueError: '鸣人' is not in list
print(name_list.index("路飞"))

# 追加
name_list.append("雏田")
name_list.append("鸣人")
print(name_list)

# 移除
# 按照元素内容
name_list.remove("路飞")
# 按照元素索引 (无参时默认移除最后一个)
print(name_list.pop(1))
print(name_list)

# 修改
name_list[2] = "滚筒洗衣机"
print(name_list)

# 遍历
for name in name_list:
    print("->",name)
    
print("-----------------------------------------")
# 排序 （原数组内容会被修改）
digit_list = [2,3,1,12,6,3,7,15,26,37,6,7]
# digit_list.sort()           # 正序排列
digit_list.sort(reverse=True) # 倒序排列
print(digit_list)

# 倒序
arg_list = [20, 40, 30, 50, 90]
# reverse 将列表进行反转
arg_list.reverse()
print(arg_list)

print("-----------------------------------------")
# 列表嵌套（多维列表）
students = [
    ["刘亦菲", "迪丽热巴", "佟丽娅"],
    ["菜虚鲲", "张曼玉"]
]

print(students[1][1])
print(students[0][1])
# 修改张曼玉位高圆圆
students[1][0] = '高圆圆'

print(students[1][4]) # IndexError: list index out of range
