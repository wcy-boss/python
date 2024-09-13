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
tcp_client_socket.connect(("127.0.0.1", 7788))

# 4. 开始发送数据（到服务端）
tcp_client_socket.send("哈哈哈，你打不过我吧！".encode(encoding="utf-8"))  # 发送端编码要和接收端一致

# 5. 接收数据,等待服务器回复消息
print("等待接收消息！")
# 代码在这里会阻塞，直到服务器回复消息了，自动释放阻塞
# 参数：bufsize，设置缓冲区大小1024字节，一次性最多接收的字节
recv_data = tcp_client_socket.recv(1024)

print("收到服务器返回：", recv_data.decode(encoding="GBK"))

# 6. 关闭套接字
tcp_client_socket.close()