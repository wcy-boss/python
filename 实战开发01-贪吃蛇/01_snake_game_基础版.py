"""
创建贪吃蛇游戏窗口 640x480 px
绘制 绿色的蛇🐍，红色苹果🍎 20 px
让蛇运动起来
根据方向键修改朝向

判定碰撞
1. 碰到苹果，吃掉苹果，长身体
2. 碰到墙体，挂了，弹分数框
3. 碰到自己，挂了，弹分数框

基于PyQt5实现
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# 创建窗口
class SnakeGame(QMainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        # 设置窗口标题和大小
        self.setWindowTitle("贪吃蛇游戏v1.0")
        self.resize(640, 480)
        # 创建画画板 QFrame
        self.frame = GameFrame(self)
        # 设置到当前窗口里
        self.setCentralWidget(self.frame)

class GameFrame(QFrame):
    
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        print("init")

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建窗口
    game = SnakeGame()
    game.show()
    # 让主程序阻塞运行
    sys.exit(app.exec_())
    
