import os
import requests
from urllib.parse import urlparse

# 创建目录来存储图片
image_dir = r"C:\Users\ymlt\Desktop\sinofuse-distributor-site\assets\images"
os.makedirs(image_dir, exist_ok=True)

# 定义要下载的图片URL列表
image_urls = [
    "https://sinofuse.elec-distributor.com/assets/images/team/technical-team.jpg",
    "https://sinofuse.elec-distributor.com/assets/images/blog/ev-fuse-selection.jpg",
]

# 下载图片
for url in image_urls:
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # 从URL中提取文件名
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        # 如果没有文件名，使用默认名称
        if not filename:
            filename = "image.jpg"
            
        # 保存图片
        file_path = os.path.join(image_dir, filename)
        with open(file_path, 'wb') as f:
            f.write(response.content)
            
        print(f"已下载: {filename}")
        
    except Exception as e:
        print(f"下载失败 {url}: {str(e)}")

print("图片下载完成")