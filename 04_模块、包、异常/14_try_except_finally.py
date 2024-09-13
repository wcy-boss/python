def read_file():
    a = 10
    b = 4
    
    try:
        rst = a / b
        print("1. 计算结果:", rst)
        return rst
    except:
        print("2. 出现异常")
    finally:
        # 无论是否发生异常，此代码一定会执行
        print("3. 关闭资源")
    
def write_file():
    # 打开文件资源
    file = None
    try:
        file = open("hiahia.txt", "w")
        a = 10
        b = 2
        rst = a / b
        file.write(f"haha: {rst}")
    except Exception as e: # PermissionError
        print("出现异常：", e, type(e)) # 
    finally:
        if file is not None:
            file.close()
        print("关闭资源")
    
# print(read_file())
write_file()