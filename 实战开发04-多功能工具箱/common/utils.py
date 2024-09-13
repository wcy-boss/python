import os
import time
import socket
import ipaddress

def get_local_ip():
    """
    获取本机所有IP
    :return: IP列表
    """
    local_ips = ["127.0.0.1"]
    for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
        local_ips.append(ip)

    local_ips.sort(reverse=True)
    return local_ips

def decode_data(recv_data: bytes):
    try:
        recv_msg = recv_data.decode("utf-8")
    except:
        recv_msg = recv_data.decode("gbk")
    return recv_msg


def decode_to_hex_str(data: bytes):
    # 将hex字符串转成大写，每两个字符用空格分隔
    data_hex = data.hex().upper()
    data_hex = " ".join([data_hex[i:i + 2] for i in range(0, len(data_hex), 2)])
    return data_hex


def hex2str(data, with_space=True, with_0x=True):
    """ Convert hex data to string

    Example:
    input: [255,227,2]
    output: "0xFF 0xE3 2"
    
    input: 255
    output: "0xFF"

    :param data: 数字或列表
    :param with_space: 是否带空格
    :param with_0x: 是否带0x
    """
    spliter = " " if with_space else ""
    prefix = "0x" if with_0x else ""
    if type(data) == int:
        rst = hex(data)
        if not with_0x:
            rst = rst[2:]
        return rst
    
    return spliter.join([f"{prefix}{i:02X}" for i in data])
    
def str2hex(data_str: str):
    """ Convert string to hex data
    inut:
    0xFF 0xE3 0x2
    FF E3 2
    FF E3 02
    FFE302
    
    output:
    [0xFF, 0xE3, 0x2]
    
    :param data: 字符串
    :return: 十六进制数据 [0xFF, 0xE3, 0x2]
    """
    # 移除所有0x
    data_str = data_str.replace("0x", "")
    # 如果有的数字是单个的话，补0
    items = data_str.split(" ")
    for i in range(len(items)):
        if len(items[i]) == 1:
            items[i] = "0" + items[i]
    # 移除所有空格
    data_str = "".join(items)
    
    # 每隔两个字符转成数字
    return bytes.fromhex(data_str)

def crc16_xmodem(data, poly=0x1021, crc=0x0000):
    for byte in data:
        crc ^= (byte << 8)
        for _ in range(8):
            if (crc & 0x8000):
                crc = ((crc << 1) ^ poly) & 0xFFFF
            else:
                crc <<= 1
    return crc

def crc16_modbus(data):
    """
    计算 Modbus CRC16 校验码
    :param data: 待计算的数据，类型为 bytes
    :return: CRC16 校验码，类型为 int
    """
    crc = 0xFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc

class Color:
    """
    颜色枚举类
    """
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    PURPLE = 35
    CYAN = 36


def wrap_color(msg, color):
    """
    包装颜色
    :param msg: 要包装的字符串
    :param color: 颜色
    :return:
    """
    return f"\033[{color}m{msg}\033[0m"


def calculate_broadcast_address(host, mask_bits):
    # 将主机IP地址和掩码位数转换为网络对象
    network = ipaddress.ip_network(f"{host}/{mask_bits}", strict=False)

    # 获取广播地址
    broadcast_address = network.broadcast_address

    # 返回广播地址的字符串表示形式
    return str(broadcast_address)


def current_time_str():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def clear_console():
    # 使用ANSI转义序列清空控制台内容
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    bytes_data = b"\x01\x02\x03\x00\x01\x02"
    # 输出结果是大端显示(最高位在前)
    print(hex2str(bytes_data, with_0x=False))
    
    rst_num = crc16_modbus(bytes_data)
    
    # 输出结果是大端显示(最高位在前)
    print(hex2str(rst_num))
    
    # 将一个数字转成2个字节
    bytes_arr = rst_num.to_bytes(2, byteorder='little')
    # 等同于
    # little
    arr = [
        rst_num & 0xFF,
        (rst_num >> 8) & 0xFF,
    ]
    
    print(hex2str(bytes_arr))
    print(hex2str(arr))
    
    print(hex(65280))
    
    print("------------------------------")
    
    bytes_data = str2hex("01 03 02 56 31")
    crc16_rst = crc16_modbus(bytes_data)
    print(hex2str(crc16_rst))


    print(get_local_ip())
    
    print(wrap_color("你好，红色", Color.GREEN))