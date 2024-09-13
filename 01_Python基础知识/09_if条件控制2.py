"""
需求：
1. 定义 holiday_name 字符串变量记录节日名称
2. 如果是 情人节，应该 买玫瑰／看电影
3. 如果是 平安夜，应该 买苹果／吃大餐
4. 如果是 生日，应该 买蛋糕
5. 其他的日子，每天都是节日……
"""
holiday = input("请输入节日：")

if holiday == "情人节":
    print("买玫瑰／看电影")
elif holiday == "平安夜":
    print("买苹果／吃大餐")
elif holiday == "生日":
    print("买蛋糕")
else:
    print("发红包，亲亲抱抱举高高！")