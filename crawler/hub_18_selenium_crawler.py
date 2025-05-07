"""
_*_ coding : utf-8 _*_
@Time : 2025-04-23 17:52
@Author : luotao
@File : yingdaoapi_urllib_crawler.py
@Description :
    使用 Selenium 直接从网页提取视频链接。
    需要安装: pip install selenium pandas sqlalchemy mysql-connector-python pymysql requests
    下载视频需要安装: pip install m3u8 ffmpeg-python
    需要下载与 Chrome 版本匹配的 ChromeDriver: https://chromedriver.chromium.org/downloads
    需要安装 ffmpeg 并添加到系统 PATH: https://ffmpeg.org/download.html
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, JavascriptException, WebDriverException
from pathlib import Path
import datetime 
import json
import pandas as pd
import subprocess
import re


def setup_driver():
    """初始化并返回 Selenium WebDriver 实例。"""
    try:
        driver_path = Path("crawler/chromedriver.exe").resolve()
        if not driver_path.exists():
            print(f"错误：ChromeDriver 未找到：{driver_path}")
            print("请下载与您的 Chrome 浏览器版本匹配的 ChromeDriver 并放置在 crawler 目录下。")
            return None
        service = Service(executable_path=str(driver_path))
        # 可以添加选项，例如无头模式 (不显示浏览器界面)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu') # 在无头模式下有时需要
        browser = webdriver.Chrome(service=service, options=options)
        # browser = webdriver.Chrome(service=service)
        print("WebDriver 初始化成功。")
        return browser
    except WebDriverException as e:
        print(f"初始化 WebDriver 时出错: {e}")
        if "This version of ChromeDriver only supports Chrome version" in str(e):
            print("错误：ChromeDriver 版本与 Chrome 浏览器版本不兼容。请下载匹配的版本。")
        return None
    except Exception as e:
        print(f"初始化 WebDriver 时发生未知错误: {e}")
        return None


def parse_content_with_selenium(driver, url):
    """
    使用 Selenium 加载 URL，并尝试通过执行 JavaScript 提取 1080p (Forced) 视频链接。

    Args:
        driver: 已初始化的 Selenium WebDriver 实例。
        url (str): 要加载和解析的目标网页 URL。

    Returns:
        str or None: 找到的视频链接，如果找不到则返回 None。
    """
    if not driver:
        print("错误：WebDriver 未成功初始化，无法解析。")
        return None

    print(f"正在加载页面: {url} ...")
    try:
        driver.get(url)
        # 等待页面加载一些时间，特别是对于依赖 JavaScript 渲染内容的页面
        # 可以考虑使用更智能的等待方式 (WebDriverWait)，但简单 sleep 也可以先试试
        print("页面初步加载完成，等待几秒让 JavaScript 执行...")
        time.sleep(2) # 等待 2 秒，这个时间可能需要调整

        print("尝试执行 JavaScript 获取播放器变量 (flashvars)...")
        # --- 关键步骤：执行 JavaScript ---
        # 这个 JavaScript 代码尝试找到全局作用域中名字匹配 'flashvars_' 开头的变量
        # 并返回它的值。你需要根据实际页面的 JS 代码调整变量名或查找逻辑。
        js_script = """
        for (var key in window) {
            if (key.startsWith('flashvars_')) {
                // 确保返回的是对象本身，而不是尝试序列化它
                // Selenium 会自动处理 JS 对象到 Python 字典的转换
                console.log('找到变量:', key,window[key],window[key].mediaDefinitions);
                return window[key];
            }
        }
        console.log('未找到以 flashvars_ 开头的变量');
        return null; // 如果找不到，返回 null
        """
        player_data = driver.execute_script(js_script) # Selenium 会自动处理 JS 对象到 Python 字典的转换
        # --------------------------------

        if player_data:
            print("成功通过 JavaScript 获取到播放器数据。结构如下 (部分):")
            # 打印部分数据结构以帮助调试 (避免打印过多内容)
            print(json.dumps(player_data, indent=2, ensure_ascii=False)[:1000] + "...") # 完整打印可能很大
            # limited_data_repr = str(player_data)[:500] + ('...' if len(str(player_data)) > 500 else '')
            # print(limited_data_repr)


            print("\n正在解析数据，查找链接...")
            # --- 在 Python 字典中查找链接 ---
            # 下面的访问路径需要根据上面打印出的实际数据结构进行调整
            media_definitions = player_data.get('mediaDefinitions')
            print(f"{type(media_definitions)}\n{media_definitions}")
            if media_definitions and isinstance(media_definitions, list):
                hub_list=[]
                for media in media_definitions:
                    # .get() 方法更安全，避免因 key 不存在而报错
                    quality = str(media.get('quality', ''))
                    video_url = media.get('videoUrl')
                    format_info = str(media.get('format', '')) 

                    # 打印检查的条目信息，方便调试
                    print(f"  检查: quality='{quality}', format='{format_info}', url_exists={bool(video_url)}")
                    movie_info={
                        "质量":quality,
                        "格式":format_info,
                        "链接":video_url
                    }

                    # 检查条件：质量是 '1080'
                    if quality in ['1080'] and video_url and  format_info:
                        # print(f"\n*** 成功找到链接: {video_url} ***")
                        hub_list.append(movie_info)


                print(hub_list, type(hub_list), sep="\n")
                df = pd.DataFrame(hub_list,columns=movie_info.keys())
                df.index.name = "id"  # 重命名索引
                df.index = df.index + 1  # id索引从1开始。
                print(f"前几行==>\n{df.head()}")
                print(f"（行数，列数）==> {df.shape}")

                # 保存excel
                file_path = (
                    f".output/hub{(datetime.datetime.now().strftime('%Y%m%d'))}.xlsx"
                )
                df.to_excel(file_path,index=False) #

                print(f"\n已经将结果保存到{file_path}")

                return hub_list
            else:
                print("错误：在获取到的数据中未找到 'mediaDefinitions' 列表，或其格式不正确。请检查上面打印的数据结构。")
            # --- 查找结束 ---

        else:
            print("错误：未能通过 JavaScript 获取到播放器数据 (execute_script 返回了 null 或 Falsy 值)。")
            print("可能原因：")
            print("1. 页面加载不完全或 JavaScript 未执行完毕 (尝试增加 time.sleep 时间)。")
            print("2. 包含视频信息的 JavaScript 变量名不是 'flashvars_...' 开头。")
            print("3. 该变量不在全局作用域 (window 对象下)。")
            print("请使用浏览器开发者工具检查目标页面的 JavaScript 代码。")

    except JavascriptException as e:
        print(f"执行 JavaScript 时出错: {e}")
    except WebDriverException as e:
         print(f"与 WebDriver 交互时出错 (可能浏览器已关闭或崩溃): {e}")
    except Exception as e:
        print(f"解析过程中发生未知错误: {e}")

    print("\n未能提取到指定的视频链接。")
    return None # 如果中间出错或没找到，返回 None


def download_m3u8_video(m3u8_url, output_filename=None, quality=None):
    """
    使用FFmpeg从m3u8链接下载视频。
    
    Args:
        m3u8_url (str): m3u8视频流的URL
        output_filename (str, optional): 输出文件名（不含扩展名）。如果未提供，将使用当前时间戳
        quality (str, optional): 视频质量标识，用于文件命名
        
    Returns:
        bool: 下载是否成功
    """
    try:
        # 检查m3u8_url是否有效
        if not m3u8_url or not isinstance(m3u8_url, str):
            print(f"错误：无效链接 - {m3u8_url}")
            return False
            
        # 创建输出目录
        output_dir = Path(".output/videos")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # 设置输出文件名
        if not output_filename:
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            quality_str = f"_{quality}" if quality else ""
            output_filename = f"video{quality_str}_{timestamp}"
        
        output_path = output_dir / f"{output_filename}.mp4"
        
        # 检查FFmpeg是否安装
        try:
            result = subprocess.run(
                ["ffmpeg", "-version"], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                check=True,
                timeout=5
            )
        except (subprocess.SubprocessError, FileNotFoundError) as e:
            print(f"错误：找不到FFmpeg或无法执行。错误信息: {e}")
            print("请确保已安装FFmpeg并添加到系统PATH中。")
            print("下载地址：https://ffmpeg.org/download.html")
            return False
        
        print(f"开始从m3u8链接下载视频...")
        print(f"链接: {m3u8_url}")
        print(f"输出文件: {output_path}")
        
        # 设置更健壮的FFmpeg参数，处理网络问题
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        referer = "https://www.pornhub.com/"
        
        # 构建命令参数列表 - 增加更多网络相关参数
        ffmpeg_cmd = [
            "ffmpeg",
            # 基本HTTP请求设置
            "-user_agent", user_agent,
            "-referer", referer,
            
            # 连接重试设置 - 使用标准支持的参数
            "-reconnect", "1",           # 启用重连
            "-reconnect_streamed", "1",  # 启用流重连
            "-reconnect_delay_max", "20", # 最大重连延迟20秒
            
            # 输入设置 - 放在输入URL之前的参数
            "-i", m3u8_url,
            
            # 输出设置
            "-c", "copy",                # 复制流而不重新编码
            "-bsf:a", "aac_adtstoasc",   # 音频流过滤器
            "-max_muxing_queue_size", "1024", # 增加队列大小处理不同步问题
            "-y",                        # 覆盖现有文件
            str(output_path)             # 输出路径
        ]
        
        print(f"执行命令: {' '.join(ffmpeg_cmd)}")
        
        # 使用subprocess.Popen执行命令
        process = subprocess.Popen(
            ffmpeg_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            errors='replace',
            bufsize=1
        )
        
        # 记录开始时间和文件大小
        start_time = datetime.datetime.now()
        last_progress_time = start_time
        last_frame = 0
        last_file_size = 0 if output_path.exists() else 0
        
        # 实时显示FFmpeg输出
        for line in process.stdout:
            line = line.strip()
            current_time = datetime.datetime.now()
            
            # 显示下载进度
            if "time=" in line:
                # 提取frame数据
                frame_match = None
                if "frame=" in line:
                    frame_match = re.search(r'frame=\s*(\d+)', line)
                
                current_frame = int(frame_match.group(1)) if frame_match else 0
                
                # 提取speed数据
                speed_match = None
                ffmpeg_speed = "N/A"
                if "speed=" in line:
                    speed_match = re.search(r'speed=\s*([\d.]+)x', line)
                    if speed_match:
                        ffmpeg_speed = f"{float(speed_match.group(1)):.2f}x"
                
                # 提取bitrate数据
                bitrate = "N/A"
                if "bitrate=" in line:
                    bitrate_match = re.search(r'bitrate=\s*([\d.]+)kbits/s', line)
                    if bitrate_match:
                        bitrate = f"{float(bitrate_match.group(1)):.1f} kbps"
                
                # 计算下载速度
                current_file_size = output_path.stat().st_size if output_path.exists() else 0
                size_diff_mb = (current_file_size - last_file_size) / (1024 * 1024)  # MB
                
                # 计算时间间隔
                time_diff = (current_time - last_progress_time).total_seconds()
                download_speed = "计算中..."
                
                # 如果过去了3秒或帧数增加了20，更新进度
                if time_diff >= 3 or (current_frame - last_frame) >= 20:
                    elapsed = (current_time - start_time).total_seconds()
                    
                    # 计算下载速度 (MB/s)
                    if time_diff > 0:
                        download_speed = f"{size_diff_mb / time_diff:.2f} MB/s"
                    
                    # 计算已下载大小
                    total_size_mb = current_file_size / (1024 * 1024)
                    
                    # 显示进度和下载信息
                    progress_info = (
                        f"\r下载进度: {line.split('time=')[1].split(' ')[0]} | "
                        f"大小: {total_size_mb:.2f} MB | "
                        f"速度: {download_speed} | "
                        f"FFmpeg处理: {ffmpeg_speed} | "
                        f"码率: {bitrate} | "
                        f"用时: {elapsed:.1f}秒"
                    )
                    print(progress_info, end="")
                    
                    # 更新记录数据
                    last_progress_time = current_time
                    last_frame = current_frame
                    last_file_size = current_file_size
            
            # 特殊处理HTTP 472错误
            elif "HTTP error 472" in line:
                print(f"\n警告: 遇到HTTP 472错误，正在重试连接...")
            
            # 显示其他错误
            elif "error" in line.lower():
                print(f"\n错误: {line}")
        
        process.wait()
        
        # 检查进程返回码和文件大小
        if process.returncode != 0:
            print(f"\n下载失败，FFmpeg返回代码: {process.returncode}")
            return False
            
        # 验证文件是否成功下载（检查文件大小）
        if not output_path.exists() or output_path.stat().st_size < 10000:  # 小于10KB视为下载失败
            print(f"\n下载似乎失败，文件太小或不存在: {output_path}")
            return False
        
        print(f"\n下载完成！视频已保存到: {output_path}")
        print(f"文件大小: {output_path.stat().st_size / (1024*1024):.2f} MB")
        total_time = (datetime.datetime.now() - start_time).total_seconds()
        print(f"总下载时间: {total_time:.1f}秒")
        return True
        
    except Exception as e:
        print(f"下载视频时发生错误: {e}")
        import traceback
        print(traceback.format_exc())  # 打印完整错误堆栈
        return False


def batch_download_videos(hub_list):
    """
    批量下载hub_list中的所有m3u8视频链接。
    
    Args:
        hub_list (list): 包含视频信息的字典列表
        
    Returns:
        dict: 下载结果统计，包含成功和失败的数量
    """
    if not hub_list or not isinstance(hub_list, list):
        print("错误：无效的hub_list")
        return {"成功": 0, "失败": 0}
    
    # 创建结果统计
    results = {"成功": 0, "失败": 0, "总数": len(hub_list)}
    
    # 创建一个时间戳，用于所有文件名
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    
    print(f"\n开始批量下载 {len(hub_list)} 个视频...")
    
    for i, item in enumerate(hub_list):
        if not isinstance(item, dict):
            print(f"错误：无效的数据项 #{i+1}")
            results["失败"] += 1
            continue
        
        url = item['链接']
        quality = item['质量']
        
        if not url:
            print(f"错误：项目 #{i+1} 没有链接")
            results["失败"] += 1
            continue
        
        print(f"\n下载视频 {i+1}/{len(hub_list)} (质量: {quality})...")
        filename = f"{quality}_{timestamp}_{i+1}"
        
        success = download_m3u8_video(url, filename, quality)
        
        if success:
            results["成功"] += 1
        else:
            results["失败"] += 1
    
    # 打印下载统计
    print("\n====== 下载完成 ======")
    print(f"总视频数: {results['总数']}")
    print(f"成功下载: {results['成功']}")
    print(f"下载失败: {results['失败']}")
    
    return results


if __name__ == "__main__":
    # target_url = input("请输入目标URL: ")
    target_url = 'https://cn.pornhub.com/view_video.php?viewkey=67cb7e84988ba'

    # 1. 初始化 WebDriver
    driver = setup_driver()

    if driver:
        try:
            # 2. 使用 WebDriver 加载并解析页面获取链接
            hub_list = parse_content_with_selenium(driver, target_url)
            
            # 3. 批量下载所有视频
            if hub_list:
                print("\n准备批量下载视频...")
                download_results = batch_download_videos(hub_list)
                if download_results["成功"] > 0:
                    print(f"成功下载了 {download_results['成功']} 个视频")
                else:
                    print("没有成功下载任何视频")
            
        finally:
            # 4. 关闭浏览器（无论成功失败都应关闭）
            print("\n操作完成，正在关闭浏览器...")
            try:
                driver.quit()
                print("浏览器已关闭。")
            except Exception as e:
                print(f"关闭浏览器时出错: {e}")

