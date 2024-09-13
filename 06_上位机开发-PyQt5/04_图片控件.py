import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

# ----------------------------------------------------
def init_widget(w : QWidget):
    w.setWindowTitle("图片展示")
    img_label = QLabel()
    pixmap = QPixmap("./img/img.png")
    img_label.setPixmap(pixmap)
    # 将图片显示到窗口里
    img_label.setParent(w)
    # 根据图片尺寸改变窗口大小
    w.setFixedSize(pixmap.width(), pixmap.height())


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

