"""
输入文件的名字，然后程序自动完成对文件进行备份

分析:
1.输入文件名 b.py
2.创建文件  文件名[复制].py
3.读取文件, 写入到复制的文件中
"""
import os

while True:
    file_name = input("请输入要备份的文件名:")
    # 首先判断文件是否存在，存在，则结束循环
    if os.path.exists(file_name):
        break
    
    # 文件不存在
    print("文件不存在：", file_name)
    
print("开始拷贝：", file_name) # good.haha.txt -> haha[复制].txt
# 创建新的文件名
# 获取点的位置
dot_index = file_name.rfind(".")
# 1. 取出文件名 haha
filename_prefix = file_name[:dot_index]
# 2. 取出后缀名 .txt
filename_suffix = file_name[dot_index:]
# 3. 格式化到一起 haha + [复制] + .txt
new_file_name = f"{filename_prefix}[复制]{filename_suffix}"

print(new_file_name)
# 读取之前旧文件 byte / binary
with open(file_name, "rb") as f:
    content = f.read()
    print(type(content), len(content))
    # 打开新文件
    with open(new_file_name, "wb") as new_file:
        new_file.write(content)
        print("拷贝完成！")