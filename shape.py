import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import io
import torch


def draw_shape(radius, length, color):
    # 创建一个新的图形和坐标轴
    fig, ax = plt.subplots(figsize=(5, 5))

    # 计算矩形的高度
    height = 2 * radius

    # 添加左侧半圆
    left_circle = patches.Wedge(
        center=(radius, radius),  # 圆心位置
        r=radius,                 # 半径
        theta1=90,                # 起始角度
        theta2=270,               # 结束角度
        facecolor=color           # 填充颜色
    )
    ax.add_patch(left_circle)

    # 添加右侧半圆
    right_circle = patches.Wedge(
        center=(length + radius, radius),  # 圆心位置
        r=radius,                          # 半径
        theta1=-90,                        # 起始角度
        theta2=90,                         # 结束角度
        facecolor=color                    # 填充颜色
    )
    ax.add_patch(right_circle)

    # 添加中间的矩形
    rectangle = patches.Rectangle(
        (radius, 0),   # 左下角坐标
        length,        # 矩形的长度
        height,        # 矩形的高度
        facecolor=color  # 填充颜色
    )
    ax.add_patch(rectangle)

    # 设置坐标轴范围
    ax.set_xlim(0, length + 2 * radius)
    ax.set_ylim(0, height)

    # 设置坐标轴的比例和隐藏
    ax.set_aspect('equal')
    ax.axis('off')  # 隐藏坐标轴

    # 使用内存文件来捕获图像
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
    plt.close(fig)
    buf.seek(0)

    # 读取图像为NumPy数组
    image = plt.imread(buf)
    buf.close()

    # 转换为1WHC格式的张量
    image_tensor = torch.tensor(image).unsqueeze(0)  # 从HWC到1,H,W,C

    return image_tensor

# 示例调用
tensor = draw_shape(radius=1, length=3, color='blue')
print(tensor.shape)  # 应该输出: torch.Size([1, H, W, C])
