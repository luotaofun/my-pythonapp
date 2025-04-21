# @Author : luotao
import math
import datetime
import random
import re
import urllib.request
import urllib.parse
from lxml import etree
import os
from bs4 import BeautifulSoup 
import json
import jsonpath

def create_request(page):
    baseurl = "http://www.boxofficecn.com/the-red-box-office"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Referer": "http://www.boxofficecn.com/",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7",
    }
    request = urllib.request.Request(url=baseurl, headers=headers)  # 创建请求对象
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
                response = opener.open(request, timeout=10)  # 设置超时时间
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

def download(content,file_path):
    with open(file_path, "w", encoding='utf-8') as fp:  # 使用'w'模式写入文本数据
        fp.write(content)
def parse_to_json(json_file):
    try:
        # if os.path.exists(json_file):
        # obj = json.load(open(json_file, 'r', encoding='utf-8')) # 读取本地json
        obj = json.loads(json_file) # 反序列化，即将json字符串转换为Python对象
        # matches  = jsonpath.jsonpath(obj,'$..regionName')
        # 提取匹配结果
        # result = [match.value for match in matches]
        # print(matches)
        return obj
    except Exception as e:
        print(f"解析文件时发生错误: {e}")

def parse_content_bs4(content):
    soup = BeautifulSoup(content, "lxml")
    # //*[@id="tablepress-4"]/tbody/tr/td[2]/text()
    movie_name_with_rating = soup.select('#tablepress-4 tbody tr td:nth-of-type(2)') 
    release_year_with_region = soup.select('#tablepress-4 tbody tr td:first-child') 
    director = soup.select('#tablepress-4 tbody tr td:nth-of-type(3)') 
    box_office = soup.select('#tablepress-4 tbody tr td:nth-of-type(4)') 
    submitter = "luotaofun"

    movie_list = []
    for i in range(len(movie_name_with_rating)):
        # 提取电影名称和评分
        name_rating_text = movie_name_with_rating[i].get_text(strip=True) #获取单元格中的文本内容，并去除首尾空白字符。
        name_match = re.match(r'(.+?)\（(\d+\.\d+)\）', name_rating_text) 
        if name_match:
            name = name_match.group(1).strip() # (.+?)匹配任意字符（除了换行符），至少匹配一次。
            rating = name_match.group(2).strip() # (\d+\.\d+)\）匹配形如 x.y 的浮点数评分
        else:
            name = name_rating_text.strip()
            rating = None
        
        # 提取上映年份和地区
        year_region_text = release_year_with_region[i].get_text(strip=True)
        year_region_match = re.match(r'(\d{4})\s*(.*)', year_region_text)
        
        if year_region_match:
            year = year_region_match.group(1).strip() # (\d{4})匹配恰好 4 位数字的年份
            region = year_region_match.group(2).strip() # \s*:匹配零个或多个空白字符（包括空格、制表符等）用于处理年份和地区的间隔。(.*):匹配任意字符（除了换行符），提取地区信息。
        else:
            year = None
            region = None
        
        # 提取导演
        director_text = director[i].get_text(strip=True)
        
        # 提取票房并清理非数字字符
        box_office_text = box_office[i].get_text(strip=True)
        numeric_data = ''.join(filter(str.isdigit, box_office_text)) # #将筛选出的数字字符拼接成一个连续的字符串
        if numeric_data:
            box_office_value = int(numeric_data)
        else:
            box_office_value = None
        
        # 创建单部电影的信息字典
        movie_info = {
            "name": name,           # 电影名称
            "year": year,          # 上映年份
            "region": region,        # 制片地区
            "rating": rating,        # 评分
            "director": director_text,   # 导演
            "box_office": box_office_value, # 票房
            "submitter": submitter      # 提交人
        }
        
        # 将当前电影信息添加到总列表中
        movie_list.append(movie_info)
        
    # print(movie_list)
    # 序列化为 JSON 字符串并保存
    json_result = json.dumps(movie_list, ensure_ascii=False,indent=4) # 序列化才能写入：把内存中的数据转换为字节序列。ensure_ascii=False表示非 ASCII 字符保持原样
    return json_result
    
def parse_content_xpath(content):
    tree = etree.HTML(content)  # 将响应数据解析为HTML树，并返回HTML树对象tree
    movie_name_with_rating = [text.strip() for text in tree.xpath('//*[@id="tablepress-4"]/tbody/tr/td[2]/text()') if text.strip()]  # 电影名称
    release_year_with_region = tree.xpath(
        '//*[@id="tablepress-4"]/tbody/tr/td[1]/text()'
    )  # 上映年份
    director = tree.xpath('//*[@id="tablepress-4"]/tbody/tr/td[3]/text()')  # 导演
    box_office = tree.xpath('//*[@id="tablepress-4"]/tbody/tr/td[4]//text()')  # 票房
    submitter = "luotaofun"  # 提交人
    
    movie_list = []
    for i in range(len(movie_name_with_rating)):
        # 提取电影名称和评分
        name_rating_text = movie_name_with_rating[i].strip() #获取单元格中的文本内容，并去除首尾空白字符。
        name_match = re.match(r'(.+?)\（(\d+\.\d+)\）', name_rating_text) 
        if name_match:
            name = name_match.group(1).strip() # (.+?)匹配任意字符（除了换行符），至少匹配一次。
            rating = name_match.group(2).strip() # (\d+\.\d+)\）匹配形如 x.y 的浮点数评分
        else:
            name = name_rating_text.strip()
            rating = None
        
        # 提取上映年份和地区
        year_region_text = release_year_with_region[i].strip()
        year_region_match = re.match(r'(\d{4})\s*(.*)', year_region_text)
        
        if year_region_match:
            year = year_region_match.group(1).strip() # (\d{4})匹配恰好 4 位数字的年份
            region = year_region_match.group(2).strip() # \s*:匹配零个或多个空白字符（包括空格、制表符等）用于处理年份和地区的间隔。(.*):匹配任意字符（除了换行符），提取地区信息。
        else:
            year = None
            region = None
        
        # 提取导演
        director_text = director[i].strip()
        
        # 提取票房并清理非数字字符
        box_office_text = box_office[i].strip()
        numeric_data = ''.join(filter(str.isdigit, box_office_text)) # #将筛选出的数字字符拼接成一个连续的字符串
        if numeric_data:
            box_office_value = int(numeric_data)
        else:
            box_office_value = None
        
        # 创建单部电影的信息字典
        movie_info = {
            "name": name,           # 电影名称
            "year": year,          # 上映年份
            "region": region,        # 制片地区
            "rating": rating,        # 评分
            "director": director_text,   # 导演
            "box_office": box_office_value, # 票房
            "submitter": submitter      # 提交人
        }
        
        # 将当前电影信息添加到总列表中
        movie_list.append(movie_info)

    # 序列化为 JSON 字符串并保存
    json_result = json.dumps(movie_list, ensure_ascii=False) # 序列化才能写入：把内存中的数据转换为字节序列。ensure_ascii=False表示非 ASCII 字符保持原样
    return json_result


if __name__ == "__main__":
    page = 1
    #         每页都创建请求对象
    request = create_request(page)
    proxies_pool = [
        # {'http': '59.54.238.213:15611'},
        {"http": "117.42.94.76:19820"},
    ]
    #       获取响应数据
    # content = get_content(request, proxies_pool)
    content = get_content(request,False)

    # 保存数据
    output_path = "./bs4"
    current_date = str(datetime.datetime.now().strftime('%Y%m%d'))
    file_path = f'{output_path}/movie{current_date}.json'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    download(content,file_path)

    # bs4解析数据
    json_result = parse_content_bs4(content)
    download(json_result,'./movie_boxofficecn_bs4.json')

    # xpath解析数据
    download(parse_content_xpath(content),'./movie_boxofficecn_xpath.json')
