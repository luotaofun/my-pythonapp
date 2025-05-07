import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from u3c3_crawlspider.items import U3C3CrawlspiderItem  # 引入自定义的 U3C3CrawlspiderItem 类
import os
import urllib.parse
from scrapy_playwright.page import PageMethod # 导入 PageMethod 用于等待元素
from scrapy.exceptions import CloseSpider # 提前停止爬虫

class U3c3Spider(CrawlSpider):
    name = "u3c3"
    allowed_domains = ["u001.25img.com"]

    search_params = {
        "search2":"eelja3lfe1a1",
        "search": "合集"
    }
    start_page = 1 

    rules = (
        # 规则 1: 处理翻页, 定位 "下一页" 链接
        # 当 CrawlSpider 处理第一页响应时，此规则会找到第二页链接
        # 然后调用 parse_page 处理第二页的响应
        Rule(
            LinkExtractor(
                restrict_xpaths='//ul[@id="pageLimit"]//a[contains(@title, "Go to next page")]'
            ),
            process_request='process_playwright_request', # 确保每页请求使用 Playwright
            callback='parse_item',
            follow=True
        ),
        # # 规则 2: 处理详情页链接，在详情页提取数据
        # Rule(
        #     LinkExtractor(
        #         restrict_xpaths='' # 详情页链接
        #     ),
        #     callback='parse_udetail', # 指定处理详情页的回调函数
        #     follow=False # 详情页是终点，不需要再跟进
        # ),
    )
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

    def process_playwright_request(self, request, response):
        """
        确保由 Rule 生成的每页请求也使用 Playwright。
        """
        request.meta.update({
            "playwright": True,
            "playwright_page_methods": [
                PageMethod("wait_for_selector", "ul#pageLimit li", state="attached"), 
            ],
        })
        return request

    def start_requests(self):
        """
        生成初始请求 (第1页), 不指定 callback, 让 Rule 处理第一页响应。
        """
        print(f"开始爬取，搜索词: '{self.search_params.get('search', '')}'")
        request_params = self.search_params.copy()
        request_params["p"] = self.start_page
        query_string = urllib.parse.urlencode(request_params)
        url = "https://u001.25img.com/?" + query_string
        print(f"生成初始请求 URL: {url}")# https://u001.25img.com/?search=spermmania&p=1
        yield scrapy.Request(
            url=url,
            headers=self.custom_headers,
            meta={
                "playwright": True, # <-- 启用 Playwright 处理这个请求
                
                "playwright_page_methods": [
                    # 明确告诉 Playwright 等待分页元素出现再返回响应，确保了 JS 有足够时间执行完毕
                    PageMethod("wait_for_selector", "ul#pageLimit li", state="attached"),
                ],
            },
            # 去掉 callback, 让 CrawlSpider 的 Rule 来处理第一页响应
        )

    # def parse_page(self, response):
    #     """
    #     处理第 2 页及后续页面的响应。
    #     负责计数、检查停止条件、提取数据以及手动生成下一页请求。
    #     """
    #     self.page_count += 1 # 计数器增加 (第2页时为1, 第3页时为2, ...)

    #     # 尝试从 URL 获取页码（用于日志）
    #     page_num_str = 'unknown'
    #     try:
    #         parsed_url = urllib.parse.urlparse(response.url)
    #         query_params = urllib.parse.parse_qs(parsed_url.query)
    #         if 'p' in query_params:
    #             page_num_str = query_params['p'][0]
    #     except Exception as e:
    #         print(f"错误: 无法从URL解析页码 {e}")

    #     print(f"--- 处理第 {self.page_count + 1} 页 (计数: {self.page_count}, URL页码: {page_num_str}) --- URL: {response.url}")

    #     # --- 在这里添加从列表页提取数据的逻辑 --- 
    #     print(f"正在从第 {self.page_count + 1} 页提取数据...")
    #     self.parse_item
    #     # ---------------------------------------

    #     # 检查是否达到最大页数限制 (因为计数从0开始，第10页时 page_count 为 9)
    #     if self.page_count >= self.max_pages:
    #         print(f"已达到最大页面数 ({self.max_pages})，关闭爬虫。")
    #         raise CloseSpider(f"已达到最大页面数，关闭爬虫: {self.max_pages}")

    #     # --- 手动查找并请求下一页 --- 
    #     # 在当前页面响应中查找"下一页"链接
    #     next_page_links = LinkExtractor(
    #         restrict_xpaths='//ul[@id="pageLimit"]//a[contains(@title, "Go to next page")]'
    #     ).extract_links(response)

    #     if next_page_links:
    #         next_page_url = next_page_links[0].url
    #         print(f"找到下一页链接: {next_page_url}")
    #         # 手动生成下一页请求
    #         next_request = scrapy.Request(
    #             url=next_page_url,
    #             headers=self.custom_headers, 
    #             callback=self.parse_page, # 递归调用自身处理下一页
    #             meta={
    #                 "playwright": True, # 手动添加 Playwright meta
    #                 "playwright_page_methods": [
    #                     PageMethod("wait_for_selector", "ul#pageLimit li", state="attached"),
    #                 ],
    #             }
    #         )
    #         yield next_request
    #     else:
    #         print(f"在第 {self.page_count + 1} 页未找到下一页链接")

    def parse_item(self, response):
        print(f'===============正在解析  {response.url} ===============\n')
        """
        解析服务器返回的响应。
        """
        # 保存页面源码用于调试
        # output_path = '.output'
        # if not os.path.exists(output_path):
        #     os.makedirs(output_path)
        # filename = f'debug_{self.name}_{response.url.split("p=")[-1].split("&")[0]}.html'
        # filepath = os.path.join(output_path, filename) # 拼接完整的文件保存路径
        # try:
        #     with open(filepath, "w",encoding='utf-8') as f:
        #         f.write(response.text)
        #     self.logger.info(f"@=================>页面源码已保存到 {filepath}")
        # except Exception as e:
            # self.logger.error(f"保存源码失败 for {response.url}: {e}")

        # print(f'@=================>{response.url}')

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
        for i in range(len(utitle_list)):
            if i<=1:
                continue
        # for i in range(6):
            title = utitle_list[i].strip()
            if title == "":
                continue
            udate = udate_list[i][:10]
            usize = usize_list[i]
            utorrent = baselink + utorrent_list[i]
            udetail = baselink + udetail_list[i]

            # 请求详情页，并将已有数据通过 cb_kwargs 传递
            yield scrapy.Request(
                url=udetail,
                headers=self.custom_headers,
                callback=self.parse_detail,
                cb_kwargs={
                    'title': title,
                    'udate': udate,
                    'usize': usize,
                    'utorrent': utorrent,
                    'udetail': udetail,
                },
                meta={
                    "playwright": True,
                    "playwright_page_methods": [
                        # 等待磁力链接出现 
                        PageMethod("wait_for_selector", 'a[href^="magnet:"]', state="attached"),
                    ],
                }
            )

    def parse_detail(self, response, title, udate, usize, utorrent, udetail):
        # print(f'{response.url} {title}\n')
        """
        解析详情页，提取磁力链接，并生成最终的 Item。
        接收来自 parse_item 通过 cb_kwargs 传递的参数。
        """
        # 提取磁力链接
        magnet = response.xpath(
            '//div[contains(@class, "panel-footer")]//a[contains(@href, "magnet:?")]/@href' 
        ).get() # 使用 get() 获取单个结果或 None
        # 创建完整的 Item
        item = U3C3CrawlspiderItem(
            title=title,
            udate=udate,
            usize=usize,
            utorrent=utorrent,
            udetail=udetail,
            magnet=magnet.strip() if magnet else magnet, # 去掉可能的空白符
        )
        # 可以通过 FilesPipeline 下载 torrent 文件
        item["file_urls"] = [utorrent]

        
        yield item  # 将 Item 发送给 Pipeline 处理


        