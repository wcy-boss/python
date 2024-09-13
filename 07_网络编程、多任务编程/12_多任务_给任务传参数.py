import time
import threading # 线程

# 练习生：跳舞，唱歌，打篮球

def singing(name, age = 18, score = 99):
    # print(threading.current_thread())
    print(f"name: {name} age: {age} score: {score}")
    for i in range(5):
        print(f"{name} singing 鸡你太美...", i)
        time.sleep(0.5)
        
    print("店员：对不起，书卖完了!")
        
        
if __name__ == '__main__':
    # 参数传递方式1：元组, 只有一个元素时，记得加逗号（10，)
    # t1 = threading.Thread(target=singing, args=("坤坤", ))
    # 参数传递方式2：字典，不要求顺序
    # t1 = threading.Thread(target=singing, kwargs={"score": 97, "name": "张靓颖"})
    # 参数传递方式3：元组+字典 (元组里的元素不可以和字典里的元素冲突)
    t1 = threading.Thread(target=singing, args=("坤坤", 22), kwargs={"score": 97})
    t1.start()
    
    for i in range(20):
        print("主任务: ", i)
        time.sleep(0.5)
        