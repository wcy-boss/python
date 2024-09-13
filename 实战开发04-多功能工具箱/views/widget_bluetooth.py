from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
# 帮我们直接运行此文件时，可以加载到上级目录的ui包
sys.path.append("../")

from drivers.driver_bluetooth import *
from ui.Ui_bluetooth_widget import Ui_BluetoothWidget
from common.qt_worker import Worker

class BluetoothWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_BluetoothWidget()
        self.ui.setupUi(self)
        
        self.current_bdt : BluetoothDataTransfer = None
        
        self.ui.box_device.setHidden(True)

        self.init_ui()

    @pyqtSlot(object)
    def scan_devices_result(self, devices):
        thread_name = QThread.currentThread()
        print("扫描完成，共找到{}个设备, 线程：{}".format(len(devices), thread_name))
        # 清理已有设备
        self.ui.cb_devices.clear()
        for device in devices:
            # print(device)
            self.ui.cb_devices.addItem(device[1], userData=device[0])
            
        # 显示隐藏
            
        # 展开下拉框
        self.ui.cb_devices.showPopup()

    # 扫描按钮
    @pyqtSlot()
    def on_btn_refresh_clicked(self):
        print("Scanning devices...")
        worker = Worker(target=BluetoothDataTransfer.scan_devices)
        worker.signal_connect(result_handler=self.scan_devices_result)
        worker.start()
        # devices = BluetoothDataTransfer.scan_devices()
        # for device in devices:
        #     print(device)

    # 连接按钮
    @pyqtSlot()
    def on_btn_connect_clicked(self):
        if self.current_bdt is not None:
            # 断开连接
            self.current_bdt.disconnect()
            # 隐藏设备信息
            self.ui.box_device.setHidden(True)
            # 按钮和图标
            self.ui.btn_connect.setText("连接蓝牙")
            self.ui.label_connect_state.setPixmap(QPixmap(":/ic/disconnect"))
            self.current_bdt = None
            return
        
        address = self.ui.cb_devices.currentData()
        if address is None:
            print("No device selected.")
            return
        
        name = self.ui.cb_devices.currentText()
        print("Connecting to {} ({})...".format(name, address))
        bdt = BluetoothDataTransfer(address, name)
        if bdt.connect():
            self.current_bdt = bdt
            self.ui.box_device.setHidden(False)
            # 将设备的名称和地址显示在界面上
            self.ui.label_name.setText(f"名称：{name}")
            self.ui.label_addr.setText(f"地址：{address}")
            # 按钮和图标
            self.ui.btn_connect.setText("断开蓝牙")
            self.ui.label_connect_state.setPixmap(QPixmap(":/ic/connect"))
        else:
            print("Failed to connect.")

    def init_ui(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = BluetoothWidget()
    window.show()

    sys.exit(app.exec_())