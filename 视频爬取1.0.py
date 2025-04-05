import requests
from moviepy import VideoFileClip, AudioFileClip

# 获取视频
video_url = input("请输入视频的URL地址：")
video_headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 CrKey/1.54.250320 Edg/134.0.0.0',
    'referer': 'https://www.bilibili.com/video/BV1FfQHYeEJ1/?vd_source=dce854820523dcf87fdf889a507362af'
}
video_response = requests.get(video_url, headers=video_headers)
open("视频.mp4", "wb").write(video_response.content)

# 获取音频
audio_url = input("请输入音频的URL地址：")
if not audio_url.startswith(('http://', 'https://')):
    raise ValueError("音频URL不合法，请确保包含http://或https://协议")
audio_headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 CrKey/1.54.250320 Edg/134.0.0.0',
    'referer': 'https://www.bilibili.com/video/BV1FfQHYeEJ1/?vd_source=dce854820523dcf87fdf889a507362af'
}
audio_response = requests.get(audio_url, headers=audio_headers)
open("音频.mp3", "wb").write(audio_response.content)

# 拼接视频和音频
video = VideoFileClip('视频.mp4')
audio = AudioFileClip('音频.mp3')

# 使用 set_audio 方法合并音频和视频
final_video = video.with_audio(audio)

final_video.write_videofile("完整的视频.mp4")

print("视频和音频拼接完成！")