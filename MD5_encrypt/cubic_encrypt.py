"""
对填充好的message进行一个立方和加密：
三数立方和问题在被加数为大数时具有单向性，分解困难
抗攻击性：
1. 将三数立方和封装进MD5后，验证Hash无法绕过立方和这一步，此时由于无法通过立方和结果反推多个被立方数，则无法构造后缀产生选择前缀攻击
2. 如果立方和要求明文末尾的分组与私钥key作用，那么无法产生长度扩展攻击，因为不知道私钥key，从而无法使末尾添加的消息与key进行立方和作用
"""


def cubic_sum(byte_array):
    def cube_sum(hex_nums):  # 求立方和函数
        result = sum(pow(int(num, 16), 3) for num in hex_nums)
        return result.to_bytes((result.bit_length() + 7) // 8, byteorder='big')

    i = 0
    cubic_sum_result = bytearray()  # 定义字节数组
    groups = [byte_array[i:i + 192] for i in range(0, len(byte_array), 192)]  # 192byte(即512bit*3)为一个group

    for group in groups[:-1]:  # 每个group内的三个512bit做立方和运算
        hex_nums = [group[i:i + 64].hex() for i in range(0, 192, 64)]
        cubic_sum_result.extend(cube_sum(hex_nums)[:192])
        i += 1

    if i != len(groups):  # 处理末尾
        last_group = groups[-1]
        hex_nums = [last_group[i:i + 64].hex() for i in range(0, len(last_group), 64)]
        cubic_sum_result.extend(cube_sum(hex_nums)[:len(last_group)])

    head_64 = byte_array[:64].hex()  # 最后一个64byte与第一第二个64byte作用
    if len(byte_array) < 65:
        second_64 = head_64
    else:
        second_64 = byte_array[64:128].hex()
    last_64 = byte_array[-64:].hex()
    cubic_sum_result.extend(cube_sum([head_64, second_64, last_64])[:192])

    return bytes(cubic_sum_result)
