tips = """
**************************************************
欢迎使用[名片管理系统]V1.0

1.新建名片
2.显示名片
3.查询名片

0.退出系统
**************************************************"""
cards = [
    ["沙务净", "13588886666", "888666","shawujing@163.com"],
    ["唐三葬", "13866669999", "666999","sanzang@163.com"],
    ["白骨精", "13999998888", "999888","baigujing@163.com"]
]

def create_card():
    """创建名片，追加到cards里
    """
    print("【新建名片】")
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ：")
    email = input("请输入邮箱：")
    card = [name, phone, qq, email]
    cards.append(card)
    print("【名片 {} 创建成功】".format(name))
    

def show_cards():
    """显示所有名片2
    """
    print("【显示名片】")
    
    # for item in ["姓名", "电话", "QQ", "邮箱"]:
    #     print(item, end="\t")
    print("{}\t{}\t\t{}\t{}".format("姓名", "电话", "QQ", "邮箱"))
    print("---------------------------------------------------")
    for card in cards:
        print("{}\t{}\t{}\t{}".format(card[0], card[1], card[2], card[3]))

def query_card():
    print("【查询名片】")
    query_name = input("请输入要查询的姓名：")
    for card in cards:
        if card[0] == query_name: # card[0]是姓名
            print("找到了-> ", card)
            handle_card(card)
            break
    else:
        # 循环结束，没发生break，没有找到
        print("没有找到-> {}".format(query_name))

def handle_card(card):
    while True:
        action = input("请输入对名片的操作: 1.修改/ 2.删除/ 0.返回上一级:")
        if action == "1":
            print("【修改名片】")
            card[0] = input("请输入姓名：")
            card[1] = input("请输入电话：")
            card[2] = input("请输入QQ：")
            card[3] = input("请输入邮箱：")
            print("【{} 名片修改成功】".format(card[0]))
            break
        elif action == "2":
            print("【删除名片】")
            cards.remove(card)
            print("【{} 名片删除成功】".format(card[0]))
            break
        elif action == "0":
            print("【返回上一级】")
            break
        else:
            print("输入错误，请重新输入：", action)
        

while True:
    print(tips)
    action = int(input("请输入操作："))
    if action == 1:
        create_card()
    elif action == 2:
        show_cards()
    elif action == 3:
        query_card()
    elif action == 0:
        print("【退出系统】")
    else:
        print("输入错误，请重新输入：", action)
    