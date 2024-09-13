import threading
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
# 帮我们直接运行此文件时，可以加载到上级目录的ui包
sys.path.append("../")

from drivers.driver_serial import *

from ui.Ui_serial_assistant_widget import Ui_SerialAssistantWidget
from views.dialog_serial_setting import SerialSettingDialog

class SerialAssistantWidget(QWidget):
    
    # a. 定义信号
    msg_update_signal = pyqtSignal(str)

    def __init__(self, parent = None):
        super().__init__(parent)
        self.root_parent = parent
        self.ui = Ui_SerialAssistantWidget()
        self.ui.setupUi(self)
        
        # c. 信号与槽函数关联
        self.msg_update_signal.connect(self.update_recv_text)

        self.current_serial_device: SerialDevice = None
        
        self.init_ui()

    def __show_status(self, msg, msecs = 0):
        if self.root_parent is None:
            return
        
        if not isinstance(self.root_parent, QMainWindow):
            # 如果不是QMainWindow，返回
            # print("parent is not QMainWindow: ", type(self.root_parent))
            return
        
        self.root_parent.statusBar().showMessage(msg, msecs)

    # b. 定义槽函数
    @pyqtSlot(str)
    def update_recv_text(self, msg):
        self.ui.edit_recv.appendPlainText(msg)

    def recv_thread(self, sd):
        """接收数据线程"""
        try:
            while True:
                if sd is None:
                    break
                data = sd.readline()
                if data is not None:
                    print("接收到数据：", data)
                    # self.ui.edit_recv.appendPlainText(data.decode())
                    # d. 发送信号
                    self.msg_update_signal.emit(data.decode())
                else:
                    print("接收到数据为空！")
                    break
        except Exception as e:
            print("接收线程异常退出：", e)
            

    @pyqtSlot()
    def on_btn_connect_clicked(self):
        """连接设备
        先判断当前是否有已连接的设备，如有，则先断开再连接；
        
        1. 获取当前选中设备
        2. 获取设置的波特率数据
        3. 连接设备
        """
        if self.current_serial_device is not None:
            self.current_serial_device.close()
            # 状态栏
            self.__show_status("已断开设备！【{}】".format(self.current_serial_device.port))
            self.current_serial_device = None
            self.ui.btn_connect.setText("连接设备")
            # 修改图标为 disconnect
            self.ui.label_state.setPixmap(QPixmap(":/ic/disconnect"))
            return
        
        # 1. 获取当前选中设备
        current_device = self.ui.cb_devices.currentData()
        # 2. 获取设置的波特率数据
        current_baudrate = int(self.ui.cb_baudrate.currentText())
        
        if current_device is None:
            print("先选择设备，再连接")
            self.__show_status("请先选择设备，再点连接！", 3000)
            return
        
        # 3. 连接设备
        print("连接设备：{} 波特率：{}".format(current_device, current_baudrate))
        sd = SerialDevice(current_device, 
                          baud_rate=current_baudrate, 
                          timeout=None)  # 替换为您的串口名称、波特率和超时时间
        success, msg = sd.open()
        if success:
            print(f"串口设备已打开：{current_device}")
            self.__show_status(f"串口已打开：{current_device}")
            # 更新按钮文字
            self.ui.btn_connect.setText("断开设备")
            # 修改图标为 connect
            self.ui.label_state.setPixmap(QPixmap(":/ic/connect"))
            # 把串口设备设置为全局变量
            self.current_serial_device = sd
            
            t1=threading.Thread(target=self.recv_thread, args=(sd,), daemon=True)
            t1.start()
            
        else:
            print(f"串口设备打开失败：{current_device}")
            self.__show_status(f"串口设备打开失败：{current_device} -> {msg}")
    
    # 清空发送事件
    @pyqtSlot()
    def on_btn_clear_send_clicked(self):
        self.ui.edit_send.clear()
    
    # 清空接收事件
    @pyqtSlot()
    def on_btn_clear_recv_clicked(self):
        self.ui.edit_recv.clear()
    
    def refresh_devices(self):
        self.ui.cb_devices.clear()
        serial_ports = scan_serial_ports()
        # 如果没有扫描到设备，提示用户
        if len(serial_ports) == 0:
            self.__show_status("扫描完成，未发现串口设备", 2000)
            return
        
        self.__show_status(f"扫描完成，发现【{len(serial_ports)}】个串口设备！")
        
        for device, description in serial_ports:
            print(device, "->", description) # COM23, /dev/ttyUSB0
            self.ui.cb_devices.addItem(description, userData = device)

    @pyqtSlot()
    def on_btn_refresh_clicked(self):
        self.refresh_devices()
        
    @pyqtSlot()
    def on_btn_send_clicked(self):
        print("发送")
        if self.current_serial_device is None:
            print("请先连接设备！")
            self.__show_status("请先连接设备！", 3000)
            QMessageBox.warning(self, "提示", "请先连接设备！", QMessageBox.Ok)
            return
        
        # 发送指令
        text = self.ui.edit_send.toPlainText()
        # 判定文本是否为空
        if text.strip() == "":
            print("发送内容为空！")
            self.__show_status("发送内容为空！", 2000)
            return
        
        # 发送数据
        self.current_serial_device.write(f"{text}\n".encode())
        
    @pyqtSlot()
    def on_btn_setting_clicked(self):
        print("设置")
        dialog = SerialSettingDialog(self)
        # dialog.show() # 不会阻塞父窗体
        rst = dialog.exec_() # 会阻塞父窗体
        print(f"rst:{rst}")
        if rst == QDialog.Accepted:
            print("设置成功:" , dialog.baudrate)
    
    def init_ui(self):
        self.refresh_devices()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = SerialAssistantWidget()
    window.show()

    sys.exit(app.exec_())