import scrapy
from pathlib import Path
import datetime
import time


class ZhipinSpider(scrapy.Spider):
    name = "zhipin"
    allowed_domains = ["www.zhipin.com"]
    start_urls = ["https://www.zhipin.com/web/geek/jobs?city=101280600&query=erp"]
    
    custom_headers = {
            "sec-ch-ua": '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7",
        # "Cookie": "... HARDCODED COOKIE REMOVED ..." # Remove or comment out the hardcoded Cookie here
    }

    def _format_cookies(self, selenium_cookies):
        """将 Selenium cookies (list of dict) 转换为 Scrapy cookies (dict)."""
        if not selenium_cookies:
            return {}
        scrapy_cookies = {cookie['name']: cookie['value'] for cookie in selenium_cookies}
        return scrapy_cookies

    def test(self,proxies_pool=None,url_base=start_urls[0],headers=custom_headers):
        """ 测试反爬 """
        import datetime
        import json
        import random
        import requests
        from pathlib import Path

        # 请求参数字典
        requestParam = {
        }
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        ]
        headers["User-Agent"] = random.choice(
            user_agents
        )  # 动态切换 User-Agent,避免被目标网站识别为爬虫

        # 目标输出
        output_dir = Path(".output")
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{timestamp}"

        # Session 对象会在底层重用 TCP 连接（通过连接池机制），减少每次请求时重新建立连接的开销，从而提升性能。
        # 在多次 HTTP 请求之间，Session 对象可以自动保存并复用 cookies。
        # 如果第一次请求登录成功后服务器返回了一个 session cookie，那么后续使用同一个 Session 对象发起的请求都会自动带上这个 cookie。
        session = requests.session()
        print(f"session==>{session}\n{type(session)}")
        # proxies_pool=[{"http":"117.42.94.76:19820"}]
        if proxies_pool:
            while proxies_pool:
                try:
                    proxies = random.choice(proxies_pool)
                    response = session.get(
                        url=url_base,
                        params=requestParam,
                        headers=headers,
                        proxies=proxies,
                        timeout=10,
                    )  # 发送get请求
                    # response = session.post(url=url_base,data=requestParam,headers=headers,proxies=proxies) # 发送post请求
                except Exception as e:
                    print(f"请求失败，代理 {proxies} 失效: {e}")
                    proxies_pool.remove(proxies)  # 移除失效的代理
                print("所有代理均失效，请检查代理池")
                return None
        else:
            response = session.get(
                url=url_base, params=requestParam, headers=headers
            )  # 发送get请求
            # response = session.post(url=url_base,data=requestParam,headers=headers) # 发送post请求
        try:
            response.encoding = "utf-8"
            print(f"状态码==>{response.status_code}")
            print(f"响应头==>{response.headers}")
            print(f"二进制网页源码==>{response.content}")
            # 尝试解析 JSON 为python的数据结构
            data = response.json()
            json_str = json.dumps(data, ensure_ascii=False, indent=4)
            print(f"序列化为json字符串==>{json_str}")
            with open(output_dir / f"{output_filename}.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                print(f"json 已保存到 {output_dir / output_filename}.json")
            return data
        except json.JSONDecodeError:
            # 不是 JSON 格式
            print(f"网页源码==>{response.text}")
            with open(output_dir / f"{output_filename}.html", "w", encoding="utf-8") as f:
                f.write(response.text)
                print(f"html 已保存到 {output_dir / output_filename}.html")
            return response.text
        except Exception as e:
            print(f"请求失败，代理 {proxies} 失效: {e}")
            return None

    def setup_driver(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.common.exceptions import NoSuchElementException, JavascriptException, WebDriverException
        """初始化并返回 Selenium WebDriver 实例。"""
        try:
            driver_path = Path("D:\workspace\python-projects\my-pythonapp\crawler\chromedriver.exe").resolve()
            if not driver_path.exists():
                print(f"错误：ChromeDriver 未找到：{driver_path}")
                print("请下载与您的 Chrome 浏览器版本匹配的 ChromeDriver 并放置在 crawler 目录下。")
                return None
            service = Service(executable_path=str(driver_path))
            # 可以添加选项，例如无头模式 (不显示浏览器界面)
            options = webdriver.ChromeOptions()
            # options.add_argument('--headless')
            options.add_argument('--disable-gpu') # 在无头模式下有时需要
            browser = webdriver.Chrome(service=service, options=options)
            # browser = webdriver.Chrome(service=service)
            print("WebDriver 初始化成功。")
            return browser
        except WebDriverException as e:
            print(f"初始化 WebDriver 时出错: {e}")
            if "This version of ChromeDriver only supports Chrome version" in str(e):
                print("错误：ChromeDriver 版本与 Chrome 浏览器版本不兼容。请下载匹配的版本。")
            return None
        except Exception as e:
            print(f"初始化 WebDriver 时发生未知错误: {e}")
            return None

    def get_cookie(self,driver,url,cookie_file_name):
        from selenium import webdriver
        import time
        import json
        driver.get(url)
        print("请在打开的浏览器窗口中手动登录...")
        # 进入网页之后，手动点击登录页码快速登录进去
        # 增加等待时间以便手动登录
        time.sleep(60)
        print("尝试获取 Cookies...")
        #在60s之内登录，获取所有cookie信息(返回是list of dict)
        dictCookies = driver.get_cookies()
        if not dictCookies:
            print("未能获取到 Cookies，请确保已成功登录。")
            return None

        #是将list of dict转化成str格式
        jsonCookies = json.dumps(dictCookies)
        # 登录完成后,自动创建一个boss直聘.json的文件，将cookies保存
        output_dir = Path(".output")
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{timestamp}_{cookie_file_name}"
        cookie_file_path = output_dir / output_filename
        try:
            with open(cookie_file_path, "w") as fp:
                fp.write(jsonCookies)
                print(f'Cookies 保存成功！==>{cookie_file_path}')
            return dictCookies # 返回获取到的 Cookies
        except Exception as e:
            print(f"保存 Cookies 时出错: {e}")
            return None # 保存失败也返回 None

    def start_requests(self):
        driver = None # Initialize driver to None
        try:
            driver = self.setup_driver()
            if not driver:
                self.logger.error("Selenium WebDriver 启动失败")
                return # Stop if driver failed

            # Get cookies using Selenium (this will involve manual login)
            selenium_cookies_list = self.get_cookie(
                driver=driver, url=self.start_urls[0], cookie_file_name='boss直聘.json'
            )

            # Format cookies for Scrapy
            scrapy_cookies = self._format_cookies(selenium_cookies_list)

            if not scrapy_cookies:
                 self.logger.warning("未能获取到有效 Cookies，请求可能失败或数据不完整。")
                 # Decide whether to proceed without cookies or stop
                 # return # Uncomment to stop if cookies are essential

            # Now yield Scrapy requests using the obtained cookies
            self.logger.info(f"使用 {len(scrapy_cookies)} 个 Cookies 发起请求...")
            for url in self.start_urls:
                yield scrapy.Request(
                    url,
                    headers=self.custom_headers, # Headers without the hardcoded cookie
                    cookies=scrapy_cookies,      # Pass formatted cookies here
                    callback=self.parse
                )

        except Exception as e:
            self.logger.error(f"start_requests 中发生错误: {e}", exc_info=True)
        finally:
            # Ensure the driver is closed even if errors occur
            if driver:
                try:
                    driver.quit()
                    self.logger.info("Selenium WebDriver 已关闭。")
                except Exception as e:
                     self.logger.error(f"关闭 Selenium WebDriver 时出错: {e}")

    def parse(self, response):
        # 保存网页源码
        page_source = response.text
        output_dir = Path(".output")
        output_dir.mkdir(parents=True, exist_ok=True)
        output_filename = (
            f"{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}_page_source_{response.status}.html"
        )
        with open(output_dir / output_filename, "w", encoding="utf-8") as f:
            f.write(page_source)
        self.logger.info(f"网页源码已保存到: {output_dir / output_filename}")


        # 这里添加你的数据提取逻辑
        # job_list = response.css('...') # Example
        # for job in job_list:
        #     item = {...}
        #     yield item
        pass 
