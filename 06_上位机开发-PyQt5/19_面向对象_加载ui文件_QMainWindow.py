import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from ui.Ui_my_mainwindow import Ui_MainWindow
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
    
class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        # 加载ui内容
        self.ui.setupUi(self)
        
        self.init_ui()
        
    def on_btn_clicked(self):
        self.ui.label.setText("你好")
        self.statusBar().showMessage("Hello")
        
        dialog = MyDialog()
        rst = dialog.exec_() # 阻塞式地弹窗
        
        print("rst: ", rst)
        
    def init_ui(self):
        self.ui.pushButton.clicked.connect(self.on_btn_clicked)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


