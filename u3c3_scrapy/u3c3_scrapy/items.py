# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class U3C3ScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field() # 标题
    udate = scrapy.Field()  # 发布时间
    usize = scrapy.Field() # 内存大小
    utorrent = scrapy.Field()  # 种子链接
    udetail =scrapy.Field()  # 详情链接
    
    # 给 FilesPipeline 使用的字段
    file_urls = scrapy.Field()      # 需要下载的文件URL列表
    files = scrapy.Field()          # FilesPipeline 在成功下载文件后会自动填充这个字段，包含下载文件的信息

