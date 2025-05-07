import scrapy
from u3c3_scrapy.items import U3C3ScrapyItem  # 引入自定义的 U3C3ScrapyItem 类
import urllib.parse
import os

class U3c3Spider(scrapy.Spider):

    name = "u3c3"  # # 爬虫名称，用于 scrapy crawl u3c3 启动
    allowed_domains = ["u001.25img.com"]
    start_urls = ["https://u001.25img.com/?"]
    search_params = {
        # "search2": "eelja3lfe1a1",
        # 'search': '合集'
        # 'search': 'G-quenen'
        "search": "spermmania",
    }
    start_page = 1
    end_page = 1
    # 请求头
    custom_headers = {
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
        "Cookie": "JSESSIONID=6EA6C71FCC5CCB52CE748E5C4C86D6A9",
        "Referer": "https//u001.25img.com/?search2=eelja3lfe1a1&search=%E5%90%88%E8%AE%A1"
    }

    def start_requests(self):
        """
        生成初始请求。Scrapy 会自动调用这个方法。
        """
        self.logger.info(f"开始爬取，页面范围: {self.start_page} - {self.end_page}")
        for page in range(self.start_page, self.end_page + 1):
            # 构造每一页的请求参数
            request_params = self.search_params.copy()
            request_params["p"] = page
            query_string = urllib.parse.urlencode(
                request_params
            )  # 将请求参数编码成查询字符串(URL编码，即%+十六进制)
            url = "https://u001.25img.com/?" + query_string
            # https://u001.25img.com/?search=spermmania&p=1
            self.logger.debug(f"生成请求 URL: {url}")
            # 发起请求，并指定回调函数为 parse
            yield scrapy.Request(
                url=url,
                headers=self.custom_headers,
                callback=self.parse,  # 指定处理响应的函数
            )

    def parse(self, response):

        """
        解析服务器返回的响应。
        """
        # 保存页面源码用于调试
        output_path = '.output'
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        filename = f'debug_{self.name}_{response.url.split("p=")[-1].split("&")[0]}.html'
        filepath = os.path.join(output_path, filename) # 拼接完整的文件保存路径
        try:
            with open(filepath, "w",encoding='utf-8') as f:
                f.write(response.text)
            self.logger.info(f"@=================>页面源码已保存到 {filepath}")
        except Exception as e:
            self.logger.error(f"保存源码失败 for {response.url}: {e}")

        utitle_list = response.xpath(
            "/html/body/div[12]/div[2]/table/tbody/tr/td[2]/a[1]/@title"
        ).extract()  # 标题
        usize_list = response.xpath(
            "/html/body/div[12]/div[2]/table/tbody/tr/td[4]/text()"
        ).extract()  # 内存大小
        udate_list = response.xpath(
            "/html/body/div[12]/div[2]/table/tbody/tr/td[5]/text()"
        ).extract()  # 发布时间
        utorrent_list = response.xpath(
            "/html/body/div[12]/div[2]/table/tbody/tr/td[3]/a[1]/@href"
        ).extract()  # 种子链接
        udetail_list = response.xpath(
            "/html/body/div[12]/div[2]/table/tbody/tr/td[2]/a[1]/@href"
        ).extract()  # 详情链接
        baselink = "https://u001.25img.com"
        # for i in range(len(utitle_list)):
        for i in range(6):
            title = utitle_list[i].strip().replace("/", "")
            if title == "":
                continue
            udate = udate_list[i][:10]
            usize = usize_list[i].replace(".", "·")
            utorrent = baselink + utorrent_list[i]
            udetail = baselink + udetail_list[i]
            # 创建 U3C3ScrapyItem 实例
            item = U3C3ScrapyItem(
                title=title,
                udate=udate,
                usize=usize,
                utorrent=utorrent,
                udetail=udetail,
            )
            item["file_urls"] = [
                utorrent
            ]  # 填充 file_urls 字段给 scrapy.pipelines.files.FilesPipeline 下载
            print(f'第{i+1}条===============\n{item}\n')
            yield item  # 将 Item 发送给 Pipeline 处理
