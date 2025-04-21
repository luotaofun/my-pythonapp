import requests
from bs4 import BeautifulSoup
import time
import random
import re
import json
import os

# 基础配置（需定期更新）
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Referer': 'https://www.pornhub.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'DNT': '1',
    # 如需通过年龄验证可添加cookie（需手动获取）
    # 'Cookie': 'age_verified=1;'
}


def extract_video_url(html_content):
    """从视频页面提取最高清MP4直链"""
    try:
        # 方法1：从flashvars提取媒体信息
        flashvars_match = re.search(r'var\s+flashvars\s*=\s*({.*?});', html_content, re.DOTALL)
        if flashvars_match:
            flashvars = json.loads(flashvars_match.group(1))
            media_definitions = flashvars.get('mediaDefinitions', [])

            valid_medias = []
            for media in media_definitions:
                if media.get('format') == 'mp4' and media.get('videoUrl'):
                    try:
                        video_url = media['videoUrl'].replace('\\/', '/')
                        quality = int(media.get('quality', 0))
                        valid_medias.append((quality, video_url))
                    except:
                        continue

            if valid_medias:
                valid_medias.sort(reverse=True)
                return valid_medias[0][1]

        # 方法2：直接搜索MP4链接
        mp4_links = re.findall(r'(https?://[^"\']+\.mp4)', html_content)
        if mp4_links:
            return max(mp4_links, key=lambda x: int(re.search(r'(\d+)p', x).group(1)) if re.search(r'(\d+)p', x) else 0)

    except Exception as e:
        print(f"解析视频链接时出错: {str(e)}")

    return None


def download_video(url, filename, headers):
    """带进度显示的流式下载"""
    try:
        with requests.get(url, headers=headers, stream=True, timeout=30) as response:
            response.raise_for_status()

            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            start_time = time.time()

            os.makedirs('videos', exist_ok=True)
            filepath = os.path.join('videos', filename)

            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        # 进度显示
                        if total_size > 0:
                            progress = downloaded / total_size * 100
                            speed = downloaded / (time.time() - start_time) / 1024
                            print(f"\r下载进度: {progress:.2f}% | 速度: {speed:.2f} KB/s", end='')

            print(f"\n视频已保存至: {filepath}")
            return True
    except Exception as e:
        print(f"\n下载失败: {str(e)}")
        return False


def fetch_video_links(max_links=10):
    """采集视频页面链接（原功能优化）"""
    collected = set()
    page = 1
    delay_range = (1.5, 3.0)

    while len(collected) < max_links:
        try:
            url = f"https://www.pornhub.com/video?page={page}"
            time.sleep(random.uniform(*delay_range))

            response = requests.get(
                url,
                headers=headers,
                timeout=15,
                allow_redirects=False
            )

            if response.status_code != 200:
                print(f"终止：收到 {response.status_code} 响应")
                break

            if "verify" in response.url:
                print("触发反爬验证机制")
                break

            soup = BeautifulSoup(response.text, 'html.parser')
            link_container = soup.find_all('a', class_='linkVideoThumb')

            if not link_container:
                print("页面结构已变更，终止执行")
                break

            for link in link_container:
                if href := link.get('href', ''):
                    if '/view_video.php?' in href:
                        full_url = f"https://www.pornhub.com{href}"
                        collected.add(full_url)

                        if len(collected) >= max_links:
                            return list(collected)[:max_links]

            page += 1

        except Exception as e:
            print(f"请求异常: {str(e)}")
            break

    return list(collected)[:max_links]


def main():
    print("警告：本代码仅用于技术研究演示")

    # 采集视频页面链接
    video_links = fetch_video_links(max_links=3)
    print(f"\n成功采集到 {len(video_links)} 个视频链接")

    # 下载视频
    for idx, page_url in enumerate(video_links):
        print(f"\n处理第 {idx + 1} 个视频: {page_url}")

        try:
            # 获取视频页面
            time.sleep(random.uniform(1.5, 3.0))
            response = requests.get(page_url, headers=headers, timeout=15)
            if response.status_code != 200:
                print(f"页面请求失败: {response.status_code}")
                continue

            # 提取视频直链
            video_url = extract_video_url(response.text)
            if not video_url:
                print("未找到有效视频链接")
                continue
            print(f"解析到视频地址: {video_url}")

            # 配置下载headers
            download_headers = headers.copy()
            download_headers['Referer'] = page_url

            # 生成文件名
            viewkey = re.search(r'viewkey=([\w]+)', page_url).group(1)
            filename = f"video_{viewkey}.mp4"

            # 开始下载
            print("开始下载...")
            if download_video(video_url, filename, download_headers):
                print("下载成功！")
            else:
                print("下载失败")

        except Exception as e:
            print(f"处理视频时出错: {str(e)}")


if __name__ == "__main__":
    main()