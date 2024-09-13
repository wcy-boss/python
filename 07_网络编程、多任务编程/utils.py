def decode_data(data: bytes):
    try:
        return data.decode("GBK")
    except:
        return data.decode("UTF-8")