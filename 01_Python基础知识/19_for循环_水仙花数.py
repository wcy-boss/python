"""
1. 遍历所有的三位数
2. 求 百位 十位个位  立方和
3. 判断并打印
"""

for i in range(100, 1000):
    # Digits, Tens, Hundreds.
    hundreds = i // 100     # 百位
    tens     = i // 10 % 10 # 十位
    digits   = i % 10       # 个位
    if (hundreds ** 3 + tens ** 3 + digits ** 3) == i:
        print("水仙花数：{} + {} + {} = {}".format(hundreds ** 3, tens ** 3, digits ** 3, i))