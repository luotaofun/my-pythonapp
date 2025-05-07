"""
_*_ coding : utf-8 _*_
@Time : 2025-04-23 17:52
@Author : luotao
@File : yingdaoapi_urllib_crawler.py
@Description :
   pip install sqlalchemy
   pip install mysql-connector-python

    -- 统计每个国家的总票房
    CREATE TEMPORARY TABLE IF NOT EXISTS temp_country_boxoffice AS
    SELECT 
        `制片地区` AS `信息`,
        SUM(`票房`) AS `票房总数`
    FROM 
        `movie`
    GROUP BY 
        `制片地区`;

    -- 获取票房总数最高的三个国家
    SELECT * FROM temp_country_boxoffice
    ORDER BY `票房总数` DESC
    LIMIT 3;

    -- 创建临时表来存储评分区间
    CREATE TEMPORARY TABLE IF NOT EXISTS temp_rating_boxoffice AS
    SELECT 
                CASE 
                        WHEN CAST(`评分` AS CHAR) IS NULL OR TRIM(`评分`) = '' OR TRIM(`评分`) = '-' THEN '无评分'
                        WHEN CAST(`评分` AS DOUBLE) >= 3.0 AND CAST(`评分` AS DOUBLE) <= 3.5 THEN '3.0-3.5'
                        WHEN CAST(`评分` AS DOUBLE) >= 9.0 AND CAST(`评分` AS DOUBLE) <= 9.5 THEN '9.0-9.5'
                        ELSE '其他'
                END AS `评分区间`,
                `票房`
        FROM 
                `movie` ORDER BY 评分区间
            
            
    -- 统计每个评分区间的总票房
    CREATE TEMPORARY TABLE IF NOT EXISTS temp_rating_boxoffice_summary AS
    SELECT 
        `评分区间` AS `信息`,
        SUM(`票房`) AS `票房总数`
    FROM 
        temp_rating_boxoffice
    WHERE 
        `评分区间` IN ('3.0-3.5', '9.0-9.5', '无评分')
    GROUP BY 
        `评分区间`;

    -- 将评分区间票房总数的结果插入 result 表
    INSERT INTO `result` (`提交人`, `信息`, `票房总数`)
    SELECT 
        'luotaofun' AS `提交人`,
        `信息`,
        `票房总数`
    FROM 
        temp_rating_boxoffice_summary;

    -- 查询 result 表以验证结果
    SELECT * FROM `result`;
"""

import datetime
import os
import urllib.request
import random
import json
import jsonpath
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, inspect
from sqlalchemy.sql.expression import text  # 用于构建SQL语句


def create_request():
    urlbase = "https://mock.jsont.run/6zA7NH6ciqxNxGYzKO-Zx"
    headers = {
        "sec-ch-ua": '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
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


def parse_content(content):
    # obj = json.load(open(json_file, 'r', encoding='utf-8')) # 读取本地json
    obj = json.loads(content)  # 反序列化，即将json字符串转换为Python对象
    matches = jsonpath.jsonpath(obj, "$.data.*")
    print(matches, type(matches), sep="\n")
    # 手动指定 DataFrame 的列名
    columns = ["上映年份", "制片地区", "导演", "提交人", "电影名称", "票房", "评分"]
    
    # df = pd.json_normalize(obj) # 将嵌套字典转换为DataFrame
    df = pd.DataFrame(matches, columns=columns)  # 将提取的匹配结果转换为DataFrame
    df.index.name = "id"  # 重命名索引
    df.index = df.index + 1  # id索引从1开始
    print(f"前几行==>\n{df.head()}")
    print(f"（行数，列数）==> {df.shape}")
    
    # 将票房列转换为数值类型
    df['票房'] = pd.to_numeric(df['票房'], errors='coerce')# 当遇到无法解析为数值的值时，将其转换为 NaN。
    
    # 1. 统计票房总数最高的三个国家：SELECT 制片地区 as 信息 ,sum(票房) as 票房总数 FROM movie GROUP BY 制片地区 LIMIT 3
    country_boxoffice = df.groupby('制片地区')['票房'].sum().reset_index() #['票房'].sum(): 对每个分组中的 票房 列进行求和计算每个 制片地区 的总票房。分组操作后，结果的索引会变成 制片地区，使用 .reset_index() 可以将其转换为一个普通的列，同时生成一个新的整数索引。
    top3_countries = country_boxoffice.sort_values('票房', ascending=False).head(3)
    print(f"票房总数最高的三个国家:\n{top3_countries}\n{type(top3_countries)}")
    
    # 2. 统计评分区间的票房总数
    # 创建评分区间列
    def get_rating_range(rating):
        if pd.isna(rating) or rating == '':
            return '无评分'
        try:
            rating = float(rating) # 转换为浮点数类型，以便进行数值比较。
        except ValueError:
            return '无评分'
        if 3.0 <= rating <= 3.5:
            return '3.0-3.5'
        elif 9.0 <= rating <= 9.5:
            return '9.0-9.5'
        else:
            return '其他'
    
    df['评分区间'] = df['评分'].apply(get_rating_range) # 创建新列，将评分转换为对应的评分区间
    
    # 筛选出需要的评分区间
    rating_ranges = ['3.0-3.5', '9.0-9.5', '无评分']
    rating_boxoffice = df[df['评分区间'].isin(rating_ranges)].groupby('评分区间')['票房'].sum().reset_index() # 保留 评分区间 列的值在 rating_ranges 列表中的行，然后对每个分组中的 票房 列进行求和，得到每个评分区间的总票房。
    print(f"评分区间票房总数:\n{rating_boxoffice}\n{type(rating_boxoffice)}")
    
    # 将结果写入MySQL数据库
    write_to_mysql(top3_countries, rating_boxoffice)
    
    return df


def write_to_mysql(top3_countries, rating_boxoffice):
    # obj = json.load(open(json_file, 'r', encoding='utf-8')) # 读取本地json
    # obj = json.loads(content)  # 反序列化，即将json字符串转换为Python对象
    # matches = jsonpath.jsonpath(obj, "$.data.*")
    # print(matches, type(matches), sep="\n")
    # 创建结果DataFrame
    result_data = []
    submitter = 'luotaofun'
    # 添加票房总数最高的三个国家。iterrows() 方法用于逐行遍历 DataFrame，返回一个包含索引和行数据的迭代器。_ 用于忽略索引，row 是当前行的数据。
    for _, row in top3_countries.iterrows():
        print(f"索引: {_}, 行数据: {row},{type(row)}")
        result_data.append({
            '提交人': submitter,
            '信息': row['制片地区'],
            '票房总数': int(row['票房'])
        })
    
    # 添加评分区间票房总数
    for _, row in rating_boxoffice.iterrows():
        result_data.append({
            '提交人': submitter,
            '信息': row['评分区间'],
            '票房总数': int(row['票房'])
        })
    
    # 创建结果DataFrame
    result_df = pd.DataFrame(result_data,columns=['提交人', '信息', '票房总数'])
    # df.index.name = "id"  # 重命名索引
    # df.index = df.index + 1  # id索引从1开始
    # print(f"前几行==>\n{df.head()}")
    print(f"（行数，列数）==> {result_df.shape}")
    print(f"结果数据==>\n{result_df}")

    file_path = (
        f".output/result_df{str(datetime.datetime.now().strftime('%Y%m%d'))}.xlsx"
    )
    result_df.to_excel(file_path,index=False) # index=False 表示不保存索引

    # 连接MySQL数据库
    conn_str = "mysql+mysqlconnector://yingdao:9527@43.143.30.32:3306/ydtest"
    engine = create_engine(conn_str)
    
    # 创建result表的SQL语句
    create_table_sql = text(
        """
        CREATE TABLE IF NOT EXISTS `result` (
            `id` INT AUTO_INCREMENT,
            `提交人` VARCHAR(255) DEFAULT NULL,
            `信息` VARCHAR(255) DEFAULT NULL,
            `票房总数` INT DEFAULT NULL,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8
        """
    )
    
    # 连接数据库并写入数据
    try:
        with engine.connect() as conn:
            with conn.begin() as transaction:
                # # 检查表是否存在，存在则追加，否则替换
                if inspect(engine).has_table("result"):
                    new_ids = result_df.index.tolist()
                    # delete_sql = text(f"DELETE FROM ydtest.movie WHERE id IN ({','.join(map(str, new_ids))})")
                    delete_sql = text("TRUNCATE TABLE result ")
                    print(delete_sql)
                    conn.execute(delete_sql)
                    result_df.to_sql(name="result", con=engine, if_exists="append")
                else:
                    conn.execute(create_table_sql)
                    result_df.to_sql(name="result", con=engine, if_exists="append", index=False)
                    print(conn.execute(text("show create table result")).first()[1])
                
                # 获取写入的数据条数
                count = conn.execute(text("SELECT COUNT(*) FROM result")).scalar()
                print(f"成功写入数据条数: {count}")
    except Exception as e:
        print(f"写入数据库失败: {e}")


if __name__ == "__main__":
    proxies_pool = [
        # {'http': '59.54.238.213:15611'},
        {"http": "117.42.94.76:19820"},
    ]
    # 创建请求对象，获取响应数据
    request = create_request()
    content = get_content(request, proxies_pool)

    # 解析数据并写入数据库
    if content:
        df = parse_content(content)
    else:
        print("获取数据失败")
