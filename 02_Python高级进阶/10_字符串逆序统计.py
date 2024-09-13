"""
需求
完成字符串的逆序以及统计
设计一个程序，要求只能输入长度低于31的字符串，否则提示用户重新输入
打印如下内容:

--------------------------------------------
您输入的字符串: zhongshanshan
长度: 13
逆序后为: nahsnahsgnohz
字符统计结果: z:1 h:3 o:1 n:3 g:1 s:2 a:2
--------------------------------------------
"""
sss = """--------------------------------------------
您输入的字符串: {}
长度: {}
逆序后为: {}
字符统计结果: {}
--------------------------------------------"""

# 要求只能输入长度低于31的字符串，否则提示用户重新输入
string = ""
while True:
    string = input("请输入字符串：")
    if len(string) >= 31:
        print("请输入长度小于31的字符串, 当前长度：", len(string))
        continue
    
    break

stat_dict = dict() # 创建一个空字典{} z h o n g s h a  nshan

for s in string:    # 逐个遍历每一个字符
    if s not in stat_dict:
        # 字符没出现过在字典里
        stat_dict[s] = 1  # 初始为1
        # stat_dict.setdefault(s, 1) # 初始为1
    else:
        # 以前有存过这个字符, 把数量+1
        stat_dict[s] += 1 # +1

# print(stat_dict) # {'z': 1, 'h': 3, 'o': 1, 'n': 3, 'g': 1, 's': 2, 'a': 2}
# 将所有键值对的字典通过推导式，转成字符串的列表 ['z->1', 'h->3', 'o->1', 'n->3', 'g->1', 's->2', 'a->2']
stat_str = ["{}->{}".format(k, v) for k,v in stat_dict.items()]
# print(stat_str)
# 将字符串的列表通过空格" "合并成一个完整的字符串 "z->1 h->3 o->1 n->3 g->1 s->2 a->2"
print(" ".join(stat_str))

# 格式化输出
print(sss.format(
    string,
    len(string),        # 长度
    string[::-1],       # 逆序
    " ".join(stat_str)
))