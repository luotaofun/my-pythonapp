def setup_driver():
    """初始化并返回 Selenium WebDriver 实例。"""
    from pathlib import Path
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.common.exceptions import WebDriverException

    try:
        driver_path = Path("crawler/chromedriver.exe").resolve()
        if not driver_path.exists():
            print(f"错误：ChromeDriver 未找到：{driver_path}")
            print(
                "请下载与您的 Chrome 浏览器版本匹配的 ChromeDriver 并放置在 crawler 目录下。"
            )
            return None
        service = Service(executable_path=str(driver_path))

        # 配置无头模式
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # 无头模式
        options.add_argument("--disable-gpu")  # 禁用 GPU 加速（在某些系统上需要）
        options.add_argument("--window-size=1920x1080")  # 设置窗口大小
        browser = webdriver.Chrome(service=service, options=options)
        # browser = webdriver.Chrome(service=service)
        print("WebDriver 初始化成功。")
        return browser
    except WebDriverException as e:
        print(f"初始化 WebDriver 时出错: {e}")
        return None
    except Exception as e:
        print(f"初始化 WebDriver 时发生未知错误: {e}")
        return None


def get_content(page, proxies_pool):
    import datetime
    import json
    import random
    import requests
    from pathlib import Path

    url_base = "https://u001.25img.com/?"
    # 请求参数字典
    requestParam = {
        "p": page,  # 页码
        "search2": "eelja3lfe1a1",
        "search": "spermmania",
    }
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
        "Cache-Control": "max-age=0",
        "Cookie": "JSESSIONID=5E51C36C2E604BB3FCC6A6646920D35E",
        "Referer": "https//u001.25img.com/?search2=eelja3lfe1a1&search=%E5%90%88%E8%AE%A1",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
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


def parse_content_with_selenium(driver, url):
    """js注入登录"""
    from pathlib import Path
    import datetime
    import time
    import json
    from selenium.common.exceptions import (
        NoSuchElementException,
        JavascriptException,
        WebDriverException,
    )
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import requests

    """
    使用 Selenium 加载 URL并注入js

    Args:
        driver: 已初始化的 Selenium WebDriver 实例。
        url (str): 要加载和解析的目标网页 URL。

    Returns:
        None: 如果找不到则返回 None。
    """
    if not driver:
        print("错误：WebDriver 未成功初始化，无法解析。")
        return None

    print(f"正在加载页面: {url} ...")
    try:
        driver.get(url)
        # 保存网页源码
        page_source = driver.page_source
        output_dir = Path(".output")
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{timestamp}_page_source.html"
        with open(output_dir / output_filename, "w", encoding="utf-8") as f:
            f.write(page_source)
        print(f"网页源码已保存到==>{output_dir / output_filename}")

        """ p1=f'{output_dir / "1点击同意#modalWrapMTubes-div-div-button.png"}'
        print(f"1点击同意==>{p1}")
        # 截取当前浏览器视口的内容，并将截图保存为指定的文件
        driver.set_window_size(1920, 1080)  # 设置窗口大小
        driver.save_screenshot(p1)
        driver.find_element(By.CSS_SELECTOR, "#modalWrapMTubes > div > div > button").click()

        headerLoginLink = driver.find_element(By.CSS_SELECTOR, "#headerLoginLink.removeAdLink.signIn")
        # 使用显式等待等待某个元素出现
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "headerLoginLink"))  # 等待元素出现
        )
        p2=f'{output_dir / "2点击登录菜单#headerLoginLink.removeAdLink.signIn.png"}'
        print(f"2点击登录菜单==>{p2}")
        driver.save_screenshot(p2)
        headerLoginLink.click()
        
        p3=f'{output_dir / "3点击登录按钮#headerLoginLink-span.png"}'
        print(f"3点击登录按钮==>{p3}")
        driver.save_screenshot(p3)
        driver.find_element(By.CSS_SELECTOR, "#headerLoginLink > span").click() """

        # 等待页面加载一些时间，特别是对于依赖 JavaScript 渲染内容的页面
        print("4注入js代码==>")
        time.sleep(2)
        js_script = """
        signinbox.show({step:'signIn'}); // 直接呼出登录表单
        // 查找包含登录信息的表单
        const loginForm = document.querySelector('form.js-loginFormModal.js-loginForm');

        if (loginForm) {
            // 创建一个空对象来存储数据
            const formData = {};

            // 查找指定 name 属性的 input 元素并获取 value
            const fieldsToExtract = ['redirect', 'user_id', 'intended_action', 'token', 'from'];

            fieldsToExtract.forEach(fieldName => {
                const inputElement = loginForm.querySelector(`input[name="${fieldName}"]`); // 模板字符串语法嵌入表达式
                // 如果找到了 input 元素，就获取它的 value，否则设为 null
                // 用方括号表示法表示fieldName 是一个动态的变量来设置formData 对象的属性，而不是点表示法,如果直接formData.fieldName 表示为 formData 对象添加一个名为 fieldName 的属性，而不是根据 fieldName 的值动态地设置属性。
                formData[fieldName] = inputElement ? inputElement.value : null;
            });

            // 返回包含提取数据的对象 (Selenium 会自动转为 Python 字典)
            console.log(formData);
            return formData; // return 给 Selenium 的 Python 字典
        } else {
            // 如果没有找到表单，返回 null
            console.error('Login form not found!');
            return null;
        }
        """
        js_data = driver.execute_script(
            js_script
        )  # Selenium 会自动处理 JS 对象到 Python 字典的转换
        # 添加登录信息
        js_data['email'] = '3452255853@qq.com'
        js_data['password'] = 'kuroneko.678'
        print(f"formData==>{js_data}\n{type(js_data)}")  # <class 'dict'>
        # --------------------------------
        headers = {
            "sec-ch-ua-full-version-list": '"Microsoft Edge";v="135.0.3179.98", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.115"',
            "sec-ch-ua-platform": '"Windows"',
            "Cache-Control": "no-cache",
            "sec-ch-ua": '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            "sec-ch-ua-model": '""',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-arch": '"x86"',
            "sec-ch-ua-full-version": '"135.0.3179.98"',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
            "Content-Type": "application/x-www-form-urlencoded",
            "sec-ch-ua-platform-version": '"19.0.0"',
            "Accept": "*/*",
            "Origin": "https://cn.pornhub.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://cn.pornhub.com/",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7",
            "Cookie": "__l=680D0CEA-42FE722901BB2C04B0-1297BE1F; ua=99d149899c4f2f3d79df1f8e73f539ef; platform=pc; bs=00000000000000001046530daa2c8e45; bsdd=00000000000000001046530daa2c8e45; ss=764865985519956585; sessid=259701793721818004; comp_detect-cookies=90419.100000; fg_afaf12e314c5419a855ddc0bf120670f=25143.100000; fg_757a7e3b2b97e62caeae14647b10ab8a=62121.100000; fg_7d31324eedb583147b6dcbea0051c868=28882.100000; __l=680D1632-42FE722901BB30C02F-13267C46; tj_UUID=ChCXGChb6Z9GrqcIgA3tuJNjEgwI8dGcwAYQ_JyOrQEYAQ==; tj_UUID_v2=ChCXGChb6Z9GrqcIgA3tuJNjEgwI8dGcwAYQ_JyOrQEYAQ==; _ga=GA1.1.1873696124.1745688120; accessAgeDisclaimerPH=1; d_uidb=ab7a7d3d-7022-a0a6-0375-30a472f64ca4; d_uid=ab7a7d3d-7022-a0a6-0375-30a472f64ca4; d_uidb=ab7a7d3d-7022-a0a6-0375-30a472f64ca4; vlc=527373886271609987; __s=680DFB54-42FE722901BB228F06-120784D2; d_fs=1; _ga_B39RFFWGYY=GS1.1.1745746775.4.0.1745746775.60.0.0",
        }
        session = requests.session()
        response = session.post(
            url='https://cn.pornhub.com/front/authenticate', data=js_data, headers=headers
        )  # 发送post请求登录https://cn.pornhub.com/front/authenticate
        output_filename = f"{timestamp}_login_source.html"
        print(f"登录源码==>{response.text}")
        with open(output_dir / f"{output_filename}", "w", encoding="utf-8") as f:
            f.write(response.text)
            print(f"登录源码已保存到 {output_dir / output_filename}")
        # if player_data:
        #     print("js注入成功。结构如下:")
        #     # 打印部分数据结构以帮助调试 (避免打印过多内容)
        #     print(json.dumps(player_data, indent=2, ensure_ascii=False)[:1000] + "...") # 完整打印可能很大
        #     # limited_data_repr = str(player_data)[:500] + ('...' if len(str(player_data)) > 500 else '')
        #     # print(limited_data_repr)

        #     print("\n正在解析数据，查找链接...")
        #     # --- 在 Python 字典中查找链接 ---
        #     # 下面的访问路径需要根据上面打印出的实际数据结构进行调整
        #     media_definitions = player_data.get('mediaDefinitions')
        #     print(f"{type(media_definitions)}\n{media_definitions}")
        #     if media_definitions and isinstance(media_definitions, list):
        #         hub_list=[]
        #         for media in media_definitions:
        #             # .get() 方法更安全，避免因 key 不存在而报错
        #             quality = str(media.get('quality', ''))
        #             video_url = media.get('videoUrl')
        #             format_info = str(media.get('format', ''))

        #             # 打印检查的条目信息，方便调试
        #             print(f"  检查: quality='{quality}', format='{format_info}', url_exists={bool(video_url)}")
        #             movie_info={
        #                 "质量":quality,
        #                 "格式":format_info,
        #                 "链接":video_url
        #             }

        #             # 检查条件：质量是 '1080'
        #             if quality in ['1080'] and video_url and  format_info:
        #                 # print(f"\n*** 成功找到链接: {video_url} ***")
        #                 hub_list.append(movie_info)

        #         print(hub_list, type(hub_list), sep="\n")
        #         df = pd.DataFrame(hub_list,columns=movie_info.keys())
        #         df.index.name = "id"  # 重命名索引
        #         df.index = df.index + 1  # id索引从1开始。
        #         print(f"前几行==>\n{df.head()}")
        #         print(f"（行数，列数）==> {df.shape}")

        #         # 保存excel
        #         file_path = (
        #             f".output/hub{(datetime.datetime.now().strftime('%Y%m%d'))}.xlsx"
        #         )
        #         df.to_excel(file_path,index=False) #

        #         print(f"\n已经将结果保存到{file_path}")

        #         return hub_list
        #     # --- 查找结束 ---

        # else:
        #     print("js注入失败")

    except JavascriptException as e:
        print(f"执行 JavaScript 时出错: {e}")
    except WebDriverException as e:
        print(f"与 WebDriver 交互时出错 {e}")
    except Exception as e:
        print(f"解析过程中发生未知错误: {e}")

    return None


if __name__ == "__main__":
    target_url = "https://cn.pornhub.com/"
    # get_content(1,None)
    driver = setup_driver()
    parse_content_with_selenium(driver, target_url)
