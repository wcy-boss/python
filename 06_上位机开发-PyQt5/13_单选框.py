import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QRadioButton

def on_toggle_nan(arg): # 发生变化
    print("男选中：", arg)
def on_toggle_nv(arg): # 发生变化
    print("女选中：", arg)
def on_toggle_yao(arg): # 发生变化
    print("妖选中：", arg)

# ----------------------------------------------------
def init_widget(w : QWidget):
    w.setWindowTitle("布局")
    # w.resize(640, 480)
    
    layout = QHBoxLayout() # Horizontal
    # 给Widget根容器设置布局方式
    w.setLayout(layout)
    
    # 通过layout布局给w添加子组件
    btn1 = QRadioButton("男")
    btn2 = QRadioButton("女")
    btn3 = QRadioButton("妖")
    btn3.setChecked(True)
    btn1.toggled.connect(on_toggle_nan)
    btn2.toggled.connect(on_toggle_nv)
    btn3.toggled.connect(on_toggle_yao)
    
    layout.addWidget(btn1)
    layout.addWidget(btn2)
    layout.addWidget(btn3)
    
    
    


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

