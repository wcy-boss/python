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
import random
import sys
import time
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent, QPaintEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

COLOR_BLACK = QColor(0, 0, 0)
COLOR_RED = QColor(255, 0, 0)
COLOR_GREEN = QColor(0, 255, 0)

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
BLOCK_SIZE = 20 # 块大小
SCREEN_W = SCREEN_WIDTH // BLOCK_SIZE       # 32
SCREEN_H = SCREEN_HEIGHT // BLOCK_SIZE      # 24

DIR_UP   = ( 0, -1)
DIR_DOWN = ( 0,  1)
DIR_LEFT = (-1,  0)
DIR_RIGHT= ( 1,  0)

# 创建窗口
class SnakeGame(QMainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        # 设置窗口标题和大小
        self.setWindowTitle("贪吃蛇游戏v1.0")
        # self.resize(640, 480)
        self.setFixedSize(640, 480) # 设置固定窗口大小
        # 创建画画板 QFrame
        self.frame = GameFrame(self)
        # 设置到当前窗口里
        self.setCentralWidget(self.frame)

class GameFrame(QFrame):
    
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        # 自动获取焦点
        self.setFocusPolicy(Qt.StrongFocus)
        
        self.snake = [[5, 10], [4, 10], [3, 10]]      # [32, 24]
        self.food = self.generate_food()
        self.direction = DIR_RIGHT # 向右
        self.score = 0
        
        # 开启定时器，每个200ms刷新一次界面
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(200) # 200ms间隔执行任务
        
    def generate_food(self):
        # return [random.randint(0, 31), random.randint(0, 23)]  # [31, 23]
        while True: 
            # 随机生成食物
            food = [random.randint(0, 31), random.randint(0, 23)]  # [31, 23]
            if food not in self.snake:
                # 如果生成的食物不在蛇身上，结束循环return
                return food
        
    def update_game(self):
        # print("刷新界面:", time.time())
        # --------------------------------------- 前进
        # 1. 获取蛇头坐标
        head_x, head_y = self.snake[0]
        dir_x , dir_y = self.direction
        # 2. 往前进方向修改坐标，添加回去 
        new_head = [head_x + dir_x, head_y + dir_y]
        self.snake.insert(0, new_head)
        
        # ---------------------------------------- 碰撞检查
        # rect1.intersects(rect2)
        if new_head == self.food:
            # 吃到食物了，得分+1
            self.score += 1
            # 食物重新生成
            self.food = self.generate_food()
        else:
            # 3. 删除蛇尾
            self.snake.pop()
            
        # 触发界面刷新操作
        self.update()

    def keyPressEvent(self, event: QKeyEvent):
        # print(event.key()) # 上下左右 
        if event.key() == Qt.Key_Up and self.direction != DIR_DOWN:
            # print("向上")
            self.direction = DIR_UP
        elif event.key() == Qt.Key_Down and self.direction != DIR_UP:
            # print("向下")
            self.direction = DIR_DOWN
        elif event.key() == Qt.Key_Left and self.direction != DIR_RIGHT:
            # print("向左")
            self.direction = DIR_LEFT
        elif event.key() == Qt.Key_Right and self.direction != DIR_LEFT:
            # print("向右")
            self.direction = DIR_RIGHT
            
    def paintEvent(self, event: QPaintEvent):
        # return super().paintEvent(event)
        # 绘制自己想要的内容
        # 创建画笔
        painter = QPainter(self)
        # 绘制背景
        painter.setBrush(QBrush(COLOR_BLACK)) # Red, Green, Blue
        painter.drawRect(self.rect())
        # 绘制食物
        painter.setBrush(QBrush(COLOR_RED)) # Red, Green, Blue
        painter.drawRect(self.food[0] * BLOCK_SIZE, self.food[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        # 绘制蛇
        painter.setBrush(QBrush(COLOR_GREEN)) # Red, Green, Blue
        painter.setPen(COLOR_GREEN)
        for x, y in self.snake:
            painter.drawRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建窗口
    game = SnakeGame()
    game.show()
    # 让主程序阻塞运行
    sys.exit(app.exec_())
    
