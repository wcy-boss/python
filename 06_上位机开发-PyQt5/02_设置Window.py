from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys

# 1. 创建应用程序
app = QApplication(sys.argv)

# 2. 创建窗口
w = QWidget()

# 设置窗口标题
w.setWindowTitle("黑马窗口")
# 设置窗口大小
w.resize(640, 480)
# w.setFixedSize(1366, 768)
# w.setGeometry(100, 200, 640, 480)

# 设置窗口图标
icon = QIcon("./img/qq.png")
w.setWindowIcon(icon)

# 气泡提示
w.setToolTip("鼠标悬浮气泡提示🤣")

# 3. 显示窗口
w.show()

# 4. 执行并等待
sys.exit(app.exec_())