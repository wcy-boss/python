def say_hello(score, name="刘亦菲", height=180):
    """测试参数
    :param score: 位置参数，放默认参数前边
    :param name: 默认值参数, 放后边，defaults to "刘亦菲"
    """
    print(f"你好: {name} 分数：{score} 身高：{height}")
    
    
# 缺少1个位置参数 TypeError: say_hello() missing 1 required positional argument: 'name'
say_hello(98, "热巴", 168) 
say_hello(100) 

def show_info(name, age = 18, height = 160.4):
    print(f"你好: {name} 年龄: {age} 身高：{height}")
    
# 关键字参数，可以不用考虑先后顺序问题
# 没有默认值的参数，必须按顺序赋值，或者提供关键字参数
show_info("流川枫")
show_info("流川枫", height=178)
show_info("流川枫", 17)
show_info(height=176, name="樱木花道", age=23)