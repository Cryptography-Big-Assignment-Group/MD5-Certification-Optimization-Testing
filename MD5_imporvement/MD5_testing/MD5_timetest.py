"""
该函数用于测试md5优化函数生成摘要的时间
"""

import modified_md5
import time
import random_bytes
from module import MD5

n = 1000

# 记录生成开始的时间
start_time = time.time()
# 生成摘要
for i in range(n):
    result = MD5.md5(random_bytes.random_bytes_init(512))
# 记录测生成结束的时间，输出用时
end_time = time.time()
execution_time = end_time - start_time
print(f"经典MD5算法：{n}次生成总用时为: {execution_time} 秒，单次摘要生成用时为{execution_time/n}秒")

# 记录生成开始的时间
start_time = time.time()
# 生成摘要
for i in range(n):
    result = modified_md5.md5(random_bytes.random_bytes_init(512))
# 记录测生成结束的时间，输出用时
end_time = time.time()
execution_time = end_time - start_time
print(f"优化MD5算法：{n}次生成总用时为: {execution_time} 秒，单次摘要生成用时为{execution_time/n}秒")