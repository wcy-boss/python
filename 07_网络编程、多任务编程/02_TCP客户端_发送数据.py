"""
1. 导入socket模块
2. 创建socket套接字
3. 建立tcp连接（和服务端建立连接）
4. 开始发送数据（到服务端）
5. 关闭套接字
"""
# 1. 导入socket模块
import socket

# 2. 创建socket套接字
# 参数1：地址簇，地址类型family: AddressFamily | int 
#       AF_INET     IPv4
#       AF_INET6    IPv6
# 参数2：协议类型 type: SocketKind | int
#       SOCK_STREAM     TCP协议
#       SOCK_DGRAM      UDP协议
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. 建立tcp连接（和服务端建立连接）
# 参数("127.0.0.1", 8080)是服务器("ip", port)的元组
tcp_client_socket.connect(("127.0.0.1", 8080))

# 4. 开始发送数据（到服务端）
# tcp_client_socket.send("Hello".encode()) # 不能直接发字符串，要发字节数组
tcp_client_socket.send("hello中国123".encode(encoding="utf-8"))  # 发送端编码要和接收端一致
# tcp_client_socket.send("hello默认编码".encode())  # 发送端编码要和接收端一致
# tcp_client_socket.send("hello，你好我是GBK编码".encode(encoding="gbk"))  # 发送端编码要和接收端一致

# 5. 关闭套接字
tcp_client_socket.close()