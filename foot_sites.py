from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By






class Footlockerbot:
    def __init__(self):
        self.driverLocation = '/Users/jamesbaker/Desktop/footlocker_notes/chromedriver'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        # chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--allow-insecure-localhost");
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument("window-size=1920,1080");
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--incognito")
        # chrome_options.add_argument("start-maximized")
        # chrome_options.add_argument("disable-infobars")
        # chrome_options.add_argument("--disable-extensions")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        # PROXY = "12.218.209.130:53281"
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.39 Safari/537.36'
        chrome_options.add_argument("user-agent="+user_agent)
        self.driver = webdriver.Chrome(self.driverLocation,chrome_options=chrome_options)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
          "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
          "source": """
            Object.defineProperty(navigator, 'plugins', {
              get: () => [1, 2, 3, 4, 5]
            })
          """
        })
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
          "source": """
            Object.defineProperty(navigator, 'languages', {
              get: () => ['en-US', 'en']
            })
          """
        })

    def add_item_to_cart(self, url, size):
        self.driver.get("https://www.footlocker.com/product/nike-air-force-1-07-low-womens/O2132602.html")
        # print(self.driver.page_source)
        print("adding item to cart")
        size = self.driver.find_element_by_xpath("//label[@for='input_radio_size_095']")
        add_to_cart = self.driver.find_element_by_xpath("//li[@class='col']/button[@class='Button ProductDetails-form__action']")

        size.click()
        self.driver.execute_script("arguments[0].click();", add_to_cart)

        # print(url + " Added to cart with size " + size)
        time.sleep(1)

    def fill_checkout(self):
        print("Checking out")
        first_name_input = "John"
        last_name_input = "Faker"
        address_line_1_input = "20 Harris Road"
        zip_code_input = "10583"
        city_input = "Scarsdale"
        state_input = "NY"
        telephone_input = "9146024735"
        email_address_input = "james.baker1328@gmail.com"

        # driver.get("file:///Users/jamesbaker/Desktop/checkout.htm")
        self.driver.get("https://www.footlocker.com/checkout")

        time.sleep(1)
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

        country = Select(self.driver.find_element_by_xpath("//select[@name='country']"))
        country.select_by_value("US")

        first_name = self.driver.find_element_by_name("firstName")
        first_name.click()
        first_name.send_keys(first_name_input)

        last_name = self.driver.find_element_by_name("lastName")
        last_name.click()
        last_name.send_keys(last_name_input)

        address_line_one = self.driver.find_element_by_name("line1")
        address_line_one.click()
        address_line_one.send_keys(address_line_1_input)

        zip_code = self.driver.find_element_by_name("postalCode")
        zip_code.click()
        zip_code.send_keys(zip_code_input)

        city = self.driver.find_element_by_name("town")
        city.click()
        city.send_keys(city_input)

        state = Select(self.driver.find_element_by_xpath("//select[@name='region']"))
        state.select_by_value(state_input)

        telephone = self.driver.find_element_by_name("phone")
        telephone.click()
        telephone.send_keys(telephone_input)

        telephone = self.driver.find_element_by_name("email")
        telephone.click()
        telephone.send_keys(email_address_input)

        dif_billing_address = self.driver.find_element_by_xpath('//*[@id="Address"]/div[12]/label/span[1]')
        self.driver.execute_script("arguments[0].click();", dif_billing_address)

        save_and_continue = self.driver.find_element_by_xpath("//*[contains(text(), 'Save & Continue')]")
        save_and_continue.click()

        time.sleep(2)
        #
        self.try_save_and_continue(1)
        #
        self.fill_billing()
        self.try_save_and_continue(1)

        time.sleep(3)

        self.fill_card()
        self.try_save_and_continue(1)


    def escape_from_alert(self):
        time.sleep(.5)
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()


    def try_save_and_continue(self, n):
        if n == 5:
            return
        self.escape_from_alert()
        print("Trying to save and continue")
        time.sleep(3)
        try:
            save_and_continue2 = self.driver.find_element_by_xpath('//*[@id="AddressLookup"]/ul/li[3]/button')
            save_and_continue2.click()
        except:
            # print(e)
            self.try_save_and_continue(n+1)
            print("fck")

    def try_accept_alert(self, n):
        print("Accepting alert")
        if n == 5:
            return
        try:
            self.driver.switch_to.alert.accept()
        except:
            self.try_accept_alert(n+1)
            print("fuck")

    def fill_card(self):
        print("Filling out card")
        self.driver.save_screenshot("screenshot1.png")
        self.escape_from_alert()

        card_number_input = "4012888888881881"
        month_exp_input = "01"
        year_exp_input = "2025"
        csc_input = "637"

        card_number = self.driver.find_element_by_name("cardNumber")
        card_number.click()
        card_number.send_keys(card_number_input)

        month_exp = Select(self.driver.find_element_by_xpath("//select[@name='expiryMonth']"))
        month_exp.select_by_value(month_exp_input)

        year_exp = Select(self.driver.find_element_by_xpath("//select[@name='expiryYear']"))
        year_exp.select_by_value(year_exp_input)

        csc = self.driver.find_element_by_name("CSC")
        csc.click()
        csc.send_keys(csc_input)

        save_and_continue = self.driver.find_element_by_xpath("//*[contains(text(), 'Save & Continue')]")
        save_and_continue.click()
        print("Done!")
        self.driver.save_screenshot("screenshot1213.png")


    def fill_billing(self):
        print("filling out billing")
        time.sleep(3)
        first_name_input = "John"
        last_name_input = "Faker"
        address_line_1_input = "20 Harris Road"
        zip_code_input = "10583"
        city_input = "Scarsdale"
        state_input = "NY"
        telephone_input = "9146024735"
        email_address_input = "james.baker1328@gmail.com"

        self.escape_from_alert()
        # self.driver.get("file:///Users/jamesbaker/Desktop/footlocker_notes/billing2.htm")
        self.driver.get("http://footlocker.com/checkout")
        self.try_accept_alert(1)
        time.sleep(5)
        country2 = Select(self.driver.find_element_by_xpath("//select[@name='country']"))
        country2.select_by_value("US")

        # first_name = self.driver.find_element_by_name("firstName")
        # first_names = self.driver.find_elements_by_xpath('//*[@id="input_text_firstName"]')
        # print(len(first_names))
        first_name = self.driver.find_element_by_xpath('//*[@id="input_text_firstName"]')
        # print(first_name.location)
        # first_name.click()
        first_name.send_keys(first_name_input)

        last_name = self.driver.find_element_by_name("lastName")
        last_name.click()
        last_name.send_keys(last_name_input)

        address_line_one = self.driver.find_element_by_name("line1")
        address_line_one.click()
        address_line_one.send_keys(address_line_1_input)

        zip_code = self.driver.find_element_by_name("postalCode")
        zip_code.click()
        zip_code.send_keys(zip_code_input)

        city = self.driver.find_element_by_name("town")
        city.click()
        city.send_keys(city_input)

        state = Select(self.driver.find_element_by_xpath("//select[@name='region']"))
        state.select_by_value(state_input)

        telephone = self.driver.find_element_by_name("phone")
        telephone.click()
        telephone.send_keys(telephone_input)

        save_and_continue = self.driver.find_element_by_xpath("//*[contains(text(), 'Save & Continue')]")
        save_and_continue.click()

    # def try_save_and_continue(self):
    #     self.driver.get("file:///Users/jamesbaker/Desktop/footlocker_notes/sandcontinue.htm")
    #
    #     save_and_continue2 = self.driver.find_element_by_xpath('//*[@id="AddressLookup"]/ul/li[3]/button')
    #
    #     save_and_continue2.click()

    def test_dif_billing(self):
        # self.driver.get("file:///Users/jamesbaker/Desktop/footlocker_notes/metoo.htm")
        self.driver.get("https://www.footlocker.com/checkout")
        time.sleep(2)

        dif_billing_address = self.driver.find_element_by_xpath('//*[@id="Address"]/div[12]/label/span[1]')
        # //*[@id="Address"]/div[12]/label/span[1]
        print(dif_billing_address.location)
        # dif_billing_address.click()
        self.driver.execute_script("arguments[0].click();", dif_billing_address)



if __name__ == "__main__":
    # execute only if run as a script
    test_bot = Footlockerbot()
    # test_bot.test_dif_billing()
    # test_bot.try_save_and_continue()
    test_bot.add_item_to_cart("https://www.footlocker.com/product/nike-air-force-1-07-low-womens/O2132602.html", "9")
    # test_bot.test_dif_billing()
    test_bot.fill_checkout()
    # test_bot.fill_billing()
    # test_bot.firefox()
    # test_bot.chrome()
    # test_bot.test_save_and_continue()
