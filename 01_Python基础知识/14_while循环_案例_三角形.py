n = int(input("请输入行数n:"))

# 正三角形
row = 1
while row <= n:
    print("* " * row)
    # 修改行数
    row += 1
    
# 倒三角形
row = n
while row >= 1:
    print("* " * row)
    # 修改*个数
    row -= 1