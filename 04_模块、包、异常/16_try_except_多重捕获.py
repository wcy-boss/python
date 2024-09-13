
def write_file():
    # 打开文件资源
    file = None
    try:
        file = open("haha.txt", "w")
        a = 10
        b = 2
        rst = a / b
        
        arr = [2,3]
        
        val = arr[5]
        
        file.write(f"haha: {rst}")
    except ZeroDivisionError as e: # ZeroDivisionError
        print("出现除零异常：", e, type(e)) # 
    except PermissionError as e: # PermissionError
        print("出现权限异常：", e, type(e)) # 
    except IndexError as e:
        print("索引异常:", e, type(e))
    except Exception as e: # Exception
        print("出现未知异常：", e, type(e)) # 
    finally:
        if file is not None:
            file.close()
        print("关闭资源")
        
    
# print(read_file())
write_file()