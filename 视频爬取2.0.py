import requests
import re
import json
import os
from moviepy import VideoFileClip, AudioFileClip

# 输入视频链接
url = input("请输入需要下载的视频链接: ")

cookie = '31274bc7,1757595684,a49aa*32CjDNlWHKVKk8htQafHeIhJKaad9P-IcZg3s8jKEOdY-kP0dWjfLCkNueUpNLRk3_VKYSVmJiU2hlZ3U0eWt6V1ZmTmNhTklFYVE1LXc1dkhBbHI0OTRtSHJQRUFfWVVGUEtnamdjN3pHY3dDMzRfMldyTzRabDF0djE2LTJkS3owQ0VYVDdGaTNBIIEC'
headers = {
    "Referer": url,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Cookie": cookie
}

response = requests.get(url=url, headers=headers)
html = response.text

# 提取视频标题
title = re.findall('title="(.*?)"', html)[0]
print("视频标题:", title)

# 处理文件名，去除非法字符
def sanitize_filename(filename):
    # 替换非法字符为下划线
    return re.sub(r'[\\/*?:"<>|]', '_', filename)

title = sanitize_filename(title)

# 提取视频信息
info = re.findall('window.__playinfo__=(.*?)</script>', html)[0]
json_data = json.loads(info)

# 提取视频和音频链接
video_url = json_data['data']['dash']['video'][0]['baseUrl']
audio_url = json_data['data']['dash']['audio'][0]['baseUrl']

# 获取视频和音频内容
video_content = requests.get(url=video_url, headers=headers).content
audio_content = requests.get(url=audio_url, headers=headers).content

# 指定保存路径
video_save_path = r"D:\PythonProject\src\crawler-data\video"
audio_save_path = r"D:\PythonProject\src\crawler-data\audio"
final_video_path = r"D:\PythonProject\src\crawler-data\full-video"

# 创建保存目录
os.makedirs(video_save_path, exist_ok=True)
os.makedirs(audio_save_path, exist_ok=True)
os.makedirs(final_video_path, exist_ok=True)

# 保存视频和音频文件
video_file_path = os.path.join(video_save_path, f'{title}_video.mp4')
audio_file_path = os.path.join(audio_save_path, f'{title}_audio.mp3')

with open(video_file_path, 'wb') as f:
    f.write(video_content)

with open(audio_file_path, 'wb') as f:
    f.write(audio_content)

# 合并视频和音频
video_clip = VideoFileClip(video_file_path)
audio_clip = AudioFileClip(audio_file_path)

final_clip = video_clip.with_audio(audio_clip)
final_clip.write_videofile(os.path.join(final_video_path, f'{title}.mp4'))

# 关闭资源
video_clip.close()
audio_clip.close()
final_clip.close()

print(title+"视频下载并合并完成!")