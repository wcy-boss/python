"""
1. 编写一个TCP服务端程序，循环等待接受客户端的连接请求
2. 当客户端和服务端建立连接成功，创建子线程，使用子线程专门处理客户端的请求，防止主线程阻塞
3. 把创建的子线程设置成为守护线程，避免主线程结束时，子线程还在运行。
"""

# 导入socket依赖
import socket
import sys
import threading
from utils import decode_data

def handle_new_client(tcp_client: socket.socket, tcp_client_addr: tuple):
    thread_name = threading.current_thread().name
    tcp_client.send(f"欢迎光临：{thread_name}!".encode())
    
    while True:
        recv_data = tcp_client.recv(1024)
        if recv_data:
            msg = decode_data(recv_data)
            print(f"收到来自 {tcp_client_addr} 的消息：{msg}")
            tcp_client.send("消息已收到！".encode())
        else:
            print("客户端已断开：", tcp_client_addr)
            break
        
    tcp_client.close()

def main():
    # 可以根据用户参数，设置服务器端口
    args = sys.argv[1:]

    # 创建TCP服务器socket
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定服务器ip和port
    port = 8888
    # print("port: ", port)
    tcp_server.bind(("", port))

    # 设置为被动模式，监听客户端的接入
    tcp_server.listen(128)
    
    index = 0

    print(f"服务器已启动，端口：{port}")
    while True:
        # 循环等待接受客户端的连接请求
        tcp_client, tcp_client_addr = tcp_server.accept()
        print(f"有新的客户端 {tcp_client_addr} 接入！")
        
        t1 = threading.Thread(
            target=handle_new_client,
            name=f"红浪漫VIP: {index}",
            args=(tcp_client, tcp_client_addr),
            daemon=True
        )
        t1.start()
        index += 1
            
    tcp_server.close()
    
if __name__ == '__main__':
    main()
