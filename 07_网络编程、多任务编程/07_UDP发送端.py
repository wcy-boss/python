"""
1. 导入模块socket
2. 创建socket套接字
3. 绑定IP&端口（可选）
4. 发送数据
5. 关闭套接字
"""

# 1. 导入模块socket
from socket import *

# 2. 创建socket套接字
# 参数1：地址簇，地址类型family: AddressFamily | int 
#       AF_INET     IPv4
#       AF_INET6    IPv6
# 参数2：协议类型 type: SocketKind | int
#       SOCK_STREAM     TCP协议 （默认协议）
#       SOCK_DGRAM      UDP协议
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 3. 绑定IP&端口（可选）
udp_socket.bind(("", 3333)) # 通常每个套接字地址(协议/网络地址/端口)只允许使用一次

# 4. 发送数据
data = "你好，陌生人".encode("UTF-8")
address = ("127.0.0.1", 8888) # 元组类型(ip, port)
udp_socket.sendto(data, address)

# 5. 关闭套接字
udp_socket.close()