from bs4 import BeautifulSoup

import datetime
import os
import urllib.request
import random
import json
import jsonpath


def create_request():
    urlbase = "http://www.boxofficecn.com/the-red-box-office"
    headers = {
        "sec-ch-ua-platform": '"Windows"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
        "sec-ch-ua": '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "Accept": "*/*",
        "Origin": "http://www.boxofficecn.com",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "http://www.boxofficecn.com/",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7",
    }
    request = urllib.request.Request(url=urlbase, headers=headers)  # 创建请求对象
    return request


def get_content(request, proxies_pool):
    if proxies_pool:
        while proxies_pool:
            # response = urllib.request.urlopen(request) # 模拟浏览器向服务器发送请求
            # 用opener对象来发送请求并获取响应。
            # handler = urllib.request.HTTPHandler
            proxies = random.choice(proxies_pool)  # 随机代理IP
            # print(proxies)
            handler = urllib.request.ProxyHandler(proxies=proxies)
            opener = urllib.request.build_opener(handler)
            try:
                response = opener.open(request)
                content = b"".join(response.readlines()).decode(
                    "utf-8"
                )  # 读取所有行并连接成字节字符串并解码
                return content
            except Exception as e:
                print(f"请求失败，代理 {proxies} 失效: {e}")
                proxies_pool.remove(proxies)  # 移除失效的代理
        print("所有代理均失效，请检查代理池。")
        return None
    else:
        try:
            response = urllib.request.urlopen(request, timeout=10)
            content = b"".join(response.readlines()).decode("utf-8")
            return content
        except Exception as e:
            print(f"请求失败: {e}")
            return None


def download(content, file_path):
    with open(file_path, "w", encoding="utf-8") as fp:  # 使用'w'模式写入文本数据
        fp.write(content)


def parse_content(html_file):
    try:
        # matches  = jsonpath.jsonpath(obj,'$..regionName')
        # # 提取匹配结果
        # # result = [match.value for match in matches]
        soup = BeautifulSoup(open(html_file,  encoding="utf-8"),'lxml')
    except Exception as e:
        print(f"解析文件时发生错误: {e}")


if __name__ == "__main__":
    proxies_pool = [
        # {'http': '59.54.238.213:15611'},
        {"http": "218.87.205.110:20718"},
    ]
    # 创建请求对象，获取响应数据
    request = create_request()
    content = get_content(request, False)

    # 保存数据
    output_path = "./bs4"
    current_date = str(datetime.datetime.now().strftime("%Y%m%d"))
    file_path = f"{output_path}/bs4{current_date}.html"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    download(content, file_path)

    # 解析数据
    parse_content(content)
