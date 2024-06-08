import os
import json
import time

import matplotlib.pyplot as plt
from modified_md5 import md5  # 可在此处修改为导入待测试的加密算法代码的文件
from uniformity_test import uniformity_test
from avalanche_effect_test import avalanche_effect_test
from collision_test import collision_test
from utils import random_bytes


def get_next_exp_dir(output_base_dir):
    """Determine the next available experiment directory name."""
    exp_dirs = [d for d in os.listdir(output_base_dir) if d.startswith('exp')]
    exp_nums = [int(d[3:]) for d in exp_dirs if d[3:].isdigit()]
    next_exp_num = max(exp_nums, default=1) + 1 if exp_nums else 1
    return os.path.join(output_base_dir, f'exp{next_exp_num}')


def main():
    """
    #直接输出到output文件夹中
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    """
    # 将输出结果打包输出到output/exp 文件夹中，每次测试输出结果到一个单独的文件夹中
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_base_dir = os.path.join(base_dir, 'output')
    output_dir = get_next_exp_dir(output_base_dir)
    os.makedirs(output_dir)

    num_samples = 1000  # 测试样本量

    # 记录测试开始的时间
    start_time = time.time()
    # 均匀程度测试
    chi2_stat, p_value = uniformity_test(num_samples=num_samples, hash_func=md5, output_dir=output_dir)
    print(f"Uniformity Test: Chi2 Stat = {chi2_stat}, p-value = {p_value}")
    # 记录均匀测试的时间，输出用时
    end_time1 = time.time()
    execution_time1 = end_time1 - start_time
    print(f"-测试均匀程度用时为: {execution_time1} 秒")

    # 记录混淆测试开始的时间
    start_time2 = time.time()
    # 混淆程度测试
    sample = random_bytes(256)
    mean_distance = avalanche_effect_test(sample, hash_func=md5, output_dir=output_dir)
    print(f"Avalanche Effect Test: Mean Hamming Distance = {mean_distance}")
    # 记录混淆测试的时间，输出用时
    end_time2 = time.time()
    execution_time2 = end_time2 - start_time2
    print(f"-测试混淆程度用时为: {execution_time2} 秒")

    # 记录碰撞测试开始的时间
    start_time3 = time.time()
    # 碰撞测试
    collision_probability = collision_test(num_samples=num_samples, hash_func=md5, output_dir=output_dir)
    print(f"Collision Test: Collision Probability = {collision_probability}")
    # 记录碰撞测试的时间，输出用时
    end_time3 = time.time()
    execution_time3 = end_time3 - start_time3
    print(f"-测试混淆程度用时为: {execution_time3} 秒")


    # 记录测试结束的时间，输出用时
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"测试总用时为: {execution_time} 秒")


    # 汇总结果
    results = {
        'uniformity': {'chi2_stat': chi2_stat, 'p_value': p_value, 'frequencies': []},
        'avalanche': {'mean_distance': mean_distance, 'distances': []},
        'collision': {'num_samples': num_samples, 'collisions': 0, 'collision_probability': collision_probability}
    }

    # 读取单独的结果文件并合并到总结果中
    with open(f'{output_dir}/uniformity_test.json', 'r') as f:
        uniformity_data = json.load(f)
        results['uniformity'].update(uniformity_data)

    with open(f'{output_dir}/avalanche_effect_test.json', 'r') as f:
        avalanche_data = json.load(f)
        results['avalanche'].update(avalanche_data)

    with open(f'{output_dir}/collision_test.json', 'r') as f:
        collision_data = json.load(f)
        results['collision'].update(collision_data)

    with open(f'{output_dir}/results_summary.json', 'w') as f:
        json.dump(results, f)

    # 绘制综合结果图表
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 3, 1)
    plt.bar(['Chi2 Stat'], [chi2_stat])
    plt.title('Uniformity Test Chi2 Stat')

    plt.subplot(1, 3, 2)
    plt.bar(['Mean Hamming Distance'], [mean_distance])
    plt.title('Avalanche Effect Test')

    plt.subplot(1, 3, 3)
    plt.bar(['Collision Probability'], [collision_probability])
    plt.title('Collision Test')

    plt.tight_layout()
    plt.savefig(f'{output_dir}/results_summary.png')
    plt.close()


if __name__ == "__main__":
    main()
