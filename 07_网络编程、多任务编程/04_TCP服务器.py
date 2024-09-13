"""
1. socket创建一个套接字
2. bind绑定ip和port
3. listen使套接字设置为被动模式
4. accept等待客户端的链接
5. recv/send接收发送数据
"""
import socket
# 1. socket创建一个TCP套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(tcp_server_socket)

# 2. bind绑定ip和port
# 如果ip是空字符串，代表所有本机网卡的ip地址
# tcp_server_socket.bind(("", 7788))
tcp_server_socket.bind(("127.0.0.1", 7788))

# 3. listen使套接字设置为被动模式
# 参数：等待客户端的链接的最大数量，只在Windows里生效，其他系统不限制
# 此时，socket套接字对象由主动连接模式变为被动模式, 等待客户端接入
tcp_server_socket.listen(128)

print("服务器已开启，等待客户端接入！")
# 4. accept等待客户端的链接(阻塞当前线程，有新客户端接入时才释放阻塞)
tcp_client, client_addr = tcp_server_socket.accept()
print("有新的客户端来了：", client_addr)

# 5. recv/send接收发送数据(会一直阻塞等待)
client_data = tcp_client.recv(1024)
print("收到来自客户端的数据：", client_data.decode("GBK"))

# 服务器回复数据
tcp_client.send("消息已收到！".encode("utf-8"))

# 6. 关闭服务器
tcp_server_socket.close()