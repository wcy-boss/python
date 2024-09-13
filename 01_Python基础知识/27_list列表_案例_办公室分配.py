"""
需求
一个学校，有3个办公室，现在有8位老师等待工位的分配
['袁腾飞', '罗永浩', '俞敏洪', '李永乐', '王芳芳', '马云', '李彦宏', '马化腾']

请编写程序:
1. 完成随机的分配
2. 打印办公室信息 (每个办公室中的人数，及分别是谁)

进阶：保证每个办公室至少1人
"""
import random
rooms = [
    [],
    [],
    []
]

teachers = ['袁腾飞', '罗永浩', '俞敏洪', '李永乐', '王芳芳', '马云', '李彦宏', '马化腾']

for teacher in teachers:
    # 生成随机数
    room_id = random.randint(0, 2)
    # 把老师请到对应办公室
    rooms[room_id].append(teacher)
    
index = 0
for room in rooms:
    # 获取每个房间人数
    count = len(room)
    print("房间[{}]人数 {} : {}".format(index, count, room))
    index += 1