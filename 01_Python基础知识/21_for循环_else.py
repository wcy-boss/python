for i in range(10):
    if i == 12:
        break
    print("媳妇，我错了！", i)
else:
    # 如果循环里没有执行到break，此函数就会执行
    print("顺利完成！1")
    
print("-------------------------------------")
    
for i in range(10):
    if i % 2 == 0:
        continue
    print("媳妇，我错了！", i)
else:
    # 如果循环里没有执行到break，此函数就会执行
    print("顺利完成！2")