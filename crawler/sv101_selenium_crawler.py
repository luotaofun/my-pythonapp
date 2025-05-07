"""
_*_ coding : utf-8 _*_
@Time : 2025-04-23 17:52
@Author : luotao
@Description :
    使用 Selenium 直接从网页提取视频链接。
    需要安装: pip install selenium pandas sqlalchemy mysql-connector-python pymysql 

"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, JavascriptException, WebDriverException
from selenium.webdriver.common.by import By
from pathlib import Path
import datetime 
import json
import pandas as pd


def setup_driver():
    """初始化并返回 Selenium WebDriver 实例。"""
    try:
        driver_path = Path("crawler/chromedriver.exe").resolve()
        if not driver_path.exists():
            print(f"错误：ChromeDriver 未找到：{driver_path}")
            print("请下载与您的 Chrome 浏览器版本匹配的 ChromeDriver 并放置在 crawler 目录下。")
            return None
        service = Service(executable_path=str(driver_path))

        # 配置无头模式
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # 无头模式
        options.add_argument('--disable-gpu')  # 禁用 GPU 加速（在某些系统上需要）
        options.add_argument('--window-size=1920x1080')  # 设置窗口大小
        browser = webdriver.Chrome(service=service, options=options)
        # browser = webdriver.Chrome(service=service)
        print("WebDriver 初始化成功。")
        return browser
    except WebDriverException as e:
        print(f"初始化 WebDriver 时出错: {e}")
        return None
    except Exception as e:
        print(f"初始化 WebDriver 时发生未知错误: {e}")
        return None

def parse_content_with_selenium(driver, url):
    if not driver:
        print("错误：WebDriver 未成功初始化，无法解析。")
        return None

    print(f"正在加载页面: {url} ...")

    driver.get(url)
    time.sleep(2) 
    element = driver.find_element(By.XPATH,'//mediaelementwrapper[@id="audio_player"]/audio[@id="audio_player_html5"]')
    linke = element.get_attribute('src')
    title = element._parent.title
    data = []
    data.append({
        title:linke
    })
    data = json.dumps(data, indent=2, ensure_ascii=False) # 序列化为json字符串
    print(data,type(data)) # <class 'str'>

    

    return None 


if __name__ == "__main__":
    # target_url = input("请输入目标URL: ")
    target_url = 'https://sv101.fireside.fm/198'

    # 1. 初始化 WebDriver
    driver = setup_driver()

    if driver:
        try:
            # 2. 使用 WebDriver 加载并解析页面获取链接
            hub_list = parse_content_with_selenium(driver, target_url)
            

            
        finally:
            # 4. 关闭浏览器（无论成功失败都应关闭）
            print("\n操作完成，正在关闭浏览器...")
            try:
                driver.quit()
                print("浏览器已关闭。")
            except Exception as e:
                print(f"关闭浏览器时出错: {e}")

