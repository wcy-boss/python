"""
1. 利用QtDesigner设计界面
2. 编译并加载.ui文件
3. 获取用户输入的IP和port
4. 创建子线程（独立任务）
    - 根据用户输入的IP和port连接服务器
    - 循环接收数据，打印
    - 要回到主线程更新显示收到的内容
5. 按下发送按钮，获取用户输入，通过Socket发送数据
    
"""

import threading
from common import utils
import socket
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# from qt_material import apply_stylesheet

from ui.Ui_main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    
    # a. 定义信号
    # 参数1: 0需要更新状态， 1收到新的消息
    # 参数2：数据
    msg_recv_signal = pyqtSignal(int, object)
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        # 加载ui内容
        self.ui.setupUi(self)
        
        # tcp客户端socket对象
        self.tcp_client: socket.socket = None
        
        # c. 将信号连接到槽
        self.msg_recv_signal.connect(self.on_data_recv_slot)
        
        self.init_ui()
    
    def update_connect_state(self):
        if self.tcp_client == None:
            # 连接网络
            self.ui.btn_connect.setIcon(QIcon(":/ic/disconnect"))
            self.ui.btn_connect.setText("连接网络")
        else:
            # 断开连接
            self.ui.btn_connect.setIcon(QIcon(":/ic/connect"))
            self.ui.btn_connect.setText("断开连接")
            
    # b. 定义槽函数
    @pyqtSlot(int, object)
    def on_data_recv_slot(self, type_t, msg):
        if type_t == 0:
            self.update_connect_state()
        elif type_t == 1:     
            thread_name = threading.current_thread().name
            print(msg, " thread->", thread_name)   
            self.ui.edit_recv.appendPlainText(msg)
            
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
        self.msg_recv_signal.emit(0, None)
        
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
                    self.msg_recv_signal.emit(1, msg)
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
        self.msg_recv_signal.emit(0, None)
        
    @pyqtSlot() # 函数的注解
    def on_btn_connect_clicked(self):
        """连接服务器
        1. 获取用户输入的ip和端口号
        2. 先创建子线程
        3. 创建socket对象并连接服务器
        4. 循环数据接收
        """
        if self.tcp_client != None:
            self.tcp_client.close()
            self.tcp_client = None
            return
        
        # 1. 获取用户输入的ip和端口号
        mode = self.ui.cb_mode.currentText()
        target_ip = self.ui.edit_target_ip.text()
        target_port = self.ui.edit_target_port.text()
        print(f"mode:{mode}, ip:{target_ip}, port:{target_port}")
        # 2. 先创建子线程，运行socket数据接收任务
        t1 = threading.Thread(
            target=self.run_tcp_client, 
            args=(target_ip, target_port), 
            daemon=True)
        t1.start()
        
    @pyqtSlot()
    def on_btn_send_clicked(self):
        """
        1. 获取用户输入的文本内容
        2. 发送数据
        """
        # print("发送")
        text = self.ui.edit_send.toPlainText()
        if len(text) == 0:
            self.statusBar().showMessage("请先输入内容，再发送！", 1000)
            return
        
        if self.tcp_client is None:
            self.statusBar().showMessage("请先连接服务器，再发送！", 1000)
            QMessageBox.warning(self, "发送失败", "请先连接服务器，再发送数据！")
            return
        
        self.tcp_client.send(text.encode())
        
        
    def init_ui(self):
        self.ui.edit_target_ip.setText("127.0.0.1")
        self.ui.edit_target_port.setText("8080")
        # self.ui.btn_connect.clicked.connect(self.on_btn_connect_clicked)
        self.ui.actionExit.triggered.connect(QApplication.quit)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


