import math
import random_bytes
import cubic_encrypt
import S_box_encrypt
import logistic_encrypt
import henon_encrypt

# 初始化MD5常量
T = [int(abs(math.sin(i + 1)) * 2 ** 32) & 0xFFFFFFFF for i in range(64)]


# 定义循环左移函数
def left_rotate(x, c):
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF


# 定义MD5算法函数
def md5(message):
    # 初始化变量
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    # 将十六进制字符串转换为字节数组
    message = bytearray.fromhex(message)

    # 以512位分组处理输入消息
    original_length = (8 * len(message)) & 0xffffffffffffffff
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0)

    message += original_length.to_bytes(8, 'little')

    # 处理每个64个字节的分组
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]

        # 初始化哈希值
        aa = a
        bb = b
        cc = c
        dd = d

        # 主循环
        for j in range(64):
            if j < 16:
                f = (b & c) | ((~b) & d)  # 定义四个不同的非线性函数
                g = j
            elif j < 32:
                f = (d & b) | ((~d) & c)  # 定义四个不同的非线性函数
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d  # 定义四个不同的非线性函数
                g = (3 * j + 5) % 16
            else:
                f = c ^ (b | (~d))  # 定义四个不同的非线性函数
                g = (7 * j) % 16

            temp = d
            d = c
            c = b
            b = (b + left_rotate((a + f + T[j] + int.from_bytes(chunk[4 * g:4 * g + 4], 'little')), 7)) & 0xFFFFFFFF
            a = temp

        # 更新哈希值
        a = (a + aa) & 0xFFFFFFFF
        b = (b + bb) & 0xFFFFFFFF
        c = (c + cc) & 0xFFFFFFFF
        d = (d + dd) & 0xFFFFFFFF

        # 使用混沌系统logistic_map构建每一轮加密的S代换表 !!!!!!!!!!!这一步非常危险，很容易翻车
        log = logistic_encrypt.generate_chaos_sequence(0.5457 - chunk[63] * 0.000002 * chunk[32],
                                                       3.9 - chunk[0] * 0.001)
        # print(log, "\n\n")  # 显示用 可以删掉
        a = logistic_encrypt.apply_logistic_map(format(a, 'x').zfill(8), log)
        b = logistic_encrypt.apply_logistic_map(format(b, 'x').zfill(8), log)
        c = logistic_encrypt.apply_logistic_map(format(c, 'x').zfill(8), log)
        d = logistic_encrypt.apply_logistic_map(format(d, 'x').zfill(8), log)

        a = int(a, 16)
        b = int(b, 16)
        c = int(c, 16)
        d = int(d, 16)

    # md5主体基本完成
    output = a.to_bytes(4, 'little') + b.to_bytes(4, 'little') + c.to_bytes(4, 'little') + d.to_bytes(4, 'little')
    output = output.hex()
    # print("md5+CubicSum+log:\t\t", output)

    # 使用S盒子做代换，增加非线性混淆
    output = S_box_encrypt.apply_s_box(output)
    # 返回最终哈希值
    return output
