"""
1. 均匀程度测试（Uniformity Testing）

哈希值的均匀性意味着输出的哈希值在整个哈希空间内均匀分布。可以通过以下方法测试：

- **频率分析**：对大量不同的输入计算哈希值，统计每个哈希值出现的频率。理想情况下，每个哈希值出现的概率应接近均匀分布。
- **统计测试**：可以使用统计学中的卡方检验（Chi-square test）来确定哈希值是否均匀分布。具体步骤如下：
  - 生成大量不同的输入数据，并计算对应的哈希值。
  - 将哈希值划分为多个区间，统计每个区间内哈希值的数量。
  - 使用卡方检验检查这些数量是否符合均匀分布。

"""
import json
import matplotlib.pyplot as plt
from scipy.stats import chisquare
#import random_bytes
from utils import random_bytes


def uniformity_test(num_samples, hash_func, output_dir):
    hash_buckets = {}
    for _ in range(num_samples):
        #sample = random_string(20)
        sample = random_bytes(256)
        hash_value = hash_func(sample)
        if hash_value not in hash_buckets:
            hash_buckets[hash_value] = 0
        hash_buckets[hash_value] += 1
    frequencies = list(hash_buckets.values())
    chi2_stat, p_value = chisquare(frequencies)

    # 输出到文件
    with open(f'{output_dir}/uniformity_test.json', 'w') as f:
        json.dump({'chi2_stat': chi2_stat, 'p_value': p_value, 'frequencies': frequencies}, f)

    # 绘制图表
    plt.hist(frequencies, bins=50)
    plt.title('Uniformity Test Histogram')
    plt.xlabel('Frequency')
    plt.ylabel('Count')
    plt.savefig(f'{output_dir}/uniformity_test_histogram.png')
    plt.close()

    return chi2_stat, p_value
