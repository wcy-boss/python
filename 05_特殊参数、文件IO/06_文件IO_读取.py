# 1. 打开文件
f = open("shi.txt", encoding="utf-8")  # 设置字符集 
# 需要保证打开文件时，使用的字符集和文件本身的字符集一致，即可避免乱码问题
# 2. 读写文件
content = f.read() # UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 10: illegal multibyte sequence
print(content)

# 3. 关闭文件
f.close()
