"""
1. 导入模块socket
2. 创建socket套接字
3. 绑定IP&端口（可选）
4. 发送数据
5. 关闭套接字
"""

# 1. 导入模块socket
from socket import *
import utils
# 2. 创建socket套接字
# 参数1：地址簇，地址类型family: AddressFamily | int 
#       AF_INET     IPv4
#       AF_INET6    IPv6
# 参数2：协议类型 type: SocketKind | int
#       SOCK_STREAM     TCP协议 （默认协议）
#       SOCK_DGRAM      UDP协议
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 3. 绑定IP&端口（可选）
udp_socket.bind(("", 8888)) # 通常每个套接字地址(协议/网络地址/端口)只允许使用一次

# 4. 接收数据
# 代码会阻塞在这里，收到消息会自动释放阻塞
# 参数：缓冲区大小，最多接收1024个字节的数据
# 返回值：元组 (b'\xce\xd2\xca123abc', ('127.0.0.1', 3333))
#       元素1：字节数组类型的数据
#       元素2：发送者的ip和端口号的元组
bytes_arr, address = udp_socket.recvfrom(1024)
msg = utils.decode_data(bytes_arr)
print("收到来自【{}】的消息：{}".format(address, msg))

# 5. 关闭套接字
udp_socket.close()