import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from ui.Ui_my_widget import Ui_MyWidget

class MyWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MyWidget()
        self.ui.setupUi(self)
        
        self.init_ui()
        
        
    def on_btn_clicked(self):
        print("按钮点击!")
        
    def init_ui(self):
        self.ui.btn_submit.clicked.connect(self.on_btn_clicked)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())


