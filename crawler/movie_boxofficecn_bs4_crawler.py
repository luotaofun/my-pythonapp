"""
 _*_ coding : utf-8 _*_
 @Time : 2025-04-22 14:12
 @Author : luotao
 @File : movie_boxofficecn_bs4_crawler.py
 @Description : 
    pip install bs4
    pip install lxml
    pip install jsonpath
    pip install urllib3 
    pip install pandas
    pip install sqlalchemy
    pip install mysql-connector-python
    pip install pymysql
"""
import datetime
import random
import re
import urllib.request
from lxml import etree
import os
from bs4 import BeautifulSoup 
import json
import pandas as pd
import pymysql
from sqlalchemy import create_engine, inspect,text

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
    """ 使用 BeautifulSoup 解析 HTML 内容。 """
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
    """ 使用 XPath 解析 HTML 内容。 """
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
            box_office.pop(i)

        
        # 创建单部电影的信息字典
        movie_info = {
            "电影名称": name,           # 电影名称
            "上映年份": year,          # 上映年份
            "制片地区": region,        # 制片地区
            "评分": rating,        # 评分
            "导演": director_text,   # 导演
            "票房": box_office_value, # 票房
            "提交人": submitter      # 提交人
        }
        
        
        # 将当前电影信息添加到总列表中
        movie_list.append(movie_info)

    # print(movie_list)
    # 序列化为 JSON 字符串并保存
    json_str = json.dumps(movie_list, ensure_ascii=False) # 序列化才能写入：把内存中的数据转换为字节序列。ensure_ascii=False表示非 ASCII 字符保持原样

    # 保存json
    download(json_str,'./.output/movie_boxofficecn_xpath.json')

    # pandas数据处理
    columns = ["电影名称","上映年份", "制片地区", "评分", "导演",  "票房", "提交人"]
    create_table_sql = text(
        """
        CREATE TABLE `movie` (
            `id` INT not null ,
            `上映年份` text DEFAULT NULL,
            `制片地区` text DEFAULT NULL,
            `导演` text DEFAULT NULL,
            `提交人` text DEFAULT NULL,
            `电影名称` text DEFAULT NULL,
            `票房` text DEFAULT NULL,
            `评分` text DEFAULT NULL,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8
        """
    )
    print(movie_list, type(movie_list), sep="\n")
    df = pd.DataFrame(movie_list,columns=columns)
    df.index.name = "id"  # 重命名索引
    df.index = df.index + 1  # id索引从1开始
    # 创建国家代码到中文名称的映射字典
    country_code_to_chinese_name = {
        '🇨🇳': '中国',
        '🇺🇸': '美国',
        '🇮🇳': '印度',
        '🇯🇵': '日本',
        '🇫🇷': '法国',
        '🇬🇧': '英国',
        '🇫🇮': '芬兰',
        '🇦🇺': '澳大利亚',
        '🇱🇧': '莱索托'
    }
    df['制片地区'] = df['制片地区'].map(country_code_to_chinese_name).fillna(df['制片地区']) #.不能映射的 NaN 值会替换为原始 制片地区 列中的对应值。
    print(f"前几行==>\n{df.head()}")
    print(f"（行数，列数）==> {df.shape}")

    # 保存excel
    file_path = (
        f".output/yingdaomovie{str(datetime.datetime.now().strftime('%Y%m%d'))}.xlsx"
    )
    df.to_excel(file_path,index=False) # index=False 表示不保存索引

    conn_str = "mysql+mysqlconnector://root:kuroneko.678@127.0.0.1:3306/ydtest?charset=utf8mb4"
    engine = create_engine(
        conn_str
    )  # 创建sqlalchemy对象连接mysql,禁用 SQLAlchemy 在执行 SQL 语句时的输出
    with engine.connect() as conn:
        with conn.begin() as transaction:
            # # 检查表是否存在，存在则追加，否则替换
            if inspect(engine).has_table("movie"):
                # new_ids = df.index.tolist()
                # delete_sql = text(f"DELETE FROM ydtest.movie WHERE id IN ({','.join(map(str, new_ids))})")
                delete_sql = text("TRUNCATE TABLE ydtest.movie ")
                print(delete_sql)
                conn.execute(delete_sql)
                print(df.dtypes)
                print(df['制片地区'].unique())
                df.to_sql(name="movie", con=engine, if_exists="append")
            else:
                conn.execute(create_table_sql)
                df.to_sql(name="movie", con=engine, if_exists="append", index=True)
                print(conn.execute(text("show create table ydtest.movie")).first()[1])
            print(
                f"写入数据条数：{conn.execute(text('select count(id) from ydtest.movie ')).first()[0]}"
            )

    return json_str


if __name__ == "__main__":
# def main(args):
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
    output_path = "./.output"
    current_date = str(datetime.datetime.now().strftime('%Y%m%d'))
    file_path = f'{output_path}/movie{current_date}_bs4.json'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    download(content,file_path)

    # bs4解析数据
    # json_result = parse_content_bs4(content)
    # download(json_result,file_path)

    # xpath解析数据
    parse_content_xpath(content)

