"""
1. 打印星星
2. 使用嵌套循环打印阶梯星星
3. 将星星替换成乘法口诀公式
"""

row = 1
while row <= 9:
    col = 1 # column 列   \t -> tab
    # 打印一行内容
    while col <= row:
        print("%d * %d = %d" % (col, row, col * row), end="\t")
        col += 1
    # 换行
    print()
    row += 1

print("-" * 50)    

row = 9
while row >= 1:
    col = 1 # column 列   \t -> tab
    # 打印一行内容
    while col <= row:
        print("%d * %d = %d" % (col, row, col * row), end="\t")
        col += 1
    # 换行
    print()
    row -= 1

