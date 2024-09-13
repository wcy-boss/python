content_lst = [
    "哎呦，你干嘛", 
    "只因你太美",
    "两年半练习生"
]

# 相对路径： ./当前目录  ../上一级目录
with open("../day02/a.txt", "w+", encoding="utf-8") as f:
    for line in content_lst:
        f.write(f"{line}\n")
    
# 绝对路径:
# 方式1：双反斜线 \\  D:\\WS\\Python\\Lessons\\Code\\day02\\a.txt
# 方式2：正斜线    /  D:/WS/Python/Lessons/Code/day02/c.txt
with open("D:/WS/Python/Lessons/Code/day02/c.txt", "w+", encoding="utf-8") as f:
    for line in content_lst:
        f.write(f"{line}\n")
