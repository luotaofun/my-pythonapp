# _*_ coding : utf-8 _*_
# @Time : 2025/3/24 16:39
# @Author : luotao
# @File : urllibDemo
# @Project pythonDemo
import math
import random
import urllib.request
import urllib.parse
from lxml import etree
import os


# https://u001.25img.com/?p=1&search2=eelja3lfe1a1&search=%E5%90%88%E9%9B%86
# https://u001.25img.com/?p=2&search2=eelja3lfe1a1&search=%E5%90%88%E9%9B%86
# https://u001.25img.com/?p=3&search2=eelja3lfe1a1&search=%E5%90%88%E9%9B%8
def create_request(page):
    url_base = 'https://u001.25img.com/?'
    # 请求参数字典
    requestParam = {
        'p': page,
        'search2': 'eelja3lfe1a1',
        'search': '合集'
    }
    queryParam = urllib.parse.urlencode(requestParam)  # 将请求参数编码成查询字符串(URL编码，即%+十六进制)
    url = url_base + queryParam
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
        "Cache-Control": "max-age=0",
        "Cookie": "JSESSIONID=5E51C36C2E604BB3FCC6A6646920D35E",
        "Referer": "https//u001.25img.com/?search2=eelja3lfe1a1&search=%E5%90%88%E8%AE%A1",
        "User-Agent":
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
    }
    request = urllib.request.Request(url=url, headers=headers)  # 创建请求对象
    return request


def get_content(request,proxies_pool):
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
                content = b''.join(response.readlines()).decode('utf-8')  # 读取所有行并连接成字节字符串并解码
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

def write_to_mysql(result_data):
    import datetime
    import pandas as pd
    from sqlalchemy import create_engine, inspect
    from sqlalchemy.sql.expression import text  # 用于构建SQL语句
    # obj = json.load(open(json_file, 'r', encoding='utf-8')) # 读取本地json
    # obj = json.loads(content)  # 反序列化，即将json字符串转换为Python对象
    # matches = jsonpath.jsonpath(obj, "$.data.*")
    # print(matches, type(matches), sep="\n")

    

    # 创建结果DataFrame
    result_df = pd.DataFrame(result_data,columns=result_data[0].keys())
    # df.index.name = "id"  # 重命名索引
    # df.index = df.index + 1  # id索引从1开始
    # print(f"前几行==>\n{df.head()}")1
    print(f"（行数，列数）==> {result_df.shape}")
    print(f"结果数据==>\n{result_df}")

    file_path = (
        f".output/u3c3_crawlspider{str(datetime.datetime.now().strftime('%Y%m%d'))}.xlsx"
    )
    result_df.to_excel(file_path,index=False) # index=False 表示不保存索引

    # 连接MySQL数据库
    conn_str = "mysql+mysqlconnector://root:kuroneko.678@127.0.0.1:3306/spider"
    engine = create_engine(conn_str)
    
    # 创建result表的SQL语句
    create_table_sql = text(
        """
        CREATE TABLE IF NOT EXISTS u3c3_crawlspider (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            magnet text NOT NULL,
            usize VARCHAR(50) NOT NULL,
            udate DATE NOT NULL,
            udetail VARCHAR(255) NOT NULL,
            utorrent VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """
    )
    
    # 连接数据库并写入数据
    try:
        with engine.connect() as conn:
            with conn.begin() as transaction:
                # # 检查表是否存在，存在则追加，否则替换
                if inspect(engine).has_table("u3c3_crawlspider"):
                    new_ids = result_df.index.tolist()
                    # delete_sql = text(f"DELETE FROM ydtest.movie WHERE id IN ({','.join(map(str, new_ids))})")
                    delete_sql = text("TRUNCATE TABLE u3c3_crawlspider ")
                    print(delete_sql)
                    conn.execute(delete_sql)
                    result_df.to_sql(name="u3c3_crawlspider", con=engine, if_exists="append")
                else:
                    conn.execute(create_table_sql)
                    result_df.to_sql(name="u3c3_crawlspider", con=engine, if_exists="append", index=False)
                    print(conn.execute(text("show create table u3c3_crawlspider")).first()[1])
                
                # 获取写入的数据条数
                count = conn.execute(text("SELECT COUNT(*) FROM u3c3_crawlspider")).scalar()
                print(f"成功写入数据条数: {count}")
    except Exception as e:
        print(f"写入数据库失败: {e}")

def download(page, content,result_data):
    # with open(str(page) + '.html','w',encoding='utf-8') as fp:
    #     fp.write(content)
    tree = etree.HTML(content)  # 将响应数据解析为HTML树，并返回HTML树对象tree
    utitle_list = tree.xpath('/html/body/div[12]/div[2]/table/tbody/tr/td[2]/a[1]/@title')  # 标题
    usize_list = tree.xpath('/html/body/div[12]/div[2]/table/tbody/tr/td[4]/text()')  # 内存大小
    udate_list = tree.xpath('/html/body/div[12]/div[2]/table/tbody/tr/td[5]/text()')  # 发布时间
    utorrent_list = tree.xpath('/html/body/div[12]/div[2]/table/tbody/tr/td[3]/a[1]/@href')  # 种子链接
    udetail_list = tree.xpath('/html/body/div[12]/div[2]/table/tbody/tr/td[2]/a[1]/@href')  # 详情链接

    baselink = 'https://u001.25img.com'
    headers = {

        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
        "Cache-Control": "max-age=0",
        "Cookie": "JSESSIONID=5E51C36C2E604BB3FCC6A6646920D35E",
        "Referer": "https//u001.25img.com/?search2=eelja3lfe1a1&search=%E5%90%88%E8%AE%A1",
        "User-Agent":
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
    }
    for i in range(len(utitle_list)):
        title = utitle_list[i].strip()
        if i<=1 or title == "":
            continue
        udate = udate_list[i][:10]
        usize = usize_list[i]
        utorrent = baselink + utorrent_list[i]
        udetail = baselink + udetail_list[i]
        filename = f'./u3c3Down/{udate}{title.replace(' ', '').replace('/', '')}{usize.replace('.', '·')}.torrent'

        request = urllib.request.Request(udetail, headers=headers)
        with urllib.request.urlopen(request) as response:  # 模拟浏览器向服务器发送请求
            handler = urllib.request.HTTPHandler
            opener = urllib.request.build_opener(handler)
            response = opener.open(request, timeout=10)
            content = b''.join(response.readlines())  # 读取所有行并连接成字节字符串
        magnet = etree.HTML(content).xpath('//div[contains(@class, "panel-footer")]//a[contains(@href, "magnet:?")]/@href')[0]
        # print(f'正在下载剩余【{len(utitle_list)-i}】==>' + utorrent)
        # try:
        #     request = urllib.request.Request(utorrent, headers=headers)
        #     with urllib.request.urlopen(request) as response:  # 模拟浏览器向服务器发送请求
        #         proxies_pool = [
        #             {'http': '59.54.238.213:15611'},
        #             # {'http':'117.42.94.98:18739'},
        #         ]
        #         proxies = random.choice(proxies_pool)
        #         handler = urllib.request.ProxyHandler(proxies=proxies)
        #         opener = urllib.request.build_opener(handler)
        #         response = opener.open(request, timeout=10)
        #         content = b''.join(response.readlines())  # 读取所有行并连接成字节字符串
        #         output_path='./u3c3Down'
        #         if not os.path.exists(output_path):
        #             os.makedirs(output_path)
        #         filename = f'{output_path}/{title}{usize}@{udate}.torrent'
        #         with open(filename, 'wb') as fp:  # 使用'wb'模式写入二进制数据
        #             fp.write(content)
        # except urllib.error as e:
        #     print(f"下载失败: {e}")
        result_data.append({
            "title" : title, # 标题
            "udate" : udate,  # 发布时间
            "usize" : usize, # 内存大小
            "utorrent" : utorrent,  # 种子链接
            "udetail" :udetail,  # 详情链接
            "magnet" : magnet # 磁力链接
        })
    return result_data

if __name__ == '__main__':
    start_page = int(input('请输入起始的页码:'))
    end_page = int(input('请输入结束的页码:'))
    proxies_pool = [
        # {'http': '59.54.238.213:15611'},
        {"http": "117.42.94.76:19820"},
    ]
    result_data=[]
    for page in range(start_page, end_page + 1):
        #         每页都创建请求对象
        request = create_request(page)
        
        #       获取响应数据
        content = get_content(request,None)
        download(page, content,result_data)
    write_to_mysql(result_data)
