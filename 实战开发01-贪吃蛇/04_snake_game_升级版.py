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
1. 面向对象封装 Snake, Food
2. 替换背景图和蛇头图片（软件图标）
3. 优化食物生成逻辑
    - a. 生成地图所有格子的坐标列表
    - b. 去掉所有蛇身的坐标
    - c. 在剩余的数组里随机取一个坐标
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

COLOR_GRAY = QColor(0, 0, 0, 50)
COLOR_BLACK = QColor(0, 0, 0)
COLOR_RED = QColor(255, 0, 0)
COLOR_GREEN = QColor(0, 255, 0)
COLOR_BLUE = QColor(0, 50, 255)

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
BLOCK_SIZE = 20 # 块大小
SCREEN_W = SCREEN_WIDTH // BLOCK_SIZE       # 32
SCREEN_H = SCREEN_HEIGHT // BLOCK_SIZE      # 24

# 构建地图网格二维数组
map = []
for x in range(0, SCREEN_W):     # 0, 1, 2, 3, 4 .. 31
    for y in range(0, SCREEN_H): # 0, 1, 2, 3 .. 23
        map.append([x, y])

DIR_UP   = ( 0, -1)
DIR_DOWN = ( 0,  1)
DIR_LEFT = (-1,  0)
DIR_RIGHT= ( 1,  0)

# 创建窗口
class SnakeGame(QMainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        # 设置窗口图标
        self.setWindowIcon(QIcon("./img/icon.png"))
        # 设置窗口标题和大小
        self.setWindowTitle("贪吃蛇游戏v1.2")
        # self.resize(640, 480)
        self.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT) # 设置固定窗口大小
        # 创建画画板 QFrame
        self.frame = GameFrame(self)
        # 设置到当前窗口里
        self.setCentralWidget(self.frame)

# 蛇头运动方向字典
DIR_DICT = {
    Qt.Key_Right : (1, 0),
    Qt.Key_Left  : (-1, 0),
    Qt.Key_Up    : (0, -1),
    Qt.Key_Down  : (0, 1)
}

# 蛇头旋转方向字典
ROTATE_DICT = {
    Qt.Key_Right : -90,
    Qt.Key_Left  : 90,
    Qt.Key_Up    : 180,
    Qt.Key_Down  : 0
}
class Snake:
    
    def __init__(self):
        # self.body = [[5, 10], [4, 10], [3, 10]]      # [32, 24]
        self.body = [
            [3, 2]
        ]
        self.direction = Qt.Key_Right # 向右
        self.direction_change = None # 方向改变
        self.is_cross_enable = True
        self.score = 0
        
        self.head_img = QImage("./img/head-red.png").scaled(BLOCK_SIZE, BLOCK_SIZE)
        
        # 身体生长2格
        self.grow()
        self.grow()
        # for _ in range(43):
        #     self.grow()

    def move(self):
        if self.direction_change is not None:
            self.direction = self.direction_change
            self.direction_change = None
        
        # 1. 获取蛇头坐标
        head_x, head_y = self.body[0]
        dir_x , dir_y = DIR_DICT[self.direction]
        # 2. 往前进方向修改坐标，添加到0号位
        new_head = [head_x + dir_x, head_y + dir_y]
        
        # ------------ 穿越
        if self.is_cross_enable:
            if new_head[0] >= SCREEN_W:
                new_head[0] = 0
            elif new_head[0] < 0:
                new_head[0] = SCREEN_W - 1
            elif new_head[1] >= SCREEN_H:
                new_head[1] = 0
            elif new_head[1] < 0:
                new_head[1] = SCREEN_H - 1
        
        self.body.insert(0, new_head)
        # 3. 删除蛇尾 （没吃到食物时，需要删除）
        self.body.pop()

    def grow(self):
        # 复制一份蛇尾坐标
        tail_x, tail_y = self.body[-1]
        # 添加到尾部
        self.body.append([tail_x, tail_y])

    def handle_event(self, event: QKeyEvent):
        # print(event.key()) # 上下左右 
        if event.key() == Qt.Key_Up and self.direction != Qt.Key_Down:
            # print("向上")
            self.direction_change = Qt.Key_Up
        elif event.key() == Qt.Key_Down and self.direction != Qt.Key_Up:
            # print("向下")
            self.direction_change = Qt.Key_Down
        elif event.key() == Qt.Key_Left and self.direction != Qt.Key_Right:
            # print("向左")
            self.direction_change = Qt.Key_Left
        elif event.key() == Qt.Key_Right and self.direction != Qt.Key_Left:
            # print("向右")
            self.direction_change = Qt.Key_Right
            

    def draw(self, qp: QPainter):
        # 绘制蛇身 -------------------------------
        qp.setPen(QColor(0, 0, 0, 0)) # 边线为透明色
        qp.setBrush(COLOR_BLUE) # Red, Green, Blue
        for x, y in self.body[1:]:
            # qp.drawRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            qp.drawRoundedRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, 5, 5)

        # 绘制蛇头 -------------------------------
        head_x, head_y = self.body[0]
        # 获取当前的方向对应的旋转角度
        angle = ROTATE_DICT[self.direction]
        # 将蛇头图片进行旋转， 得到一个新图片
        rotated_img = self.head_img.transformed(QTransform().rotate(angle))
        # 绘制图片
        qp.drawImage(head_x * BLOCK_SIZE, head_y * BLOCK_SIZE, rotated_img)

class Food:
    
    def __init__(self, snake: Snake) -> None:
        self.pos = self.generate_food(snake)

    def generate_food(self, snake: Snake):
        # return [random.randint(0, 31), random.randint(0, 23)]  # [31, 23]
        # 通过推导式，得到新的temp_map，只保留蛇身以外的所有坐标
        temp_map = [node for node in map if node not in snake.body]
        
        if len(temp_map) == 0:
            return
        
        # 生成新的坐标
        node = random.choice(temp_map)
        print("food: ", node)
        return node
            
    def draw(self, qp: QPainter):
        qp.setBrush(COLOR_RED) # Red, Green, Blue
        qp.drawRect(self.pos[0] * BLOCK_SIZE, self.pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            
class GameFrame(QFrame):
    
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        # 自动获取焦点
        self.setFocusPolicy(Qt.StrongFocus)
        # 类的属性
        self.bg_img = QImage("./img/bg.png").scaled(SCREEN_WIDTH, SCREEN_HEIGHT)
        
        self.is_game_success = False
        self.is_game_over = False
        
        # 开启定时器，每个200ms刷新一次界面
        self.timer = QTimer(self)
        
        # 游戏初始化
        self.init_game()
        
        self.timer.timeout.connect(self.update_game)
        self.timer.start() # 200ms间隔执行任务
        
    def init_game(self):
        self.snake = Snake()
        self.food = Food(self.snake)
        self.timer.setInterval(200)
        
    def update_game(self):
        # 胜利判断：蛇身长度和map的大小一致
        if len(self.snake.body) >= len(map):
            # is_game_success = True
            print("游戏胜利")
            QMessageBox.information(self, "恭喜你，游戏胜利！", f"得分：{self.snake.score} 关闭窗口重启游戏")
            print("重启游戏")
            self.init_game()
            return
                    
        
        # print("刷新界面:", time.time())
        # --------------------------------------- 前进
        self.snake.move()
        
        # ---------------------------------------- 碰撞检查，食物碰撞
        head = self.snake.body[0]
        # rect1.intersects(rect2)
        if head == self.food.pos:
            # 吃到食物了，得分+1
            self.snake.score += 1
            # 蛇身生长
            self.snake.grow()
            # 食物重新生成
            self.food = Food(self.snake)
            # 根据score更新timer的帧率 (50ms间隔 = 1000ms / 20Hz)
            interval = max(50, 200 - self.snake.score * 20)
            self.timer.setInterval(interval)
            
            
        # ----------------------------------------- 墙体碰撞, 身体碰撞
        new_head_x, new_head_y = head
        if(head in self.snake.body[1:]  # 蛇头是否和身体碰撞
           or (new_head_x >= SCREEN_W or new_head_x < 0)    # 判断水平方向墙体碰撞
           or (new_head_y >= SCREEN_H or new_head_y < 0)):  # 判断竖直方向墙体碰撞
            # 弹出对话框，提示游戏结束
            print("游戏结束")
            QMessageBox.warning(self, "游戏结束", f"得分：{self.snake.score} 关闭窗口重启游戏")
            print("重启游戏")
            self.init_game()
            return
            
        # 触发界面刷新操作
        self.update()

    def keyPressEvent(self, event: QKeyEvent):
        # 判断是否按了Esc
        if event.key() == Qt.Key_Escape:
            # 关闭窗口
            # QApplication.exit()
            self.init_game()
            return
        
        self.snake.handle_event(event)
            
    def paintEvent(self, event: QPaintEvent):
        # return super().paintEvent(event)
        # 绘制自己想要的内容
        # 创建画笔
        qp = QPainter(self)
        # 画笔设置抗锯齿
        qp.setRenderHint(QPainter.Antialiasing, True)
        # 绘制背景图片
        qp.drawImage(0, 0, self.bg_img)
        
        qp.setPen(COLOR_GRAY)
        # 绘制网格
        # 绘制横线  y => [0, 20, 40 ... 480] 
        # (0,  0) -> (SCREEN_WITH, 0)
        # (0, 20) -> (SCREEN_WITH,20)
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
            qp.drawLine(0, y, SCREEN_WIDTH, y)
        # 绘制竖线  x => [0, 20, 40 ... 620] 
        # (0,  0) -> (0, SCREEN_HEIGHT)
        # (20,0) -> (20,SCREEN_HEIGHT)
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            qp.drawLine(x, 0, x, SCREEN_HEIGHT)
        
        # 绘制食物
        self.food.draw(qp)
        # 绘制蛇
        self.snake.draw(qp)
        
        # 画笔设置白色
        qp.setPen(QColor(255, 255, 255))
        # 设置字体：微软雅黑，字号16
        qp.setFont(QFont("微软雅黑", 16))
        # 左上角绘制得分
        qp.drawText(10, 20, f"得分：{self.snake.score}")
        # 右上角绘制帧率  200ms -> 1000ms / 200ms = 5帧/s
        qp.drawText(SCREEN_WIDTH - 120, 20, "帧率：{:.1f}".format(1000 / self.timer.interval()))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建窗口
    game = SnakeGame()
    game.show()
    # 让主程序阻塞运行
    sys.exit(app.exec_())
    
