import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

# ----------------------------------------------------
def init_widget(w : QWidget):
    w.setWindowTitle("布局")
    # w.resize(640, 480)
    
    layout = QHBoxLayout() # Horizontal
    # 给Widget根容器设置布局方式
    w.setLayout(layout)
    
    # 第1列
    layout.addWidget(QPushButton("1"))
    # 第2列
    layout_col2 = QVBoxLayout()
    layout_col2.addWidget(QPushButton("2"))
    layout_col2.addWidget(QPushButton("3"))
    layout.addLayout(layout_col2)
    # 第3列
    layout_col3 = QVBoxLayout()
    layout_col3.addWidget(QPushButton("4"))
    layout_col3.addWidget(QPushButton("5"))
    layout_col3.addWidget(QPushButton("6"))
    layout.addLayout(layout_col3)
    # 第4列
    layout_col4 = QVBoxLayout()
    layout_col4.addWidget(QPushButton("7"))
    layout_col4.addWidget(QPushButton("8"))
    layout_col4.addWidget(QPushButton("9"))
    layout_col4.addWidget(QPushButton("10"))
    layout.addLayout(layout_col4)
    


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

