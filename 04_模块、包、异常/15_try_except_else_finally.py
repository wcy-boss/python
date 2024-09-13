
def write_file():
    # 打开文件资源
    file = None
    try:
        file = open("haha.txt", "w")
        a = 10
        b = 0
        rst = a / b
        file.write(f"haha: {rst}")
        print("无异常时，执行的代码1")
    except Exception as e: # PermissionError
        print("出现异常：", e, type(e)) # 
    else:
        print("无异常时，执行的代码2")
    finally:
        if file is not None:
            file.close()
        print("关闭资源")
    
# print(read_file())
write_file()