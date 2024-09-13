import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

# ----------------------------------------------------
def init_widget(w : QWidget):
    w.setWindowTitle("布局")
    w.resize(640, 480)
    
    layout = QHBoxLayout() # Horizontal
    # 给Widget根容器设置布局方式
    w.setLayout(layout)
    
    # 通过layout布局给w添加子组件
    layout.addWidget(QPushButton("1"))
    layout.addWidget(QPushButton("2"))
    layout.addWidget(QPushButton("3"))
    layout.addWidget(QPushButton("4"))
    layout.addWidget(QPushButton("5"))
    


if __name__ == '__main__':
    # 1. 创建应用程序
    app = QApplication(sys.argv)
    # 2. 创建窗口
    w = QWidget()
    init_widget(w)
    # 3. 显示窗口
    w.show()
    # 4. 等待窗口停止
    sys.exit(app.exec_())

