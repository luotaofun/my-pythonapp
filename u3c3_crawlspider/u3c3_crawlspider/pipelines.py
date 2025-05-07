# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class U3C3CrawlspiderPipeline:
    def open_spider(self, spider):
        """spider 之前执行"""
        self.fp = open("u3c3.json", "w", encoding="utf-8")

    def process_item(self, item, spider):
        import json

        # print(type(item))
        json_str = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False, indent=4)
        self.fp.write(json_str)
        # print(f"已保存json文件: u3c3.json")
        return item

    def close_spider(self, spider):
        """spider 结束之后执行"""
        self.fp.close()


class U3C3ScrapyPipelineUtorrentDown:
    """自定义下载utorrent"""

    def process_item(self, item, spider):
        import urllib.request

        utorrent = item.get("utorrent")
        title = item.get("title")
        usize = item.get("usize")
        udate = item.get("udate")
        filename = f"{title.replace("/", "")}{usize.replace(".", "·")}@{udate}.torrent"
        import os

        # 创建输出目录
        output_path = ".output"
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        filepath = os.path.join(output_path, filename)  # 拼接完整的文件保存路径
        urllib.request.urlretrieve(utorrent, filepath)
        return item


from scrapy.utils.project import get_project_settings  # 获取settings.py
class MysqlPipeline:
    """持久化到MySQL"""

    def open_spider(self, spider):
        """spider 之前执行"""
        settings = get_project_settings()
        self.host = settings["DB_HOST"]
        self.port = settings["DB_PORT"]
        self.user = settings["DB_USER"]
        self.password = settings["DB_PASSWORD"]
        self.dbname = settings["DB_NAME"]
        self.charset = settings["DB_CHARSET"]
        # 在读取配置后，调用 connect 方法建立连接和创建游标
        self.connect()

    def connect(self):
        import pymysql

        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.dbname,
            charset=self.charset,
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # 构建SQL语句，使用参数化查询防止SQL注入
        # 检查表是否存在，不存在则创建
        create_table_sql = '''
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
        '''
        self.cursor.execute(create_table_sql)
        self.conn.commit()
        
        # 插入数据
        sql = 'INSERT INTO u3c3_crawlspider(title, udate, udetail, usize, utorrent,magnet) VALUES (%s, %s, %s, %s, %s, %s)'
        # 执行SQL语句
        self.cursor.execute(sql, (item["title"], item["udate"], item["udetail"], item["usize"], item["utorrent"], item["magnet"]))
        # 提交事务
        self.conn.commit()
        return item

    def close_spider(self, spider):
        """spider 结束之后执行"""
        self.cursor.close()
        self.conn.close()
