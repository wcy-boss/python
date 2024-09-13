

import socket
import threading
from common import utils

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class NetDriver(QObject):
    """
    1. 连接服务器功能 connect_server
    2. 数据循环接收功能 
    3. 数据发送功能 send, send_msg
    """
    
    # a. 定义信号
    # 参数1: 0需要更新状态， 1收到新的消息
    # 参数2：数据
    net_msg_signal = pyqtSignal(int, object)
    
    def __init__(self) -> None:
        super().__init__()
        # tcp客户端socket对象
        self.tcp_client: socket.socket = None
    
    def is_connected(self):
        """
        返回是否连接
        """
        return self.tcp_client is not None
    
    def send(self, bytes_data):
        if self.tcp_client is None:
            return
        self.tcp_client.send(bytes_data)
    
    def send_msg(self, text):
        if self.tcp_client is None:
            return
        self.tcp_client.send(text.encode())
    
    def disconnect(self):
        self.tcp_client.close()
        self.tcp_client = None
    
    def run_tcp_client(self, target_ip, target_port):
        # 创建socket对象并连接服务器
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 连接服务器
        try:
            self.tcp_client.connect((target_ip, int(target_port))) # ConnectionRefusedError: [WinError 10061] 由于目标计算机积极拒绝，无法连接。
        except Exception as e:
            print("连接服务器失败，请重试！")
            self.tcp_client = None
            return
        
        # 通知主线程，更新UI状态
        self.net_msg_signal.emit(0, None)
        
        local_ip, local_port = self.tcp_client.getsockname()
        print(f"服务器连接成功, 本机信息ip:{local_ip} port:{local_port}")
        
        try:
            while True:
                # 阻塞接收消息  
                bytes_data = self.tcp_client.recv(1024) # ConnectionAbortedError
                if bytes_data:
                    msg = utils.decode_data(bytes_data)
                    print("收到数据：", msg)
                    # self.on_data_recv_slot(msg)
                    # 通过信号和槽机制，将消息发到主线程执行
                    self.net_msg_signal.emit(1, msg)
                    # 子线程不能直接操作主线程UI组件，会出现争抢问题
                    # self.ui.edit_recv.appendPlainText(msg)
                else:
                    print("服务器已断开！")
                    break
        except:
            print("已断开连接！")
        
        if self.tcp_client is not None:
            self.tcp_client.close()
            self.tcp_client = None
            
        # 通知主线程，更新UI状态
        self.net_msg_signal.emit(0, None)
        
    def connect_server(self, target_ip, target_port):
        t1 = threading.Thread(
            target=self.run_tcp_client, 
            args=(target_ip, target_port), 
            daemon=True)
        t1.start()