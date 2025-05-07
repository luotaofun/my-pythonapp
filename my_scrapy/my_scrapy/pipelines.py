# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyScrapyPipeline:
    def open_spider(self,spider):
        """ spider 之前执行 """
        self.fp = open("zhipin.json","a",encoding="utf-8")
    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item
    
    def close_spider(self,spider):
        """ spider 结束之后执行 """
        self.fp.close()

class zhipin_pipeline:
    def process_item(self, item, spider):
        import urllib.request
        print(item)
        # url=item.get('')
        # filename=item.get('')
        # urllib.request.urlretrieve(url,filename)
        return item