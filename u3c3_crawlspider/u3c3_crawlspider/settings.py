# Scrapy settings for u3c3_crawlspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "u3c3_crawlspider"

SPIDER_MODULES = ["u3c3_crawlspider.spiders"]
NEWSPIDER_MODULE = "u3c3_crawlspider.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "u3c3_crawlspider (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "u3c3_crawlspider.middlewares.U3C3CrawlspiderSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "u3c3_crawlspider.middlewares.U3C3CrawlspiderDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# 日志配置
# LOG_LEVEL = "WARNING"
# LOG_LEVEL = "DEBUG"
LOG_LEVEL = "INFO"
LOG_FILE = "u3c3_crawlspider.log" # 日志文件
AUTOTHROTTLE_DEBUG = True # 可以取消注释这个来看 AutoThrottle 的详细日志

# 数据库配置
DB_HOST='127.0.0.1'
DB_PORT=3306
DB_USER='root'
DB_PASSWORD='kuroneko.678'
DB_NAME='spider' # 数据库名
DB_CHARSET='utf8mb4'
# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "u3c3_crawlspider.pipelines.U3C3CrawlspiderPipeline": 300,
#    "u3c3_crawlspider.pipelines.U3C3ScrapyPipelineUtorrentDown": 301,
   "u3c3_crawlspider.pipelines.MysqlPipeline": 302, # 持久化
}

# --- 添加 Playwright 下载处理器 ---
DOWNLOAD_HANDLERS = {
   "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
   "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
# --- 添加 Twisted Reactor (Playwright 需要 asyncio) ---
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
# --- （可选）配置 Playwright ---
PLAYWRIGHT_BROWSER_TYPE = "chromium"  # 可以是 'firefox' 或 'webkit'
PLAYWRIGHT_LAUNCH_OPTIONS = {         # 比如设置无头模式 (默认就是 True)
    "headless": True,
}
# 增加默认超时时间 (单位：毫秒)，如果页面加载或 JS 执行较慢
PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = 60000 # 设置为 60 秒

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# 启用自动限速扩展 (推荐)
# 它会根据服务器的响应情况自动调整延迟
AUTOTHROTTLE_ENABLED = True
# 起始的下载延迟（秒）
# AUTOTHROTTLE_START_DELAY = 1
# 在高延迟情况下设置的最大下载延迟（秒）
# AUTOTHROTTLE_MAX_DELAY = 90
# Scrapy 应针对的平均请求数。较低的值意味着更保守（更慢）
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:


# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
