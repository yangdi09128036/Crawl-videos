# B站视频爬取工具 (Python + Requests + MoviePy)

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Requests](https://img.shields.io/badge/Requests-2.26%2B-green)
![MoviePy](https://img.shields.io/badge/MoviePy-1.0%2B-red)

一个基于 Python 的 Bilibili 视频下载工具，可以爬取 B 站视频并自动合并音视频流。

## 功能特性

- 支持单个视频下载
- 支持分P视频自动合并
- 自动识别视频清晰度
- 保留视频封面和元信息
- 支持自定义下载路径
- 自动处理网络请求头

## 快速开始

### 安装依赖

```bash
pip install requests moviepy
```

### 下载脚本

1. 直接下载脚本文件：
```bash
wget https://raw.githubusercontent.com/yangdi09128036/Crawl-bilibili-videos/main/bilibili_downloader.py
```

2. 或者克隆整个仓库：
```bash
git clone https://github.com/yangdi09128036/Crawl-bilibili-videos.git
cd Crawl-bilibili-videos
```

### 使用方法

```bash
python bilibili_downloader.py [视频BV号或完整URL]
```

示例：
```bash
python bilibili_downloader.py BV1GJ411x7h7
# 或
python bilibili_downloader.py https://www.bilibili.com/video/BV1GJ411x7h7
```

## 配置说明

### 获取必要请求头信息

1. 登录B站后，打开开发者工具 (F12)
2. 切换到"网络"(Network)选项卡
3. 刷新页面并点击任意一个请求
4. 复制以下信息：
   - `Cookie`
   - `Referer`
   - `User-Agent`

### 修改脚本配置

打开 `bilibili_downloader.py` 文件，找到以下部分并替换为你的信息：

```python
HEADERS = {
    'User-Agent': '你的User-Agent',
    'Referer': 'https://www.bilibili.com/',
    'Cookie': '你的Cookie'
}
```

## 常见问题

### 下载失败怎么办？

1. 检查你的网络连接
2. 更新请求头信息 (Cookie/User-Agent/Referer)
3. 尝试降低视频质量
4. 检查B站是否有反爬机制更新

### 音视频不同步怎么办？

1. 确保安装了最新版 MoviePy
2. 尝试重新下载
3. 可能是原始视频问题，可尝试其他视频测试

### 如何批量下载？

可以配合Shell脚本使用：
```bash
#!/bin/bash
for bv in BV1xx BV2xx BV3xx; do
    python bilibili_downloader.py $bv
done
```

## 免责声明

1. 本项目仅用于学习交流
2. 请勿用于商业用途
3. 下载内容请遵守B站用户协议
4. 过度频繁请求可能导致账号被封禁

## 更新计划

- [ ] 增加多线程下载支持
- [ ] 添加GUI界面
- [ ] 支持UP主全部视频批量下载
- [ ] 增加下载进度显示

## 开发者信息

- 作者: yangdi09128036
- 邮箱/QQ: 3349476867@qq.com
- 仓库: [GitHub](https://github.com/yangdi09128036/Crawl-bilibili-videos)

## 许可证

[MIT License](LICENSE)

---

**温馨提示**：请合理使用本工具，尊重视频创作者版权，下载内容仅限个人学习使用。
