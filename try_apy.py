import requests
import re
import time
import uuid
import json
from selenium import webdriver

class FootLockerApiBot:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': '"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0"',
            'DNT': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,da;q=0.6',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        })
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            'DNT': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,da;q=0.6',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }

        # self.driverLocation = '/Users/jamesbaker/Desktop/footlocker_notes/chromedriver'
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--window-size=1920,1080")
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("--proxy-server='direct://'")
        # chrome_options.add_argument("--proxy-bypass-list=*")
        # # chrome_options.add_argument("--start-maximized")
        # # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--ignore-certificate-errors')
        # chrome_options.add_argument("--allow-insecure-localhost");
        # # chrome_options.add_argument('--headless')
        # # chrome_options.add_argument("window-size=1920,1080");
        # # chrome_options.add_argument('--no-sandbox')
        # # chrome_options.add_argument('--disable-dev-shm-usage')
        # # chrome_options.add_argument("--incognito")
        # # chrome_options.add_argument("start-maximized")
        # # chrome_options.add_argument("disable-infobars")
        # # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # chrome_options.add_experimental_option('useAutomationExtension', False)
        # # PROXY = "12.218.209.130:53281"
        # # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.39 Safari/537.36'
        # chrome_options.add_argument("user-agent="+user_agent)
        # self.driver = webdriver.Chrome(self.driverLocation,chrome_options=chrome_options)
        # self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        #   "source": """
        #     Object.defineProperty(navigator, 'webdriver', {
        #       get: () => undefined
        #     })
        #   """
        # })

    def add_to_cart2(self, url):
        self.driver.get(url)
        cookies = self.driver.get_cookies()
        s = requests.Session()
        for cookie in cookies:
            s.cookies.set(cookie['name'], cookie['value'])


    def add_to_cart(self, url, size):
        # response = requests.get(url, timeout=5, headers=self.headers)
        # self.driver.get(url)
        # cookies = self.driver.get_cookies()
        # for cookie in cookies:
        #     self.session.cookies.set(cookie['name'], cookie['value'])
        response = self.session.get(url, timeout=5, headers=self.headers)

        session_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/json',
            'x-fl-request-id': str(uuid.uuid1()),
            'referer': url,
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin'
        }
        session_headers2 = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            'DNT': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,da;q=0.6',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        current_millis = int(round(time.time() * 1000))

        session_url = "https://www.footlocker.com/api/v3/session?timestamp=" + str(current_millis)
        session_response = self.session.get("https://www.footlocker.com/api/v3/session?", timeout=5, headers=session_headers)
        print(session_response.text)
        return
        # print(self.session.cookies.get_dict())
        # return
        csrf_token = json.loads(session_response.text)["data"]["csrfToken"]

        # print(session_response.text)
        size = r'\"name\":\"' + size + r'\"'
        pattern = re.compile(size + r',\"code\":\"(.*?)\"', re.MULTILINE)
        re_sneaker_code = re.search(pattern, response.text)
        if re_sneaker_code:
            sneaker_code = re_sneaker_code.group(1)
            print("Sneaker code is", sneaker_code)
        else:
            print("Can't find sneaker code. This may be a problem with the size.")
            return

        add_to_cart_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/json',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'origin': 'https://www.footlocker.com',
            'referer': url,
            'x-fl-productid': sneaker_code,
            'x-fl-request-id': str(uuid.uuid1()),
            'x-csrf-token': csrf_token

        }
        add_to_cart_payload = {
            "productQuantity": 1,
            "productId": sneaker_code
        }
        add_to_cart_url = "https://www.footlocker.com/api/users/carts/current/entries?timestamp=" + str(current_millis)
        add_to_cart_response = self.session.post(add_to_cart_url, headers=add_to_cart_headers, data=add_to_cart_payload)
        print(add_to_cart_response.request.headers)
        print(add_to_cart_response.request.body)
        print(add_to_cart_response.text)



if __name__ == "__main__":
    foot_locker_bot = FootLockerApiBot()
    foot_locker_bot.add_to_cart("https://www.footlocker.com/product/nike-lebron-17-mens/5052300.html", "08.5")
    # foot_locker_bot.add_to_cart2("https://www.footlocker.com/product/nike-lebron-17-mens/5052300.html")

    # foot_locker_bot.get_main_page()
