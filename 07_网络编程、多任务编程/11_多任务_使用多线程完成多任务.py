import time
import threading # 线程

# 练习生：跳舞，唱歌，打篮球

def singing():
    print("singing线程：", threading.current_thread())
    for i in range(5):
        print("singing 鸡你太美...", i)
        time.sleep(0.5)
        
def dancing():
    print("dancing线程：", threading.current_thread())
    for i in range(5):
        print("dancing 铁山靠...", i)
        time.sleep(0.5)
        
if __name__ == '__main__':
    print("主线程：", threading.current_thread())
    t1 = threading.Thread(target=singing)
    t1.start()
    t2 = threading.Thread(target=dancing)
    t2.start()
    
    for i in range(10):
        print("主任务:", i)
        time.sleep(0.5)
        