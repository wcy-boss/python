import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QTextEdit

# ----------------------------------------------------
def init_widget(w : QWidget):
    w.setWindowTitle("输入框")
    w.resize(640, 480)
    
    # 创建垂直布局的容器 QVBoxLayout
    # Vertical Box Layout
    layout = QVBoxLayout()
    username_edit = QLineEdit()
    # 设置输入框提示
    username_edit.setPlaceholderText("输入姓名")
    # 自动填充内容
    username_edit.setText("PoplarTang")
    # 限制用户名输入的长度12字符
    username_edit.setMaxLength(12)
    # 将输入框添加到layout里
    layout.addWidget(username_edit)
    
    # 创建多行输入框
    text_edit = QTextEdit()
    # 设置提示内容
    text_edit.setPlaceholderText("请输入个人简介")
    # 设置默认内容
    # text_edit.setText("<font color='red'>abc</font>") # 支持富文本 （HTML+CSS标签语言）
    # text_edit.setText("<strong>abc</strong>") # 支持富文本
    # 设置默认文本内容
    text_edit.setPlainText("<font color='red'>abc</font>") # 普通文本
    # 获取用户输入的内容
    print(text_edit.toPlainText())
    text_edit.clear()
    
    # 将输入框添加到layout里
    layout.addWidget(text_edit)
    
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

