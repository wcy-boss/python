from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
# 帮我们直接运行此文件时，可以加载到上级目录的ui包
sys.path.append("../")
# print(sys.path)

from ui.Ui_upper_car_widget import Ui_UpperCarWidget
from drivers.driver_serial import *
from common.utils import *

class UpperCarWidget(QWidget):

    def __init__(self, parent : QMainWindow=None):
        super().__init__(parent)
        self.root_parent = parent
        self.ui = Ui_UpperCarWidget()
        self.ui.setupUi(self)
        
        self.current_serial_device: SerialDevice = None

        self.init_ui()
        
    def __show_status(self, msg, msecs = 0):
        if self.root_parent is None:
            print("parent is none")
            return
        
        if not isinstance(self.root_parent, QMainWindow):
            # 如果不是QMainWindow，返回
            print("parent is not QMainWindow: ", type(self.root_parent))
            
            return
        
        self.root_parent.statusBar().showMessage(msg, msecs)
        
    @pyqtSlot()
    def on_btn_refresh_clicked(self):
        self.refresh_devices()
        
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
            self.ui.btn_connect.setText("连接🔗")
            return
        
        # 1. 获取当前选中设备
        current_device = self.ui.cb_devices.currentData()
        # 2. 获取设置的波特率数据
        current_bandrate = int(self.ui.cb_bandrate.currentText())
        
        if current_device is None:
            print("先选择设备，再连接")
            self.__show_status("请先选择设备，再点连接！", 3000)
            return
        
        # 3. 连接设备
        print("连接设备：{} 波特率：{}".format(current_device, current_bandrate))
        sd = SerialDevice(current_device, baud_rate=current_bandrate, timeout=1)  # 替换为您的串口名称、波特率和超时时间
        success, msg = sd.open()
        if success:
            print(f"串口设备已打开：{current_device}")
            self.__show_status(f"串口已打开：{current_device}")
            # 更新按钮文字
            self.ui.btn_connect.setText("断开🔌")
            
            # 把串口设备设置为全局变量
            self.current_serial_device = sd
            
        else:
            print(f"串口设备打开失败：{current_device}")
            self.__show_status(f"串口设备打开失败：{current_device} -> {msg}")

    @pyqtSlot()
    def on_btn_light_clicked(self):            
        print('点灯')
        self.send_bytes(b'\x01')

    def send_bytes(self, data):
        if self.current_serial_device is None:
            print("请先连接设备！")
            self.__show_status("请先连接设备！", 3000)
            QMessageBox.warning(self, "提示", "请先连接设备！", QMessageBox.Ok)
            return
        
        # 发送指令
        # self.current_serial_device.write([0x01])
        self.current_serial_device.write(data)
        # 状态栏
        self.__show_status("已发送指令！：{}".format(hex2str(data)), 2000)

    @pyqtSlot()
    def on_btn_forward_clicked(self):
        print('前进')      
        self.send_bytes(b'\x10')
        
    @pyqtSlot()
    def on_btn_stop_clicked(self):
        print('停止')
        self.send_bytes(b'\x19')    

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

    @pyqtSlot(int)
    def on_slider_forward_speed_valueChanged(self, value: int):
        print("前进速度：", value)
        byte_arr = bytearray([0x13, value]) # [0, 100]
        self.send_bytes(byte_arr)    

    def init_ui(self):
        # self.ui.slider_forward_speed.valueChanged['int'].connect(self.on_slider_forward_speed_changed)
        self.refresh_devices()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UpperCarWidget()
    window.show()
    sys.exit(app.exec_())