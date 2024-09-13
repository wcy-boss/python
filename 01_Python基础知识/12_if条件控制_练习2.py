import random

your = int(input("请出拳："))

# 生成随机数, 包含头尾
computer = random.randint(1,3)

# 石头（1）／剪刀（2）／布（3）
if (your == 3 and computer == 1) or (your == 2 and computer == 3) or (your == 1 and computer == 2):
    print("You win, my: %d com: %d" % (your, computer))
elif your == computer:
    print("Tie 平局!")
else:
    print("Computer win, my: %d com: %d" % (your, computer))