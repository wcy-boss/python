import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLineEdit

edit_name: QLineEdit = None
edit_age: QLineEdit = None
edit_phone: QLineEdit = None

def on_submit():
    print("提交")
    print("姓名：", edit_name.text())
    print("年纪：", edit_age.text())
    print("电话：", edit_phone.text())

# ----------------------------------------------------
def init_widget(w : QWidget):
    w.setWindowTitle("布局")
    w.resize(640, 480)
    
    # 创建布局
    layout = QFormLayout(w)
    
    global edit_name, edit_age, edit_phone
    
    edit_name = QLineEdit()
    edit_age = QLineEdit()
    edit_phone = QLineEdit()
    layout.addRow("姓名：", edit_name)
    layout.addRow("年纪：", edit_age)
    layout.addRow("电话：", edit_phone)
    btn_submit = QPushButton("提交")
    btn_submit.clicked.connect(on_submit)
    layout.addRow(btn_submit)


if __name__ == '__main__':
    # 1. 创建应用程序
    app = QApplication(sys.argv)
    # 2. 创建窗口
    w = QWidget()
    
    w.setWindowTitle("布局")
    w.resize(640, 480)
    
    # 创建布局
    layout = QFormLayout(w)
    
    edit_name = QLineEdit()
    edit_age = QLineEdit()
    edit_phone = QLineEdit()
    layout.addRow("姓名：", edit_name)
    layout.addRow("年纪：", edit_age)
    layout.addRow("电话：", edit_phone)
    btn_submit = QPushButton("提交")
    btn_submit.clicked.connect(on_submit)
    layout.addRow(btn_submit)
    
    # 3. 显示窗口
    w.show()
    # 4. 等待窗口停止
    sys.exit(app.exec_())

