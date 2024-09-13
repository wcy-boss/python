import time

# 练习生：跳舞，唱歌，打篮球

def singing():
    for i in range(5):
        print("singing鸡你太美...", i)
        time.sleep(0.5)
        
def dancing():
    for i in range(5):
        print("dancing铁山靠...", i)
        time.sleep(0.5)
        
if __name__ == '__main__':
    singing()
    dancing()
