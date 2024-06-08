"""
使用混沌系统logistic生成S盒子，对每一轮abcd加密
Seed和r由原文分组的头尾决定
要求：代换表必须足够混沌（需测试）
"""
import numpy as np


def logistic_map(x, r):
    return r * x * (1 - x)


def generate_chaos_sequence(seed, r):
    chaos_sequence = np.zeros((16, 16), dtype=int)
    x = seed

    for i in range(16):
        for j in range(16):
            x = logistic_map(x, r)
            s = format(int(x * (16 ** 2) % 256), '02x')  # 将混沌值映射到0-255的整数范围内
            chaos_sequence[i][j] = int(s, 16)

    return chaos_sequence


def apply_logistic_map(hex_string, log_map):
    # 混沌mao代换
    output = ""
    for i in range(0, len(hex_string), 2):
        row = int(hex_string[i], 16)
        column = int(hex_string[i + 1], 16)
        value = log_map[row][column]
        output += format(value, '02x')

    return output


"""
# 测试
seed = 0.5457
r = 3.9
n = 16
chaos_sequence = generate_chaos_sequence(seed, r)

print(chaos_sequence)
"""
