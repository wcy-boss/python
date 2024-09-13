"""-------------------家具类------------------------"""
class Item:
    
    def __init__(self, name, area) -> None:
        """家具类的初始化方法

        :param name: 家具名称
        :param area: 家具占地面积
        """
        self.name = name
        self.area = area
        
    def __str__(self) -> str:
        return "str家具：{} 占用面积：{}".format(self.name, self.area)
    
    def __repr__(self) -> str:
        return "repr家具：{} 占用面积：{}".format(self.name, self.area)
    
"""-------------------房子类------------------------"""
class House:
    
    def __init__(self, address, area) -> None:
        self.address = address  # 地址
        self.area = area        # 房子总面积
        self.free_area = self.area # 剩余面积
        self.items = []         # 所有家具的列表
    
    def __str__(self) -> str:
        return f"房子地址：{self.address} 总面积：{self.area} 剩余面积：{self.free_area}"
    
    def add_item(self, item: Item):
        """添加家具到房子里
        剩余面积 >= 家具的面积时，才允许添加

        :param item: 家具类Item的对象（实例）
        """
        if self.free_area >= item.area:
            self.items.append(item)
            self.free_area -= item.area
            print("添加成功:", item)
        else:
            print("面积不足，无法添加：", item)
    
# 创建对象
sofa = Item("沙发", 5)
bed  = Item("大床", 15)
desktop = Item("桌椅套装", 30)
home_movie = Item("家庭影院", 60)
print(sofa)
print(bed)
print(desktop)
print(home_movie)

# 创建房子
house = House("深圳湾一号", 100)
# 输出房子信息
print(house)

print("----------------------------------------")

house.add_item(sofa)
house.add_item(bed)
house.add_item(desktop)
house.add_item(home_movie)
print(house)
# 如果对象在容器中（列表、元组），直接打印容器，需要重写类的__repr__函数，才能正确打印
print(house.items)