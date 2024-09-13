import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("窗口标题")
        
        self.init_ui()
        print("init执行了")
        
    def on_btn_clicked(self):
        print("按钮点击")
        
    def init_ui(self):
        layout = QVBoxLayout(self)
    	# ---------------------------------

        # 在这里初始化界面内容
        btn = QPushButton("按钮1")
        btn.clicked.connect(self.on_btn_clicked)
        layout.addWidget(btn)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())


