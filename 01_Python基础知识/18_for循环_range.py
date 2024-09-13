print(list(range(10)))   # [0, 10) stop
print(list(range(2, 7))) # [2, 7) start, stop

for i in range(10):     # 0, stop
    print(i, end=" ")
print()

# i += 1
# 5 6 7 8 9
for i in range(5, 10):  # start, stop
    print(i, end=" ")
print()

# i += 2
# 5 7 9
for i in range(5, 10, 2): # start, stop, step
    print(i, end=" ")
print()

# i += -1
# 10, 9, 8, 7, 6
for i in range(10, 5, -1): # start, stop, step
    print(i, end=" ")
print()
