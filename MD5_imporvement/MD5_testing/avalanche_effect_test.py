"""
2. 混淆程度测试（Avalanche Effect）
Avalanche效应意味着输入的微小变化（如单个位的改变）会导致输出的哈希值发生大规模变化。可以通过以下方法测试：

单比特变化测试：对一组输入数据，计算其原始哈希值，然后对每个输入数据仅改变一位，再计算新哈希值。比较原始哈希值和新哈希值的不同位数。理想情况下，改变输入的一个比特应导致输出哈希值约有一半的位发生变化（即约50%的位翻转）。
哈希差异统计：对比不同输入的哈希值差异。计算原始输入和单比特变化输入的哈希值的汉明距离（Hamming Distance），即两者不同的位数。

"""
import json
import matplotlib.pyplot as plt
import numpy as np
from utils import random_bytes
from modified_md5 import md5
import os


# 确保输入是有效的十六进制字符串
def ensure_hex_string(s):
    try:
        bytes.fromhex(s)
        return True
    except ValueError:
        return False

# 混沌程度测试（Avalanche Effect）
def avalanche_effect_test(sample, hash_func, output_dir):
    while not ensure_hex_string(sample):
        sample = random_bytes(256)

    original_hash = hash_func(sample)
    flipped_hashes = []

    # 将输入转换为字节数组
    sample_bytes = bytearray.fromhex(sample)

    for i in range(len(sample_bytes) * 8):
        flipped_sample = sample_bytes[:]
        flipped_sample[i // 8] ^= (1 << (i % 8))
        flipped_sample_hex = flipped_sample.hex()

        while not ensure_hex_string(flipped_sample_hex):
            flipped_sample_hex = random_bytes.random_bytes(256)

        flipped_hash = hash_func(flipped_sample_hex)
        flipped_hashes.append(flipped_hash)

    def hamming_distance(s1, s2):
        return sum(el1 != el2 for el1, el2 in zip(s1, s2))

    distances = [hamming_distance(original_hash, h) for h in flipped_hashes]
    mean_distance = np.mean(distances)

    # 输出到文件
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(f'{output_dir}/avalanche_effect_test.json', 'w') as f:
        json.dump({'mean_distance': mean_distance, 'distances': distances}, f)

    # 绘制图表
    plt.hist(distances, bins=50)
    plt.title('Avalanche Effect Test Histogram')
    plt.xlabel('Hamming Distance')
    plt.ylabel('Count')
    plt.savefig(f'{output_dir}/avalanche_effect_test_histogram.png')
    plt.close()

    return mean_distance


def main():
    output_dir = 'output'
    sample = random_bytes(256)
    mean_distance = avalanche_effect_test(sample, hash_func=md5, output_dir=output_dir)
    print(f"Avalanche Effect Test: Mean Hamming Distance = {mean_distance}")


