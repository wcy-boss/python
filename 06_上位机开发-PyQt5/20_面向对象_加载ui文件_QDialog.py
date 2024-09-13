import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from ui.Ui_my_dialog import Ui_Dialog

class MyDialog(QDialog):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        # 加载ui内容
        self.ui.setupUi(self)
        
        self.init_ui()
        
    def init_ui(self):
        pass

    def accept(self):
        super().accept()
        print("accept 接受")
        # 读取当前波特率的设置值

    def reject(self):
        super().reject()
        print("reject 拒绝")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyDialog()
    window.show()
    sys.exit(app.exec_())


