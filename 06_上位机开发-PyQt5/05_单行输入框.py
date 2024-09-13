import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout

# ----------------------------------------------------
def init_widget(w : QWidget):
    w.setWindowTitle("输入框")
    w.resize(640, 480)
    
    # 创建垂直布局的容器 QVBoxLayout
    # Vertical Box Layout
    layout = QVBoxLayout()
    username_edit = QLineEdit()
    # 设置输入框提示
    username_edit.setPlaceholderText("请输入用户名")
    # 自动填充内容
    username_edit.setText("PoplarTang")
    # 限制用户名输入的长度12字符
    username_edit.setMaxLength(12)
    # 将输入框添加到layout里
    layout.addWidget(username_edit)
    
    pwd_edit = QLineEdit()
    # 设置输入框提示
    pwd_edit.setPlaceholderText("请输入密码")
    # 自动填充内容
    pwd_edit.setText("123456")
    # 设置回显模式echo
    pwd_edit.setEchoMode(QLineEdit.Password)
    # 将输入框添加到layout里
    layout.addWidget(pwd_edit)
    
    w.setLayout(layout)


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

