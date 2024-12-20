import cv2
import os

# 输入视频文件路径
input_video_path = 'test.mp4'  # 请替换为你的输入视频路径
# 输出文件夹
output_folder = 'frames_output'
os.makedirs(output_folder, exist_ok=True)  # 创建输出文件夹

# 打开视频文件
cap = cv2.VideoCapture(input_video_path)

# 检查视频是否打开成功
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_count = 1  # 从 1 开始计数

while True:
    # 读取一帧
    ret, frame = cap.read()

    # 如果成功读取到帧
    if ret:
        # 使用填充零的格式化字符串保存每一帧为图像文件
        frame_output_path = os.path.join(output_folder, f'{frame_count:04d}.jpg')  # 格式化为 4 位数字

        # 写入帧到图像文件
        cv2.imwrite(frame_output_path, frame)

        print(f"Saved: {frame_output_path}")
        frame_count += 1
    else:
        break

# 释放视频捕获对象
cap.release()
print("Done processing video frames.")
