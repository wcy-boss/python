import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from qt_material import apply_stylesheet

from ui.Ui_my_main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        # 加载ui内容
        self.ui.setupUi(self)
        
        self.init_ui()
        
    def on_dial_update(self, value: int):
        print("value: ", value)
        # self.ui.horizontalSlider.setValue(value)
        
    def init_ui(self):
        self.ui.dial.valueChanged.connect(self.on_dial_update)
        
        # 给actionExit添加退出功能实现
        self.ui.actionExit.triggered.connect(self.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    # setup stylesheet
    # apply_stylesheet(app, theme='dark_teal.xml')
    apply_stylesheet(app, theme='dark_cyan.xml')
    window.show()
    sys.exit(app.exec_())


