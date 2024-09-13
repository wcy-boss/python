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
from drivers.driver_net import NetDriver

class MainWindow(QMainWindow):
    
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        # 加载ui内容
        self.ui.setupUi(self)
        
        self.net_driver = NetDriver()
        # c. 将信号连接到槽
        self.net_driver.net_msg_signal.connect(self.on_data_recv_slot)
        
        self.init_ui()
    
    def update_connect_state(self):
        if not self.net_driver.is_connected():
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
            
        
    @pyqtSlot() # 函数的注解
    def on_btn_connect_clicked(self):
        """连接服务器
        1. 获取用户输入的ip和端口号
        2. 先创建子线程
        3. 创建socket对象并连接服务器
        4. 循环数据接收
        """
        if self.net_driver.is_connected():
            self.net_driver.disconnect()
            return
        
        # 1. 获取用户输入的ip和端口号
        mode = self.ui.cb_mode.currentText()
        target_ip = self.ui.edit_target_ip.text()
        target_port = self.ui.edit_target_port.text()
        print(f"mode:{mode}, ip:{target_ip}, port:{target_port}")
        # 2. 先创建子线程，运行socket数据接收任务
        self.net_driver.connect_server(target_ip, target_port)
        
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
        
        if not self.net_driver.is_connected():
            self.statusBar().showMessage("请先连接服务器，再发送！", 1000)
            QMessageBox.warning(self, "发送失败", "请先连接服务器，再发送数据！")
            return
        
        # self.tcp_client.send(text.encode())
        self.net_driver.send_msg(text)
        
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


