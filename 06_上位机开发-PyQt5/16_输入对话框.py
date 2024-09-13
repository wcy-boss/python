import sys
import functools
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout,QLabel, QInputDialog, QFileDialog, QColorDialog

"""
让用户在对话框里输入用户名
把用户名回显到主界面
"""

user_label: QLabel = None

def on_create_clicked():
    text, confirm = QInputDialog.getText(w, "请输入", "请输入用户名")
    print(text, confirm)
    
    # 获取文件路径对话框(过滤 png或jpg文件)
    # file = QFileDialog.getOpenFileName(w, "选择文件", "", "PNG Files (*.png);;JPG Files (*.jpg)")
    # print(file)
    
    # 选择颜色对话框
    # color = QColorDialog.getColor()
    # print(color.name())
    
# ----------------------------------------------------
def init_widget(w : QWidget):
    w.setWindowTitle("布局")
    w.resize(640, 480)
    
    layout = QHBoxLayout() # Horizontal
    # 给Widget根容器设置布局方式
    w.setLayout(layout)
    
    # 通过layout布局给w添加子组件
    btn = QPushButton("创建用户")
    btn.clicked.connect(on_create_clicked)
    
    user_label = QLabel()
    
    layout.addWidget(btn)    
    layout.addWidget(user_label)    
    
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

