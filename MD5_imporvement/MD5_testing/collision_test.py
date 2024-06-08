"""
3. 碰撞与抗碰撞测试（Collision Resistance Testing）
评估算法抗碰撞攻击的能力，即找到两个不同的输入产生相同哈希值的难度。

随机碰撞测试：生成大量随机输入，计算哈希值并检查是否存在哈希值碰撞。此方法虽然不能证明抗碰撞性，但可以提供一些统计信息。
结构性碰撞测试：采用已知的碰撞生成方法，测试新算法是否能抵抗这些攻击。

"""
import json
from utils import random_bytes


def collision_test(num_samples, hash_func, output_dir):
    seen_hashes = set()
    collisions = 0
    for _ in range(num_samples):
        #sample = random_string(20)
        sample = random_bytes(256)
        hash_value = hash_func(sample)
        if hash_value in seen_hashes:
            collisions += 1
        else:
            seen_hashes.add(hash_value)

    collision_probability = collisions / num_samples if num_samples > 0 else 0

    # 输出到文件
    with open(f'{output_dir}/collision_test.json', 'w') as f:
        json.dump(
            {'num_samples': num_samples, 'collisions': collisions, 'collision_probability': collision_probability}, f)

    return collision_probability
