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
        pass

    def test1(self):
        driverLocation = '/Users/jamesbaker/Desktop/footlocker_notes/chromedriver'
        # driver = webdriver.Chrome(driverLocation)
        # # driver.get("https://www.footlocker.com/product/adidas-originals-yeezy-boost-350-v2-mens/FLYESH.html")
        # driver.get("https://www.google.com")

        # assert "Python" in driver.title
        # elem = driver.find_element_by_class_name('ProductDetails-form__action')
        # elem.click()
        # elem = driver.find_element_by_xpath('//button[text()="ADD TO CART"]')
        # elem.clear()
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source
        # driver.close()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(driverLocation,chrome_options=chrome_options)
        driver.get("https://www.footlocker.com/product/adidas-originals-yeezy-boost-350-v2-mens/FLYESH.html")
        print(driver.window_handles)
        # time.sleep(3)
        # elem = driver.find_element_by_xpath('//*[@id="ProductDetails"]')
        # elem = driver.find_element_by_id("ProductDetails")

# //*[@id="ProductDetails"]/[text()="Add To Cart"]
# /html/body/div[1]/div/main/div/div[2]/div/div/form/div[6]/button
        # elem = driver.find_element_by_class_name('ProductDetails-form__action')

        # d.get('https://www.google.nl/')

    def test2(self):
        driverLocation = '/Users/jamesbaker/Desktop/footlocker_notes/chromedriver'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        prox = Proxy()
        prox.proxy_type = ProxyType.MANUAL
        prox.http_proxy = "34.93.147.196:80"
        # prox.socks_proxy = "ip_addr:port"
        # prox.ssl_proxy = "ip_addr:port"
        capabilities = webdriver.DesiredCapabilities.CHROME
        prox.add_to_capabilities(capabilities)
        driver = webdriver.Chrome(driverLocation,chrome_options=chrome_options, desired_capabilities=capabilities)
        # driver.get("https://www.footlocker.com/product/nike-air-force-1-07-low-womens/O2132602.html")
        driver.get("https://www.google.com")

        print(driver.page_source)
        # elem = driver.find_element_by_xpath("//button[contains('Add To Cart')]")
        # elem = driver.find_element_by_css_selector(".Button.ProductDetails-form__action")
        # elem.click()

    # def test(self):
    #     driverLocation = '/Users/jamesbaker/Desktop/footlocker_notes/chromedriver'
    #     chrome_options = webdriver.ChromeOptions()
        PROXY = "smart-us.jeru035.com:23774:jerursvpking8588:rsvpking8588"
        PROXY = "jerursvpking8588:rsvpking8588@smart-us.jeru035.com:23774"
        PROXY = "174.127.155.118:32505"
    #     # chrome_options.add_argument('--headless')
    #     chrome_options.add_argument('window-size=1200x600') # optional
    #
    #     chrome_options.add_argument('--incognito')
    #     chrome_options.add_argument('--no-sandbox')
    #     chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
    #     driver = webdriver.Chrome(driverLocation, chrome_options=chrome_options)
    #     # driver.get("https://www.aol.com")
    #     # time.sleep(.75)
    #     # try:
    #     #     alert = driver.switch_to.alert
    #     # except:
    #     #     print("No Alert!")
    #     # driver.switch_to.alert.send_keys("jerursvpking8588" + TAB + "rsvpking8588")
    #     # driver.switch_to.alert.accept()
    #     # driver.get("https://www.footlocker.com/product/nike-air-force-1-07-low-womens/O2132602.html")
    #     driver.get("https://www.google.com")
    #     driver.save_screenshot("tester.png")
    #     print(driver.page_source)

    def firefox(self):

        first_name_input = "James"
        last_name_input = "Baker"
        address_line_1_input = "7 Myrtledale Road"
        zip_code_input = "10583"
        city_input = "Scarsdale"
        state_input = "NY"
        telephone_input = "9146024775"
        email_address_input = "james.baker1628@gmail.com"
        size = "10"

        driverLocation = '/Users/jamesbaker/Desktop/footlocker_notes/geckodriver'
        options = FirefoxOptions()
        # options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path=driverLocation, options=options)
        # driver.get("https://www.footlocker.com/product/nike-air-force-1-07-low-womens/O2132602.html")
        if False:
            driver.get("file:///Users/jamesbaker/Desktop/jim.htm")
            print("Loaded " + driver.title)
            assert "Foot Locker" in driver.title

            add_to_cart = driver.find_element_by_css_selector(".Button.ProductDetails-form__action")
            size = driver.find_element_by_xpath("//label[@for='input_radio_size_100']")
            size.click()
            time.sleep(.5)
            add_to_cart.click()
            time.sleep(.5)

        driver.get("file:///Users/jamesbaker/Desktop/checkout.htm")
        # driver.get("https://www.footlocker.com/checkout")

        country = Select(driver.find_element_by_xpath("//select[@name='country']"))
        country.select_by_value("US")

        first_name = driver.find_element_by_name("firstName")
        first_name.click()
        first_name.send_keys(first_name_input)

        last_name = driver.find_element_by_name("lastName")
        last_name.click()
        last_name.send_keys(last_name_input)

        address_line_one = driver.find_element_by_name("line1")
        address_line_one.click()
        address_line_one.send_keys(address_line_1_input)

        zip_code = driver.find_element_by_name("postalCode")
        zip_code.click()
        zip_code.send_keys(zip_code_input)

        city = driver.find_element_by_name("town")
        city.click()
        city.send_keys(city_input)

        state = Select(driver.find_element_by_xpath("//select[@name='region']"))
        state.select_by_value(state_input)

        telephone = driver.find_element_by_name("phone")
        telephone.click()
        telephone.send_keys(telephone_input)


        email_address = driver.find_element_by_name("email")
        email_address.click()
        email_address.send_keys(email_address_input)

        # time.sleep(1)

        # save_and_continue = driver.find_element_by_xpath("//*[contains(text(), 'Save & Continue')]")
        # save_and_continue.click()





        # driver.get("http://www.python.org")
        # assert "Python" in driver.title
        # elem = driver.find_element_by_name("q")
        # elem.clear()
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source
        # print(elem)
        # # driver.close()
    def chrome(self):

        first_name_input = "John"
        last_name_input = "Faker"
        address_line_1_input = "20 Harris Road"
        zip_code_input = "10583"
        city_input = "Scarsdale"
        state_input = "NY"
        telephone_input = "9146024735"
        email_address_input = "james.baker1328@gmail.com"

        driverLocation = '/Users/jamesbaker/Desktop/footlocker_notes/chromedriver'
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument("--incognito")
        # chrome_options.add_argument("start-maximized")
        # chrome_options.add_argument("disable-infobars")
        # chrome_options.add_argument("--disable-extensions")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        # PROXY = "12.218.209.130:53281"
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)


        driver = webdriver.Chrome(driverLocation,chrome_options=chrome_options)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
          "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })
        # options = FirefoxOptions()
        # options.add_argument("--headless")
        # driver = webdriver.Chrome(driverLocation)
        # driver.get("https://www.footlocker.com/product/nike-air-force-1-07-low-womens/O2132602.html")
        # driver.get("file:///Users/jamesbaker/Desktop/test.htm")
        print("Loaded " + driver.title)
        # assert "Foot Locker" in driver.title

        # add_to_cart = driver.find_element_by_css_selector(".Button.ProductDetails-form__action")
        # add_to_cart = driver.find_element_by_xpath("//*[contains(text(), 'Add To Cart')]")
        # add_to_cart = driver.find_element_by_xpath("//*[contains(text(), 'Add To Cart')]")
        # add_to_cart = driver.find_element_by_css_selector(".ProductDetails-form__action.Button")

        if True:
            driver.get("https://www.footlocker.com/product/nike-air-force-1-07-low-womens/O2132602.html")
            size = driver.find_element_by_xpath("//label[@for='input_radio_size_095']")
            size.click()
            # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Add To Cart')]"))).click()
            # add_to_cart.click()
            add_to_cart = driver.find_element_by_xpath("//li[@class='col']/button[@class='Button ProductDetails-form__action']")
            # add_to_cart.click()
            driver.execute_script("arguments[0].click();", add_to_cart)
            print(add_to_cart.location)
            print(size.location)
            time.sleep(2)
        # webdriver.ActionChains(driver).move_to_element(add_to_cart).click(add_to_cart).perform()

        # time.sleep(10)

        # try:
        # add_to_cart.click()
        # webdriver.ActionChains(driver).move_to_element(add_to_cart).click(add_to_cart).perform()

        # except:
        #     # time.sleep(4)
        #     print("here")
        #     # Click away from modal
        #     # action = webdriver.ActionChains(driver)
        #     # action.move_to_element(size)
        #     # action.click()
        #     # action.perform()
        #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        #     time.sleep(.5)
        # webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        #     time.sleep(.5)
        # webdriver.ActionChains(driver).move_to_element(add_to_cart).click(add_to_cart).perform()
        # add_to_cart.click()
        # time.sleep(1)

        if True:
            # driver.get("file:///Users/jamesbaker/Desktop/checkout.htm")
            driver.get("https://www.footlocker.com/checkout")
            # driver.get("https://www.google.com")
            # driver.get("http://whatismyipaddress.com")
            # driver.get("https://www.redbubble.com/")
            # driver.get("")

            time.sleep(1)
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            # try:
            #     continue_checkout = driver.find_element_by_xpath("//*[contains(text(), 'Continue Checkout')]")
            #     print(continue_checkout.location)
            # except:
            #     print("can't find that shit")

            time.sleep(1)
            country = Select(driver.find_element_by_xpath("//select[@name='country']"))
            country.select_by_value("US")

            first_name = driver.find_element_by_name("firstName")
            first_name.click()
            first_name.send_keys(first_name_input)

            last_name = driver.find_element_by_name("lastName")
            last_name.click()
            last_name.send_keys(last_name_input)

            address_line_one = driver.find_element_by_name("line1")
            address_line_one.click()
            address_line_one.send_keys(address_line_1_input)

            zip_code = driver.find_element_by_name("postalCode")
            zip_code.click()
            zip_code.send_keys(zip_code_input)

            city = driver.find_element_by_name("town")
            city.click()
            city.send_keys(city_input)

            state = Select(driver.find_element_by_xpath("//select[@name='region']"))
            state.select_by_value(state_input)

            telephone = driver.find_element_by_name("phone")
            telephone.click()
            telephone.send_keys(telephone_input)

            telephone = driver.find_element_by_name("email")
            telephone.click()
            telephone.send_keys(email_address_input)

            time.sleep(1)

            save_and_continue = driver.find_element_by_xpath("//*[contains(text(), 'Save & Continue')]")
            save_and_continue.click()

            time.sleep(200)

        # if True:
        #     driver.get("file:///Users/jamesbaker/Desktop/checkout_popup.htm")
        #
        #     try:
        #         continue_checkout = driver.find_element_by_xpath("//*[contains(text(), 'Continue Checkout')]")
        #         print(continue_checkout.location)
        #     except:
        #         print("can't find that shit")




            # email_address = driver.find_element_by_name("email")
            # email_address.click()
            # email_address.send_keys(email_address_input)

            # time.sleep(1)

            # save_and_continue = driver.find_element_by_xpath("//*[contains(text(), 'Save & Continue')]")
            # save_and_continue.click()





            # driver.get("http://www.python.org")
            # assert "Python" in driver.title
            # elem = driver.find_element_by_name("q")
            # elem.clear()
            # elem.send_keys("pycon")
            # elem.send_keys(Keys.RETURN)
            # assert "No results found." not in driver.page_source
            # print(elem)
            # # driver.close()



    def test_save_and_continue(self):
        driverLocation = '/Users/jamesbaker/Desktop/footlocker_notes/geckodriver'
        options = FirefoxOptions()
        # options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path=driverLocation, options=options)
        driver.get("file:///Users/jamesbaker/Desktop/checkout.htm")
        save_and_continue = driver.find_element_by_xpath("//*[contains(text(), 'Save & Continue')]")
        save_and_continue.click()

if __name__ == "__main__":
    # execute only if run as a script
    test_bot = Footlockerbot()
    # test_bot.firefox()
    test_bot.chrome()
    # test_bot.test_save_and_continue()
