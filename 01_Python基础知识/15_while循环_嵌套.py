"""
0 1 2
0 1 2
0 1 2
0 1 2
0 1 2
0 1 2
"""
# row = 6 # 行数
# col = 3 # 列数

i = 0
while i < 6:
    # print("0 1 2")
    # 打印每一行的内容
    j = 0
    while j < 3:
        print(j, end=" ") # 打印并不加换行
        j += 1
    
    print()
    
    i += 1 