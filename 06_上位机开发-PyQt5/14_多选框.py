import sys
import functools
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QCheckBox, QButtonGroup,QLabel

def on_state_changed(index, arg):
    print(f"btn: {index}", end=" ")
    
    if arg == Qt.Checked:
        print("选中")
    else :
        print("取消")
        
        
# def on_state_changed(arg):
    
#     if arg == Qt.Checked:
#         print("选中")
#     else :
#         print("取消")


# ----------------------------------------------------
def init_widget(w : QWidget):
    w.setWindowTitle("布局")
    # w.resize(640, 480)
    
    layout = QHBoxLayout() # Horizontal
    # 给Widget根容器设置布局方式
    w.setLayout(layout)
    
    # 通过layout布局给w添加子组件
    btn1 = QCheckBox("抽烟")
    btn2 = QCheckBox("喝酒")
    btn3 = QCheckBox("烫头")
    btn3.setChecked(True)
    
    # 监听实时的状态变化， 以下两种写法作用一致
    btn1.stateChanged.connect(lambda arg: on_state_changed(1, arg))
    btn2.stateChanged.connect(functools.partial(on_state_changed, 2))
    
    btn3.stateChanged.connect(lambda arg: print("按钮3：", arg))
    
    # btn1.stateChanged.connect(on_state_changed)
    # btn2.stateChanged.connect(on_state_changed)
    # btn3.stateChanged.connect(on_state_changed)
    
    layout.addWidget(QLabel("谦哥的三大爱好："))    
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

