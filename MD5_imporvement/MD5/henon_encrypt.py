def henon_map(x, y, a, b):
    """
    Henon映射函数
    参数:
        x: 当前x坐标
        y: 当前y坐标
        a: 控制参数a
        b: 控制参数b
    返回值:
        下一个x坐标, 下一个y坐标
    """
    x_next = 1 - a * x ** 2 + y
    y_next = b * x
    return x_next, y_next


def map_to_integer(value, min_val, max_val):
    """
    将值映射到整数范围
    参数:
        value: 原始值
        min_val: 映射的最小值
        max_val: 映射的最大值
    返回值:
        映射后的整数值
    """
    range_val = max_val - min_val
    return int(min_val + (value * range_val)) % 16


def generate_henon_array(row, line, a, b, min_val, max_val):
    """
    生成Henon映射的二维数组
    参数:
        size: 数组维度
        a: 控制参数a
        b: 控制参数b
        min_val: 映射的最小整数值
        max_val: 映射的最大整数值
    返回值:
        生成的二维数组
    """
    array = [[0 for _ in range(line)] for _ in range(row)]
    x, y = 0.1, 0.1  # 初始坐标
    for i in range(row):
        for j in range(line):
            mapped_value = map_to_integer(x, min_val, max_val)
            array[i][j] = mapped_value
            x, y = henon_map(x, y, a, b)
    return array


def multiply_string_item(str_x, hen_line):
    str_list = list(str_x)  # 将字符串转换为列表
    for i in range(len(str_x)):
        str_list[i] = hex(int(str_list[i], 16) * hen_line[i] % 16)[2:]  # 修改列表中的元素,替换为行*列结果中相应的元素
    return "".join(str_list)  # 将列表转换回字符串
