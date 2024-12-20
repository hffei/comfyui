import requests
import json
import os

# 设置文件夹和接口
image_folder = 'G:\\dev\\comfyui\\frames_output'  # 图片所在文件夹
url = 'http://localhost:8188/prompt'  # 接口地址

# 遍历所有图像文件
for i in range(1, 1206):  # 从 1 到 1206
    # 格式化文件名
    image_filename = f'{i:04d}.jpg'
    image_path = os.path.join(image_folder, image_filename)

    # 检查文件是否存在
    if not os.path.exists(image_path):
        print(f"File {image_path} not found, skipping...")
        continue

    # 构建请求的 JSON 数据
    payload = {
        "prompt": {
            "3": {
                "inputs": {
                    "seed": 172327074680789,
                    "steps": 20,
                    "cfg": 8,
                    "sampler_name": "euler",
                    "scheduler": "normal",
                    "denoise": 0.3,
                    "model": ["4", 0],
                    "positive": ["6", 0],
                    "negative": ["7", 0],
                    "latent_image": ["11", 0]
                },
                "class_type": "KSampler",
                "_meta": {
                    "title": "K采样器"
                }
            },
            "4": {
                "inputs": {
                    "ckpt_name": "A2D卡通.safetensors"
                },
                "class_type": "CheckpointLoaderSimple",
                "_meta": {
                    "title": "Checkpoint加载器(简易)"
                }
            },
            "6": {
                "inputs": {
                    "text": "",
                    "speak_and_recognation": True,
                    "clip": ["4", 1]
                },
                "class_type": "CLIPTextEncode",
                "_meta": {
                    "title": "CLIP文本编码器"
                }
            },
            "7": {
                "inputs": {
                    "text": "text, watermark",
                    "speak_and_recognation": True,
                    "clip": ["4", 1]
                },
                "class_type": "CLIPTextEncode",
                "_meta": {
                    "title": "CLIP文本编码器"
                }
            },
            "8": {
                "inputs": {
                    "samples": ["3", 0],
                    "vae": ["4", 2]
                },
                "class_type": "VAEDecode",
                "_meta": {
                    "title": "VAE解码"
                }
            },
            "9": {
                "inputs": {
                    "filename_prefix": "bubu",
                    "images": ["8", 0]
                },
                "class_type": "SaveImage",
                "_meta": {
                    "title": "保存图像"
                }
            },
            "10": {
                "inputs": {
                    "image": image_path,  # 加载当前图像
                    "upload": "image"
                },
                "class_type": "LoadImage",
                "_meta": {
                    "title": "加载图像"
                }
            },
            "11": {
                "inputs": {
                    "pixels": ["10", 0],
                    "vae": ["4", 2]
                },
                "class_type": "VAEEncode",
                "_meta": {
                    "title": "VAE编码"
                }
            }
        }
    }

    # 打印请求的 JSON 数据
    # print(f"Sending request for {image_filename}:")
    # print(json.dumps(payload, ensure_ascii=False, indent=2))  # 打印 JSON 数据

    # 发送 POST 请求
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # 抛出异常如果请求失败
        print(f"Processed {image_filename}: {response.json()}")  # 打印响应
    except requests.exceptions.RequestException as e:
        print(f"Error processing {image_filename}: {e}")

print("All images have been processed.")
