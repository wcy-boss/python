import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 1. 创建应用程序
app = QApplication(sys.argv)

# 2. 创建窗口
w = QWidget()
w.setWindowTitle("第一个窗口")

# 3. 显示窗口
w.show()

# 4. 等待窗口停止
sys.exit(app.exec_())