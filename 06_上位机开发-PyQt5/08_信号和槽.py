import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

# 槽函数
@pyqtSlot()
def func_clicked():
    print("按钮按下！")

# ----------------------------------------------------
def init_widget(w : QWidget):
    w.setWindowTitle("按钮")
    w.resize(640, 480)
    
    btn = QPushButton("发射")
    btn.setText("发射火箭")
    
    # -------------------------- 方式1：使用函数作为槽函数 ----------------------
    # 给按钮添加（关联）点击事件 [pyqtSignal关联pyqtSlot槽函数]
    btn.clicked.connect(func_clicked)
    
    # -------------------------- 方式2：使用lambda表达式作为槽函数 ----------------------
    btn.clicked.connect(lambda: print("触发！"))
    
    # -------------------------- 方式3：使用系统函数式作为槽函数 ----------------------
    btn.clicked.connect(QApplication.quit)
    
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

