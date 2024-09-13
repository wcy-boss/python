import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# 添加上级目录到系统路径，以便导入ui里的模块
sys.path.append("../")

from ui.Ui_serial_setting_dialog import Ui_SerialSettingDialog

class SerialSettingDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SerialSettingDialog()
        self.ui.setupUi(self)

        # 可以通过此设置，固定对话框的大小
        self.setFixedSize(self.width(), self.height())
        
        self.initUi()

        self.baudrate = None

    def initUi(self):
        pass

    def accept(self):
        super().accept()
        print("accept")
        # 读取当前波特率的设置值
        self.baudrate = self.ui.cb_baudrate.currentText()
        print(self.baudrate)

    def reject(self):
        super().reject()
        print("reject")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = SerialSettingDialog()
    dialog.show()
    sys.exit(app.exec_())