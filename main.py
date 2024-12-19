from PIL import Image, ImageDraw


def draw_line_on_image(image_path, start_x, start_y, end_x, end_y, line_color, line_thickness, output_path):
    # 打开图像
    image = Image.open(image_path)

    # 创建一个可绘制的对象
    draw = ImageDraw.Draw(image)

    # 绘制线条
    draw.line([(start_x, start_y), (end_x, end_y)], fill=line_color, width=line_thickness)

    # 保存修改后的图像
    image.save(output_path)
    print(f"Line drawn and image saved to {output_path}")


# 使用示例
image_path = '11.jpg'  # 输入图片的路径
start_x, start_y = 50, 50  # 线条起始坐标
end_x, end_y = 200, 200  # 线条结束坐标
line_color = (0, 255, 0)  # 线条颜色 (R, G, B) 格式
line_thickness = 25  # 线条宽度
output_path = 'output_image.jpg'  # 输出图片的路径

draw_line_on_image(image_path, start_x, start_y, end_x, end_y, line_color, line_thickness, output_path)
