import sys
import functools
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QCheckBox, QButtonGroup,QLabel, QMessageBox

def on_delete_clicked():
    result = QMessageBox.question(w, "删除提示", "确认要删除xxx吗？",
                buttons = QMessageBox.Ok | QMessageBox.Cancel,
                defaultButton = QMessageBox.Cancel)

    if result == QMessageBox.Ok:
        print("确认删除")
    else:
        print("取消")
# ----------------------------------------------------
def init_widget(w : QWidget):
    w.setWindowTitle("布局")
    w.resize(640, 480)
    
    layout = QHBoxLayout() # Horizontal
    # 给Widget根容器设置布局方式
    w.setLayout(layout)
    
    # 通过layout布局给w添加子组件
    btn = QPushButton("删除用户")
    btn.clicked.connect(on_delete_clicked)
    layout.addWidget(btn)    
    
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

