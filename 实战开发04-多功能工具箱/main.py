from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
# 帮我们直接运行此文件时，可以加载到上级目录的ui包
# sys.path.append("../")

from ui.Ui_main_window import Ui_MainWindow
from views.widget_upper_car import UpperCarWidget
from views.widget_serial_assistant import SerialAssistantWidget
from views.widget_bluetooth import BluetoothWidget
from views.widget_net_assistant import NetAssistantWidget
    
class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始化ui相关组件
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_ui()

    def init_ui(self):
        self.ui.tabWidget.addTab(NetAssistantWidget(self), "网络助手")
        self.ui.tabWidget.addTab(BluetoothWidget(self), "蓝牙助手")
        self.ui.tabWidget.addTab(SerialAssistantWidget(self), "串口助手")
        self.ui.tabWidget.addTab(UpperCarWidget(self), "小车上位机")
        self.ui.tabWidget.addTab(QWidget(self), "物联网平台")
        self.ui.tabWidget.addTab(QWidget(self), "其他")
        # 选中最后一个标签
        self.ui.tabWidget.setCurrentIndex(3)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())