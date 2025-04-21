# _*_ coding : utf-8 _*_
# @Time : 2025/3/24 16:39
# @Author : luotao
# @File : urllibDemo
# @Project pythonDemo
import urllib.request
import  urllib.parse
import datetime
import re
import json


# https://cn.govopendata.com/xinwenlianbo/20250325/
def create_request(page):
    url_base = 'https://cn.govopendata.com/xinwenlianbo/'
    url = url_base +  page
    headers = {
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
    }
    request = urllib.request.Request(url=url,headers=headers) # 创建请求对象
    return request

def get_content(request):
    response = urllib.request.urlopen(request) # 模拟浏览器向服务器发送请求
    content = b''.join(response.readlines()).decode('utf-8')  # 读取所有行并连接成字节字符串并解码
    return content


def download(page,content):
    with open(str(page) + '.html','w',encoding='utf-8') as fp:
        fp.write(content)

def extract_article_body(html_content):
    # 使用正则表达式匹配 <script type="application/ld+json"> 标签的内容
    script_pattern = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.DOTALL)
    script_match = script_pattern.search(html_content)

    if script_match:
        script_content = script_match.group(1)
        # 解析 JSON 数据
        try:
            json_data = json.loads(script_content)
            # 提取 articleBody 字段的内容
            article_body = json_data.get('articleBody', '')
            if not article_body or article_body.strip() == '':
                # print("Article body is empty")
                raise Exception("Article body is empty")
            return article_body
        except json.JSONDecodeError as e:
            print(f"JSON 解析错误: {e}")
            return None
    else:
        print("未找到 <script type='application/ld+json'> 标签")
        return None

if __name__ == '__main__':
        # current_date = str(datetime.datetime.now().strftime('%Y%m%d'))
        current_date = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y%m%d')) # 昨天
        page = str(current_date)
#         每页都创建请求对象
        request = create_request(page)
#       获取响应数据
        content = get_content(request)
#       下载保存
        download(page,content)
        # 提取 articleBody 内容
        article_body = extract_article_body(content)
        if article_body:
            prompt = ('以下为【' + current_date + '新闻文字稿】我的需求是将这篇较长的新闻稿件总结成适合发布到小红书等社交平台的内容，并且要求按照一定的格式进行整理，同时确保信息专业可靠、积极正能量，你需要对原文进行梳理分析和总结然后进行格式化输出。对于小贴士部分，你会根据信息内容，提供一些针对内容透露出来的商机或者机会，你会给出一些关键词。，增加内容的附加值。在输出之前，你会对整理好的内容进行检查，确保没有遗漏或错误，保证内容的质量。\n'
                      + article_body)
            download('article-' + page ,prompt)
