import requests
import re
import time
import uuid
import json

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


    def add_to_cart(self, url, size):
        response = self.session.get(url, timeout=5, headers=self.headers)

        real_cookies = '_pxhd=1312c3b9aed6a10b7b354d9a708e66281c22c4ccf491619f861cfa7cc29ec495:747de031-42e2-11ea-be40-153d8257a839; DCT_Exp_HUNDRED=DCT; bm_sz=7274CABDFEA70E0D69C1245CAB0BCAC3~YAAQaEEtF5jAIGhvAQAAButP8wbOyCnfDmyey4K7Aa2JP89ci79AbkJLLPxrgvNbLWEtYaVV3hTL0o6/7MBuQXAriih1VcaJuS4u+Uyor709/7wV6O14mjmziNWXQskx35TtsAeQEmHxA2YcsrD7G96ddWViSoMCA4L9k6tHZ8hpwfc/fswjWyO/MQVap6ACInRcZQ==; check=true; AMCVS_40A3741F578E26BA7F000101%40AdobeOrg=1; _abck=D5630E5B2611E76CC41372AFC56C3293~0~YAAQaEEtF57AIGhvAQAAtu5P8wMx67X02zSv5y/GtpdkE+smZNkb8g0+wdg69p/IQKUIJ2+OdJiKzqTZgbSYHy//vDwd12UL4n/yjCz8LQNxjCHYtGlfMmRBsnha/u3hWhOfPfWJcDWeiTrSrkS3dFCrgmCFGECzRIHlCMZB+JIq02xfknqMEde9ohcwYL4rK8uTNyraHYn8n32V/9PW1af7GKzqdP5uXLMmPP8z9iL7vDayYwtFYFxS9n9oXz4UDVM9e8OA9mYFYunFmSKo3nAXMwJJ3cEqt4wAhoFj76ZVz/AeL14zxJ+faGMF8EXaKLrr/U4GfOQXJxc=~-1~-1~-1; mboxEdgeCluster=28; AMCV_40A3741F578E26BA7F000101%40AdobeOrg=1075005958%7CMCIDTS%7C18291%7CMCMID%7C21858781549984748062372331071284516982%7CMCAAMLH-1580939899%7C7%7CMCAAMB-1580939899%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1580342299s%7CNONE%7CMCSYNCSOP%7C411-18298%7CvVersion%7C4.4.1; se=signal_off; _pxvid=747de031-42e2-11ea-be40-153d8257a839; _pxff_cl=111; _pxff_wa=1; aa_pageHistory=[{"n":"no previous page","t":"no previous page","p":"no previous page"},{"n":"FL: W: PDP","t":"Product","p":"/product/nike-lebron-17-mens/5052300.html"}]; gpv_prevURL=https%3A%2F%2Fwww.footlocker.com%2Fproduct%2Fnike-lebron-17-mens%2F5052300.html; gpv_events=no%20value; gpv_products=5052300; JSESSIONID=1l3shjadqnm8r1pd2lpdf3wrza.fzcexflapipdb638883; bm_sv=35E770B89F4E9B727B1E83F9999B10B2~LOj7e4tUHEWVGHVZ9wK9D9C6W0OPqZhW1+/qIUHSus2VksPx3vRibq7JuphJOAf6RxebqT2Ie2nCQpj880GKDP3p+W372Pj8eMd+JMK0H6dBfiAH6FtheW9PHyP5WPKzkzf705RcavFTb3IHVqtTHq5jeoxmdcIXC+o0LTzQufQ=; ak_bmsc=91E41D310F65D6E32A9FD997ACA82D2D172D41686E400000FAFF315E63C1EA09~pl/nUnNWSwP2hWoYjdSS90QJIdGaKgtMKog2wHsjo8uqIc14i4lPwNoAkQOMj/ZYAJds85GTT8HFxO/0gAzcCuW3N3/FKrsQgMU1gtXPo7Od5xIrVQ65WBaTZTriwGDa0gMNUU5Km6lbOImv8ZWHLNhVXDTzVBOfQY769ly4QKkjQR4dVIhnyPXDuygMhyXHi3aq33YD3a4YG3kFnM5+nh2sufsBjYbfgGv/DcQEsCu4jufAfL0Vgf7VfbiEl/UHdn; s_lv_s=First%20Visit; s_vnum=1580533200894%26vn%3D1; s_invisit=true; s_vs=1; s_pr_tbe65=1580335100898; s_pr_tbe66=1580335100898; s_cc=true; _px3=9b2f717d44c655d3c451b5ef61a80e91baba37327c803e38809e2d05d39daac2:0Pa/APv1GNjwTM4yauk8TIll0ES9DrzHQACfvX4GJHZDtbeINxDcxgKHgfm4mH+I7d79NcBXXxh2iCKGvlzN2A==:1000:2vh4dQ7VRAx90eTMM//GdsvB44lC0ID+5HZ9uwHhI5KR0uw5lwQGNPv6nGLQHe0T9LnZJISBG35DzYNBntzoqzBT6PZaaiXTDjcLI9Lf8AE6ElPFuxfnkdn1XZ3bcPhRm6RXbv10QgLVf+f5Fj+QIQZUAAu185HDRJTFs1+ts8I=; userStatus=guest; userVIP=unknown; mbox=session#8c5590b736a04f5788e06e655168b6bc#1580336960|PC#8c5590b736a04f5788e06e655168b6bc.28_0#1643579902; BVBRANDID=c1ab1c7e-8c0f-41c9-82b8-50a3c97a10fe; BVBRANDSID=aa197b2b-61df-44b4-b918-64c5488aa3f9; janrainSSO_session=session; BVImplmain_site=8001; rmStore=dmid:false; stc111427=tsa:1580335103086.1522518150.402585.699181115703629.15:20200129222823|env:1%7C20200229215823%7C20200129222823%7C1%7C1011950:20210128215823|uid:1580335103086.1073159794.7055864.111427.1089636337:20210128215823|srchist:1011950%3A1%3A20200229215823:20210128215823; g_vs=1; _ga=GA1.2.855384835.1580335104; _gid=GA1.2.1864486429.1580335104; _gcl_au=1.1.187331066.1580335104; sc.InTg=a; _gat_gtag_UA_116985434_4=1; mp_footlocker_mixpanel=%7B%22distinct_id%22%3A%20%2216ff350000f30a-0ca768c6d1c5e8-39647b09-13c680-16ff350001077a%22%2C%22bc_persist_updated%22%3A%201580335104111%2C%22event_lang%22%3A%20%22en%22%7D; xyz_cr_100238_et_100==&cr=100238&et=100; _mibhv=anon-1580335104465-4781220630_2389; _micpn=esp:-1::1580335104465; _scid=c9d316c6-4331-47d8-895a-5f28c68f0e38; sc.ASP.NET_SESSIONID=ccmi4k2vhf4dmu14txdvpy1r; _sctr=1|1580274000000; sc.UserId=8c568160-6ccb-4a0c-abe6-cc88ff056fd0; _fbp=fb.1.1580335105692.718294082; _ju_v=4.1_3.15; _ju_dn=1; _ju_dc=7a7ba6aa-42e2-11ea-8316-d303d8e3a406; _ju_pn=1; _gat=1; __zlcmid=wUisGeQ4aESM1S; s_lv=1580335114554; s_sq=footlockerglobalprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dfl%25253A%252520w%25253A%252520pdp%2526link%253DADD%252520TO%252520CART%2526region%253DProductDetails%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dfl%25253A%252520w%25253A%252520pdp%2526pidt%253D1%2526oid%253DADD%252520TO%252520CART%2526oidt%253D3%2526ot%253DSUBMIT; _gali=ProductDetails'

        real_cookies = real_cookies.split(";")
        real_cookes_dict = {}
        for item in real_cookies:
            new_items = item.split("=")
            real_cookes_dict[new_items[0]] = new_items[1]

        my_session = self.session.cookies.get_dict()
        print(real_cookes_dict.keys())
        print(my_session.keys())

        return

        session_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            'DNT': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,da;q=0.6',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-fl-request-id': str(uuid.uuid1()),
            'referer': url,
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin'
        }
        current_millis = int(round(time.time() * 1000))

        session_url = "https://www.footlocker.com/api/v3/session?timestamp=" + str(current_millis)
        session_response = self.session.get("https://www.footlocker.com/api/v3/session?", timeout=5, headers=session_headers)
        csrf_token = json.loads(session_response.text)["data"]["csrfToken"]

        print(session_response.text)
        size = r'\"name\":\"' + size + r'\"'
        pattern = re.compile(size + r',\"code\":\"(.*?)\"', re.MULTILINE)
        re_sneaker_code = re.search(pattern, response.text)
        if re_sneaker_code:
            sneaker_code = re_sneaker_code.group(1)
            print(sneaker_code)
        else:
            print("Can't find sneaker code. This may be a problem with the size.")
            return

        add_to_cart_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            'DNT': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,da;q=0.6',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
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

        print(add_to_cart_response.text)


if __name__ == "__main__":
    foot_locker_bot = FootLockerApiBot()
    foot_locker_bot.add_to_cart("https://www.footlocker.com/product/nike-lebron-17-mens/5052300.html", "08.5")
    # foot_locker_bot.get_main_page()
