"""
超市买苹果计算金额
需求:	
●  收银员输入苹果的价格price，单位：元/斤
●  收银员输入用户购买苹果的重量weight，单位：斤
●   计算并输出付款金额:xxx元
"""
# ●  收银员输入苹果的价格price，单位：元/斤
price = float(input("请输入苹果单价(单位：元/斤)："))

# ●  收银员输入用户购买苹果的重量weight，单位：斤
weight = float(input("请输入购买的重量（单位：斤）"))

# ●   计算并输出付款金额:xxx元
total = price * weight

# 格式化打印字符串
print("重量：%.2f 斤，付款金额: %.2f 元" % (weight, total))