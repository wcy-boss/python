# 将字符串转成bytes字节数组类型, encoding表示编码字符集（默认utf-8）
bytes_arr = "你好abc123".encode(encoding="utf-8")
print(bytes_arr, type(bytes_arr))
# for byte in bytes_arr:
#     print(hex(byte))
aaa = b'\xe4\xbd\xa0\xe5\xa5\xbdabc123'

# 将bytes类型数据转成字符串类型
string = aaa.decode(encoding="UTF-8")
print(string, type(string))

print("-------------------------------------------- ")
# 将字符串转成bytes字节数组类型, encoding表示编码字符集（默认utf-8）
bytes_arr = "呀哈哈abc123".encode(encoding="GBK") # GBK一个汉字，2字节
print(bytes_arr, type(bytes_arr))
# 将bytes类型数据转成字符串类型, encoding表示编码字符集
string = bytes_arr.decode(encoding="GBK")
print(string)