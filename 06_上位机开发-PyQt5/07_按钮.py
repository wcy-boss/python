import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

def func_shoot():
    print("按钮按下啦，发射火箭！")

# ----------------------------------------------------
def init_widget(w : QWidget):
    w.setWindowTitle("按钮")
    w.resize(640, 480)
    
    btn = QPushButton("发射")
    btn.setText("发射火箭")
    
    # 给按钮添加（关联）点击事件 [pyqtSignal关联pyqtSlot槽函数]
    btn.clicked.connect(func_shoot)
    
    btn.setParent(w)


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

