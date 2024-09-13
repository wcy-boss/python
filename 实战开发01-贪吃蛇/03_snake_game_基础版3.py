"""
创建贪吃蛇游戏窗口 640x480 px      ✅
绘制 绿色的蛇🐍，红色苹果🍎 20 px ✅
让蛇运动起来            ✅
根据方向键修改朝向      ✅

判定碰撞
1. 碰到苹果，吃掉苹果，长身体 ✅
2. 碰到墙体，挂了，弹分数框   ✅
3. 碰到自己，挂了，弹分数框   ✅

基于PyQt5实现

升级版：
1. 面向对象封装
2. 替换背景图和蛇头图片（软件图标）
3. 优化食物生成逻辑
4. 游戏胜利判定逻辑
5. 实时显示分数，帧率

6. 左右穿越
"""
import random
import sys
import time
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
        self.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT) # 设置固定窗口大小
        # 创建画画板 QFrame
        self.frame = GameFrame(self)
        # 设置到当前窗口里
        self.setCentralWidget(self.frame)

class GameFrame(QFrame):
    
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        # 自动获取焦点
        self.setFocusPolicy(Qt.StrongFocus)
        
        # 游戏初始化
        self.init_game()
        
        # 开启定时器，每个200ms刷新一次界面
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(200) # 200ms间隔执行任务
        
    def init_game(self):
        self.snake = [[5, 10], [4, 10], [3, 10]]      # [32, 24]
        self.direction = DIR_RIGHT # 向右
        self.score = 0
        self.food = self.generate_food()
        
    def generate_food(self):
        # return [random.randint(0, 31), random.randint(0, 23)]  # [31, 23]
        while True: 
            # 随机生成食物
            food = [random.randint(0, SCREEN_W - 1), random.randint(0, SCREEN_H - 1)]  # [31, 23]
            if food not in self.snake:
                # 如果生成的食物不在蛇身上，结束循环return
                return food
        
    def update_game(self):
        # print("刷新界面:", time.time())
        # --------------------------------------- 前进
        # 1. 获取蛇头坐标
        head_x, head_y = self.snake[0]
        dir_x , dir_y = self.direction
        # 2. 往前进方向修改坐标，添加到0号位
        new_head = [head_x + dir_x, head_y + dir_y]
        self.snake.insert(0, new_head)
        
        # ---------------------------------------- 碰撞检查，食物碰撞
        # rect1.intersects(rect2)
        if new_head == self.food:
            # 吃到食物了，得分+1
            self.score += 1
            # 食物重新生成
            self.food = self.generate_food()
        else:
            # 3. 删除蛇尾 （没吃到食物时，需要删除）
            self.snake.pop()
            
        # ----------------------------------------- 墙体碰撞, 身体碰撞
        new_head_x, new_head_y = new_head
        if(self.snake[0] in self.snake[1:]  # 蛇头是否和身体碰撞
           or (new_head_x >= SCREEN_W or new_head_x < 0)    # 判断水平方向墙体碰撞
           or (new_head_y >= SCREEN_H or new_head_y < 0)):  # 判断竖直方向墙体碰撞
            # 弹出对话框，提示游戏结束
            print("游戏结束")
            QMessageBox.warning(self, "游戏结束", f"得分：{self.score} 关闭窗口重启游戏")
            print("重启游戏")
            self.init_game()
            return
            
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
        for x, y in self.snake:
            painter.drawRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建窗口
    game = SnakeGame()
    game.show()
    # 让主程序阻塞运行
    sys.exit(app.exec_())
    
