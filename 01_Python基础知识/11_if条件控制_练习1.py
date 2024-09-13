your = int(input("请出拳："))

computer = 1 # 石头

if your == 3 and computer == 1:
    print("You win!")
elif your == 2 and computer == 1:
    print("Computer Win")
else:
    print("Tie 平局!")