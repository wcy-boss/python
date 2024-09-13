"""
1. 导入模块socket
2. 创建socket套接字
3. 设置允许发送广播
4. 发送广播数据(注意广播地址)
5. 关闭套接字
"""
# 1. 导入模块socket
import socket

# 2. 创建socket套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 3. 设置允许发送广播
#       level: int      设置的影响范围， SOL_SOCKET只针对当前socket对象
#       optname: int    要设置的属性名， socket.SO_BROADCAST广播
#       value: int      要设置的属性值， True 允许广播
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

# 4. 发送广播数据(注意广播地址)
data = "来村东头王老家吃喜酒!".encode("UTF-8")
udp_socket.sendto(data, ("192.168.40.255", 8888))

# 5. 关闭套接字
udp_socket.close()