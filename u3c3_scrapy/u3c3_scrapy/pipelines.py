# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class U3C3ScrapyPipeline:
    def open_spider(self,spider):
        """ spider 之前执行 """
        self.fp = open("u3c3.json","w",encoding="utf-8")
        print(f">>>>>>>>>>>>>>保存json文件: u3c3.json")
    def process_item(self, item, spider):
        import json
        print(type(item))
        json_str = json.dumps(ItemAdapter(item).asdict(),ensure_ascii=False,indent=4)
        self.fp.write(json_str)
        return item
    
    def close_spider(self,spider):
        """ spider 结束之后执行 """
        self.fp.close()


class U3C3ScrapyPipelineUtorrentDown:
    """ 自定义下载utorrent """
    def process_item(self, item, spider):
        import urllib.request
        utorrent = item.get('utorrent')
        title = item.get('title')
        usize = item.get('usize')
        udate = item.get('udate')
        filename = f'{title}{usize}@{udate}.torrent'
        import os
        # 创建输出目录
        output_path = '.output'
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        filepath = os.path.join(output_path, filename) # 拼接完整的文件保存路径
        urllib.request.urlretrieve(utorrent,filepath)
        return item
