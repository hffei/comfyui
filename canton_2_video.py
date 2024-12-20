import cv2
import os

# 视频输出设置
output_video_path = 'output_video.avi'  # 输出视频文件名
frame_rate = 30  # 帧率
image_folder = 'G:\\ComfyUI_FK_202408\\ComfyUI\\output'  # 你的图片文件夹路径

# 获取图像文件名并排序
image_files = [f'bubu_{i:05d}_.png' for i in range(1, 1205)]  # 从 1 到 1205
image_files = [os.path.join(image_folder, img) for img in image_files]  # 完整路径

# 确保输出视频的路径是有效的
if not os.path.exists(image_folder):
    print(f"Error: The folder {image_folder} does not exist.")
    exit()

# 读取第一帧以确定视频的大小
first_frame = cv2.imread(image_files[0])
height, width, layers = first_frame.shape

# 创建 VideoWriter 对象
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 使用 XVID 编码
video_writer = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (width, height))

# 遍历所有图像文件并写入视频
for image_file in image_files:
    frame = cv2.imread(image_file)
    if frame is None:
        print(f"Warning: {image_file} could not be read and will be skipped.")
        continue
    video_writer.write(frame)  # 将帧写入视频

# 释放 VideoWriter 对象
video_writer.release()
print(f"Video {output_video_path} has been created successfully.")
