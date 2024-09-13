content_lst = [
    "哎呦，你干嘛", 
    "只因你太美",
    "两年半练习生"
]

# 通过with打开的文件，可以在使用结束后，自动close
with open("e.txt", "w+", encoding="utf-8") as f:
    for line in content_lst:
        f.write(f"{line}\n")
    
print("is closed: ", f.closed)
