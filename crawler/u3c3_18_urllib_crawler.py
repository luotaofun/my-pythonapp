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
        # 'search': '合集'
        # 'search': 'G-quenen'
        'search': 'spermmania'
        
    }
    queryParam = urllib.parse.urlencode(requestParam)  # 将请求参数字典编码为查询字符串
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


def download(page, content):
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
        title = utitle_list[i].replace(' ', '').replace('/', '')
        udate = udate_list[i][:10]
        usize = usize_list[i].replace('.', '·')
        utorrent = baselink + utorrent_list[i]
        udetail = baselink + udetail_list[i]
        filename = f'./u3c3Down/{udate}{title}{usize}.torrent'
        print(f'正在下载剩余【{len(utitle_list)-i}】==>' + utorrent)
        try:
            request = urllib.request.Request(utorrent, headers=headers)
            with urllib.request.urlopen(request) as response:  # 模拟浏览器向服务器发送请求
                proxies_pool = [
                    {'http': '59.54.238.213:15611'},
                    # {'http':'117.42.94.98:18739'},
                ]
                proxies = random.choice(proxies_pool)
                handler = urllib.request.ProxyHandler(proxies=proxies)
                opener = urllib.request.build_opener(handler)
                response = opener.open(request, timeout=10)
                content = b''.join(response.readlines())  # 读取所有行并连接成字节字符串
                output_path='./u3c3Down'
                if not os.path.exists(output_path):
                    os.makedirs(output_path)
                filename = f'{output_path}/{title}{usize}@{udate}.torrent'
                with open(filename, 'wb') as fp:  # 使用'wb'模式写入二进制数据
                    fp.write(content)
        except urllib.error as e:
            print(f"下载失败: {e}")


if __name__ == '__main__':
    start_page = int(input('请输入起始的页码:'))
    end_page = int(input('请输入结束的页码:'))
    proxies_pool = [
        # {'http': '59.54.238.213:15611'},
        {"http": "117.42.94.76:19820"},
    ]
    for page in range(start_page, end_page + 1):
        #         每页都创建请求对象
        request = create_request(page)
        
        #       获取响应数据
        content = get_content(request,proxies_pool)
        #       下载保存
        download(page, content)
