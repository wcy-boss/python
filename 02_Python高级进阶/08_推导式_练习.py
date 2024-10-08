"""
请写出一段 Python 代码实现分组一个 list 里面的元素
比如 [1,2,3,...100] 变成 [[1,2,3],[4,5,6]....[100]]

[10, 20, 30, 40, 50, 60, 70, 80]

[
    [10, 20, 30],       # [0:0+3]
    [40, 50, 60],       # [3:3+3]
    [70, 80]            # [6:6+3]
]
"""
#      0           1           2
# lst = [10, 20, 30, 40, 50, 60, 70, 80]

lst = list(range(1, 101))

# 每3个数分到1个组 (左闭右开)
print(lst[0:3]) # [10, 20, 30]
print(lst[2:5]) # [30, 40, 50]

rst = [lst[i: i+3] for i in range(len(lst)) if i % 3 == 0]

print(rst)