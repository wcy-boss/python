# 1. 打开文件
f = open("shi.txt", encoding="utf-8")  # 设置字符集 
# 2. 读写文件
content = f.read(5) # 5个字符
print(content)

line = f.readline() # 读取一行, 读到\n结束
print(line)

line = f.readline(3) # 读取一行指定个字节, 读到\n结束
print(line)

lines = f.readlines()
print(lines)
# 3. 关闭文件
f.close()
