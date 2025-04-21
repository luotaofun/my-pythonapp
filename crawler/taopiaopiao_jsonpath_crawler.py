import datetime
import os
import urllib.request
import random
import json
import jsonpath

def create_request():
    urlbase='https://www.taopiaopiao.com/cityAction.json?activityId&_ksTS=1745138158355_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
    headers={
        "sec-ch-ua-platform": '"Windows"',
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
        "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
        "sec-ch-ua": '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "bx-v": "2.5.28",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.taopiaopiao.com/?spm=a1z21.3046609.city.5.1e59112aB1cogs&tbpm=3&city=440300",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7",
        "Cookie": 'cna=wJ+LIN1DMyoCAQAAAACsptu2; xlly_s=1; tb_city=440300; tb_cityName="ye7b2g=="; isg=BA8PUzVTuwJcVr_-oI0Mn0yxnqMZNGNWc9GFECEcwX6F8C_yKQQmpkvu8yDOvTvO',
    }
    request=urllib.request.Request(url=urlbase,headers=headers)# 创建请求对象
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

def download(content,file_path):
    with open(file_path, "w", encoding='utf-8') as fp:  # 使用'w'模式写入文本数据
        fp.write(content)

def parse_content(json_file):
    try:
        # if os.path.exists(json_file):
        # obj = json.load(open(json_file, 'r', encoding='utf-8')) # 读取本地json
        obj = json.loads(json_file) # 反序列化，即将json字符串转换为Python对象
        matches  = jsonpath.jsonpath(obj,'$..regionName')
        # 提取匹配结果
        # result = [match.value for match in matches]
        print(matches)
    except Exception as e:
        print(f"解析文件时发生错误: {e}")

if __name__ == '__main__':
    proxies_pool = [
        # {'http': '59.54.238.213:15611'},
        {"http": "117.42.94.76:19820"},
    ]
    # 创建请求对象，获取响应数据
    request = create_request()
    content = get_content(request,proxies_pool)
    # content = content.replace('jsonp109(', '').replace(');', '')
    content_json = content.split('jsonp109(')[1].split(');')[0]

    # 保存数据
    output_path = "./taopiaopiao"
    current_date = str(datetime.datetime.now().strftime('%Y%m%d'))
    file_path = f'{output_path}/taopiaopiao{current_date}.json'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    download(content_json,file_path)

    # 解析数据
    parse_content(content_json)