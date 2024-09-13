string = "Hello"
print(string[1])

print("-------------------------- 判断")
print("abCDef".isalpha())   # 判断是否全是字母
print("12345".isdecimal())  # 判断全是数字
# print("12345①②".isdigit())    # 判断全是数字
# print("12345一二三ⅠⅡⅢ①②贰".isnumeric())  # 判断全是数字（所有语言）
print("pop123".startswith("po"))
print("pop123".endswith("3"))

print("-------------------------- 查找")
# print("abcdefg".index("X")) # 找不到，报异常ValueError
print("abcdefg".find("c"))    # 找不到，返回-1
print("abcdefg".find("x"))    # 找不到，返回-1
print("haha.good.mp4".rfind("."))
print("abcdefg.comcccC".replace("c", "C", 1))

print("-------------------------- 切割&合并")
print("张三葬|王大拿|孙悟空".split("|")) # 如果split不写参数，会根据空格分隔
lst = ['张三葬', '王大拿', '孙悟空']
print("-".join(lst)) # 用-合并成字符串

print("-------------------------- 其他")
print(" \t abc  \t".strip()) # 去空白
print(" abc  ".strip())
print(" abc  ".upper())