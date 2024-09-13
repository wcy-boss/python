class WashMachine:
    
    def __init__(self, brand, capacity) -> None:
        """初始化方法

        :param brand: 品牌
        :param capacity: 容量
        """ 
        self.brand = brand
        self.capacity = capacity
        # 门是否关闭
        self.__is_closed = False
        # 模式 0:未设定模式 1:轻揉模式 2:狂揉模式
        self.__mode = 0
        # 马达转速
        self.__motor_speed = 0
        
    def __set_motor_speed(self, speed):
        self.__motor_speed = speed
        
    def open_door(self):
        self.__is_closed = False
        print("打开洗衣机门")
        
    def close_door(self):
        self.__is_closed = True
        print("关闭洗衣机门")
        
    def set_mode(self, new_mode):
        """设置模式，只允许是1或2
        :param new_mode: 新的模式
        """
        if new_mode in [0, 1, 2]: # 模式是1或2
            self.__mode = new_mode
            print("设置模式：", new_mode)
        else:
            print('模式无法设置：', new_mode)
        
    def wash(self):
        if not self.__is_closed:
            # 门没关，提示用户
            print("请关闭洗衣机门，哔哔哔...")
            return
        
        if self.__mode == 0:
            print("请先设置模式")
            return
        
        print("放水....哗哗哗")
        print("放满了")
        if self.__mode == 1: # 轻柔模式
            print("轻柔模式，洗内衣")
            # 调节马达转速
            self.__set_motor_speed(1000)
            print("马达转速：", self.__motor_speed)
            print("开始洗衣服")
        elif self.__mode == 2: # 狂暴模式
            print("狂暴模式，洗大衣")
            # 调节马达转速
            self.__set_motor_speed(2000)
            print("马达转速：", self.__motor_speed)
            print("开始洗衣服")
        
        print("洗完了！哔哔哔！")

machine = WashMachine("海尔", 10)
machine.open_door()
# 放衣服
machine.close_door()
machine.set_mode(1)
machine.wash()

