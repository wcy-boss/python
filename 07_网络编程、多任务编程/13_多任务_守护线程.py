import time
import threading # 线程

# 练习生：跳舞，唱歌，打篮球

def singing():
    print("singing线程：", threading.current_thread())
    for i in range(10):
        print("singing 鸡你太美...", i)
        time.sleep(0.5)
        
def dancing():
    print("dancing线程：", threading.current_thread())
    for i in range(10):
        print("dancing 铁山靠...", i)
        time.sleep(0.5)
        
def play_basketball():
    print("playing线程：", threading.current_thread())
    for i in range(10):
        print("playing篮球...", i)
        time.sleep(0.5)
        
# 必须所有的子线程都设置为守护线程，才能一起退出
if __name__ == '__main__':
    print("主线程：", threading.current_thread())
    t1 = threading.Thread(target=singing)
    # 将子线程设置为守护线程（必须在start之前） RuntimeError: cannot set daemon status of active thread
    t1.daemon = True
    # 启动线程
    t1.start()
    
    t2 = threading.Thread(target=dancing)
    # 将子线程设置为守护线程（必须在start之前）
    t2.daemon = True
    # 启动线程
    t2.start()
    
    t3 = threading.Thread(target=play_basketball, daemon=True)
    t3.start()
    
    time.sleep(2)
    print("主线程执行完毕，退出")
    exit(-123)
    
    print("------------------")
        