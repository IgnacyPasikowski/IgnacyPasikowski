
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class Crawlers:

    driver= None
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--headless=new')
        self.driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)



    def kon_com_get_urls(self):
        url_vaporizers = "https://URL/?SubmitCurrency=1&id_currency=2"
        product_frame = "//div[@id='js-product-list']"
        next_btn ="//a[@class='btn btn-sm btn-no-active me-1 next js-search-link']"
        self.driver.get(url_vaporizers)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)
        iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='samba-popup-iframe samba-popup-animation']")))
        self.driver.switch_to.frame(iframe)
        yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='accept-btn']")))
        yes_button.click()
        self.driver.switch_to.default_content()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        product_urls_list = []
        next = True
        while next is True:
            print("next loop")
            time.sleep(2)
            wait.until(EC.presence_of_element_located((By.XPATH, product_frame)))
            element = self.driver.find_element(By.XPATH, product_frame)
            option_elements = element.find_elements(By.XPATH,
                                                    '//body[1]/main[1]/section[1]/div[1]/div[1]/div[3]/section[1]/section[1]/div[3]/div[1]/div[1]/article[*]/div[1]/div[1]/a[1]')
            for product in option_elements:
                a = product.get_attribute('href')
                product_urls_list.append(str(a) + "/?SubmitCurrency=1&id_currency=1")
                print(product_urls_list)
            try:
                # Find the element
                next_page = self.driver.find_element(By.XPATH, next_btn)
                # Get the dimensions of the viewport
                viewport_width = self.driver.execute_script("return window.innerWidth;")
                viewport_height = self.driver.execute_script("return window.innerHeight;")
                # Get the location of the element
                element_x = next_page.location["x"]
                element_y = next_page.location["y"]
                element_width = next_page.size["width"]
                element_height = next_page.size["height"]
                # Calculate the scroll position to center the element
                scroll_x = element_x - (viewport_width / 2) + (element_width / 2)
                scroll_y = element_y - (viewport_height / 2) + (element_height / 2)
                # Scroll to the calculated position
                self.driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", scroll_x, scroll_y)
                time.sleep(2)
                next_page.click()
                next = True
            except:
                print("false")
                next = False

        return product_urls_list

    def kon_pl_get_urls(self):
        url_vaporizers = "https://URL/?SubmitCurrency=1&id_currency=1"
        product_frame = "//div[@id='js-product-list']"
        next_btn = "//a[@class='btn btn-sm btn-no-active me-1 next js-search-link']"
        self.driver.get(url_vaporizers)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)
        iframe = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//iframe[@class='samba-popup-iframe samba-popup-animation']")))
        self.driver.switch_to.frame(iframe)
        yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='accept-btn']")))
        yes_button.click()
        self.driver.switch_to.default_content()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        product_urls_list = []

        next = True
        while next is True:
            print("next loop")
            time.sleep(2)
            wait.until(EC.presence_of_element_located((By.XPATH, product_frame)))
            element = self.driver.find_element(By.XPATH, product_frame)
            option_elements = element.find_elements(By.XPATH,
                                                    '//body[1]/main[1]/section[1]/div[1]/div[1]/div[3]/section[1]/section[1]/div[3]/div[1]/div[1]/article[*]/div[1]/div[1]/a[1]')
            for product in option_elements:
                a = product.get_attribute('href')
                product_urls_list.append(str(a) + "/?SubmitCurrency=1&id_currency=1")
                print(product_urls_list)
            try:
                # Find the element
                next_page = self.driver.find_element(By.XPATH, next_btn)
                # Get the dimensions of the viewport
                viewport_width = self.driver.execute_script("return window.innerWidth;")
                viewport_height = self.driver.execute_script("return window.innerHeight;")
                # Get the location of the element
                element_x = next_page.location["x"]
                element_y = next_page.location["y"]
                element_width = next_page.size["width"]
                element_height = next_page.size["height"]
                # Calculate the scroll position to center the element
                scroll_x = element_x - (viewport_width / 2) + (element_width / 2)
                scroll_y = element_y - (viewport_height / 2) + (element_height / 2)
                # Scroll to the calculated position
                self.driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", scroll_x, scroll_y)
                time.sleep(2)
                next_page.click()
                next = True
            except:
                print("false")
                next = False
        return product_urls_list

    def vs_pl_get_urls(self):
        url_vaporizers = "https://URL/pl/12-url"
        product_frame = "//div[@id='js-product-list']"
        next_btn = ("//div[c"
                    "ontains(@class,'pagination-wrapper pagination-wrapper-bottom')]//a[@id='infinity-url-next']")
        self.driver.get(url_vaporizers)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)
        product_urls_list = []
        next = True
        while next is True:
            print("next loop")
            time.sleep(2)
            wait.until(EC.presence_of_element_located((By.XPATH, product_frame)))
            element = self.driver.find_element(By.XPATH, product_frame)
            option_elements = element.find_elements(By.XPATH,
                                                    '//body[1]/main[1]/section[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[3]/div[2]/div[1]/div[*]/article[1]/div[1]/a[1]')
            for product in option_elements:
                a = product.get_attribute('href')
                product_urls_list.append(a)
                print(product_urls_list)
            try:
                # Find the element
                next_page = self.driver.find_element(By.XPATH, next_btn)
                # Get the dimensions of the viewport
                viewport_width = self.driver.execute_script("return window.innerWidth;")
                viewport_height = self.driver.execute_script("return window.innerHeight;")
                # Get the location of the element
                element_x = next_page.location["x"]
                element_y = next_page.location["y"]
                element_width = next_page.size["width"]
                element_height = next_page.size["height"]
                # Calculate the scroll position to center the element
                scroll_x = element_x - (viewport_width / 2) + (element_width / 2)
                scroll_y = element_y - (viewport_height / 2) + (element_height / 2)
                # Scroll to the calculated position
                self.driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", scroll_x, scroll_y)
                time.sleep(2)
                next_page.click()
                next = True
            except:
                print("false")
                next = False

        return product_urls_list


    def vs_get_urls(self):
        url_vaporizers = "https://www.URL"
        product_frame = "//reveal-items[@selector='.product-list > *']"
        next_btn ="//button[@id='gsloadmore']"
        self.driver.get(url_vaporizers)
        self.driver.maximize_window()
        product_urls_list = []
        try:
            wait = WebDriverWait(self.driver, 10)
            iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='fancyboxAge-iframe']")))
            self.driver.switch_to.frame(iframe)
            yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='enter']")))
            yes_button.click()

            self.driver.switch_to.default_content()
        except TimeoutException:
            pass

        next = True
        while next is True:
            print("next loop")
            time.sleep(2)

            try:
                # Find the element
                next_page = self.driver.find_element(By.XPATH, next_btn)
                # Get the dimensions of the viewport
                viewport_width = self.driver.execute_script("return window.innerWidth;")
                viewport_height = self.driver.execute_script("return window.innerHeight;")
                # Get the location of the element
                element_x = next_page.location["x"]
                element_y = next_page.location["y"]
                element_width = next_page.size["width"]
                element_height = next_page.size["height"]
                # Calculate the scroll position to center the element
                scroll_x = element_x - (viewport_width / 2) + (element_width / 2)
                scroll_y = element_y - (viewport_height / 2) + (element_height / 2)
                # Scroll to the calculated position
                self.driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", scroll_x, scroll_y)
                time.sleep(2)
                next_page.click()
                next = True
            except:

                print("false")
                next = False
        wait.until(EC.presence_of_element_located((By.XPATH, product_frame)))
        element = self.driver.find_element(By.XPATH,product_frame)
        option_elements = element.find_elements(By.XPATH,
                                                '//body[1]/main[1]/section[2]/div[1]/div[1]/div[3]/div[1]/reveal-items[1]/product-list[1]/product-card[*]/div[2]/a[1]')
        for product in option_elements:
            a = product.get_attribute('href')
            product_urls_list.append(str(a))
            print(product_urls_list)
        return product_urls_list

    def vsDE_get_urls(self):
        url_vaporizers = "https://www.URL"
        product_frame = "//reveal-items[@selector='.product-list > *']"
        next_btn ="//button[@id='gsloadmore']"
        self.driver.get(url_vaporizers)
        self.driver.maximize_window()
        product_urls_list = []
        try:
            wait = WebDriverWait(self.driver, 5)
            iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='fancyboxAge-iframe']")))
            self.driver.switch_to.frame(iframe)
            yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='enter']")))
            yes_button.click()
            self.driver.switch_to.default_content()
        except TimeoutException:
            pass

        next = True

        while next is True:
            print("next loop")
            time.sleep(2)
            try:
                # Find the element
                next_page = self.driver.find_element(By.XPATH,next_btn)
                # Get the dimensions of the viewport
                viewport_width = self.driver.execute_script("return window.innerWidth;")
                viewport_height = self.driver.execute_script("return window.innerHeight;")
                # Get the location of the element
                element_x = next_page.location["x"]
                element_y = next_page.location["y"]
                element_width = next_page.size["width"]
                element_height = next_page.size["height"]
                # Calculate the scroll position to center the element
                scroll_x = element_x - (viewport_width / 2) + (element_width / 2)
                scroll_y = element_y - (viewport_height / 2) + (element_height / 2)
                # Scroll to the calculated position
                self.driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", scroll_x, scroll_y)
                time.sleep(2)
                next_page.click()
                next = True
            except:
                next = False
        wait.until(EC.presence_of_element_located((By.XPATH, product_frame)))
        element = self.driver.find_element(By.XPATH,product_frame)
        option_elements = element.find_elements(By.XPATH,
                                        '//body[1]/main[1]/section[2]/div[1]/div[1]/div[3]/div[1]/reveal-items[1]/product-list[1]/product-card[*]/div[2]/a[1]')
        for product in option_elements:
            a = product.get_attribute('href')
            product_urls_list.append(str(a))
            print(product_urls_list)
        return product_urls_list

    def vsNL_get_urls(self):
        url_vaporizers = "https://www.URL"
        product_frame = "//reveal-items[@selector='.product-list > *']"
        next_btn ="//button[@id='gsloadmore']"
        self.driver.get(url_vaporizers)
        self.driver.maximize_window()
        product_urls_list = []
        try:
            wait = WebDriverWait(self.driver, 5)
            iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='fancyboxAge-iframe']")))
            self.driver.switch_to.frame(iframe)
            yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='enter']")))
            yes_button.click()
            self.driver.switch_to.default_content()
        except TimeoutException:
            pass


        next = True
        while next is True:
            print("next loop")
            time.sleep(2)

            try:
                # Find the element
                next_page = self.driver.find_element(By.XPATH,next_btn)
                # Get the dimensions of the viewport
                viewport_width = self.driver.execute_script("return window.innerWidth;")
                viewport_height = self.driver.execute_script("return window.innerHeight;")
                # Get the location of the element
                element_x = next_page.location["x"]
                element_y = next_page.location["y"]
                element_width = next_page.size["width"]
                element_height = next_page.size["height"]
                # Calculate the scroll position to center the element
                scroll_x = element_x - (viewport_width / 2) + (element_width / 2)
                scroll_y = element_y - (viewport_height / 2) + (element_height / 2)
                # Scroll to the calculated position
                self.driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", scroll_x, scroll_y)
                time.sleep(2)
                next_page.click()
                next = True
            except:
                next = False
        wait.until(EC.presence_of_element_located((By.XPATH, product_frame)))
        element = self.driver.find_element(By.XPATH,product_frame)
        option_elements = element.find_elements(By.XPATH,
                                        '//body[1]/main[1]/section[2]/div[1]/div[1]/div[3]/div[1]/reveal-items[1]/product-list[1]/product-card[*]/div[2]/a[1]')
        try:
            for product in option_elements:
                a = product.get_attribute('href')
                product_urls_list.append(str(a))
                print(product_urls_list)
            return product_urls_list
        except TimeoutException:
            pass

    def vsFR_get_urls(self):
        url_vaporizers = "https://www.URL"
        product_frame = "//reveal-items[@selector='.product-list > *']"
        next_btn ="//button[@id='gsloadmore']"
        self.driver.get(url_vaporizers)
        self.driver.maximize_window()
        product_urls_list = []
        try:
            wait = WebDriverWait(self.driver, 10)
            iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='fancyboxAge-iframe']")))
            self.driver.switch_to.frame(iframe)
            yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='enter']")))
            yes_button.click()
            self.driver.switch_to.default_content()
        except TimeoutException:
            pass


        next = True
        while next is True:
            print("next loop")
            time.sleep(2)

            try:
                # Find the element
                next_page = self.driver.find_element(By.XPATH,next_btn)
                # Get the dimensions of the viewport
                viewport_width = self.driver.execute_script("return window.innerWidth;")
                viewport_height = self.driver.execute_script("return window.innerHeight;")
                # Get the location of the element
                element_x = next_page.location["x"]
                element_y = next_page.location["y"]
                element_width = next_page.size["width"]
                element_height = next_page.size["height"]
                # Calculate the scroll position to center the element
                scroll_x = element_x - (viewport_width / 2) + (element_width / 2)
                scroll_y = element_y - (viewport_height / 2) + (element_height / 2)
                # Scroll to the calculated position
                self.driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", scroll_x, scroll_y)
                time.sleep(2)
                next_page.click()
                next = True
            except:
                next = False
        wait.until(EC.presence_of_element_located((By.XPATH, product_frame)))
        element = self.driver.find_element(By.XPATH,product_frame)
        option_elements = element.find_elements(By.XPATH,
                                        '//body[1]/main[1]/section[2]/div[1]/div[1]/div[3]/div[1]/reveal-items[1]/product-list[1]/product-card[*]/div[2]/a[1]')
        for product in option_elements:
            a = product.get_attribute('href')
            product_urls_list.append(str(a))
            print(product_urls_list)
        return product_urls_list
    def vsES_get_urls(self):
        url_vaporizers = "https://www.URL"
        product_frame = "//reveal-items[@selector='.product-list > *']"
        next_btn ="//button[@id='gsloadmore']"
        self.driver.get(url_vaporizers)
        self.driver.maximize_window()
        product_urls_list = []
        try:
            wait = WebDriverWait(self.driver, 10)
            iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='fancyboxAge-iframe']")))
            self.driver.switch_to.frame(iframe)
            yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='enter']")))
            yes_button.click()
            self.driver.switch_to.default_content()
        except TimeoutException:
            pass
        next = True
        while next is True:
            print("next loop")
            time.sleep(2)

            try:
                # Find the element
                next_page = self.driver.find_element(By.XPATH,next_btn)
                # Get the dimensions of the viewport
                viewport_width = self.driver.execute_script("return window.innerWidth;")
                viewport_height = self.driver.execute_script("return window.innerHeight;")
                # Get the location of the element
                element_x = next_page.location["x"]
                element_y = next_page.location["y"]
                element_width = next_page.size["width"]
                element_height = next_page.size["height"]
                # Calculate the scroll position to center the element
                scroll_x = element_x - (viewport_width / 2) + (element_width / 2)
                scroll_y = element_y - (viewport_height / 2) + (element_height / 2)
                # Scroll to the calculated position
                self.driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", scroll_x, scroll_y)
                time.sleep(2)
                next_page.click()
                next = True
            except:
                print("false")
                next = False
        wait.until(EC.presence_of_element_located((By.XPATH, product_frame)))
        element = self.driver.find_element(By.XPATH,product_frame)
        option_elements = element.find_elements(By.XPATH,
                                                '//body[1]/main[1]/section[2]/div[1]/div[1]/div[3]/div[1]/reveal-items[1]/product-list[1]/product-card[*]/div[2]/a[1]')
        for product in option_elements:
            a = product.get_attribute('href')
            product_urls_list.append(str(a))
            print(product_urls_list)
        return product_urls_list

    def cbdr_pl_get_urls(self):
        url_vaporizers = "https://URL"
        product_frame = "//div[@id='box_mainproducts']//div[@class='innerbox']"
        pagin = "//body[1]/div[2]/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/ul[1]/li[*]/a[1]"

        self.driver.get(url_vaporizers)
        self.driver.maximize_window()
        product_urls_list = []
        paginator = self.driver.find_elements(By.XPATH,pagin)
        print(len(paginator))
        paginato_len = len(paginator)

        i = 1
        for page in range(paginato_len):
            i+=1
            element = self.driver.find_element(By.XPATH,product_frame)
            option_elements = element.find_elements(By.XPATH,"//body[1]/div[2]/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[*]/div[1]/a[1]")
            option_elements_len= len(option_elements)
            if option_elements_len > 0 :
                print(option_elements)
                for product in option_elements:
                    a = product.get_attribute('href')
                    product_urls_list.append(a)
                    print(product_urls_list)
                self.driver.get(str(url_vaporizers) + "/" + str(i))
            else:
                option_elements = element.find_elements(By.XPATH,
                                                        "//body[1]/div[2]/div[4]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[*]/div[1]/a[1]")
                for product in option_elements:
                    a = product.get_attribute('href')
                    product_urls_list.append(a)
                    print(product_urls_list)
                self.driver.get(str(url_vaporizers) + "/" + str(i))
        return product_urls_list

    def cbdr_com_get_urls(self):
        url_vaporizers = "https://URL"
        product_frame = "//div[@id='box_mainproducts']//div[@class='innerbox']"
        pagin = "//body[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/ul[1]/li[*]/a[1]"

        self.driver.get(url_vaporizers)
        self.driver.maximize_window()
        product_urls_list = []
        paginator = self.driver.find_elements(By.XPATH,pagin)
        print(len(paginator))
        paginato_len = len(paginator)
        i =1
        for page in range(paginato_len):
            i += 1
            element = self.driver.find_element(By.XPATH,product_frame)
            option_elements = element.find_elements(By.XPATH,
                                                    "//body[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[*]/div[1]/a[1]")
            option_elements_len = len(option_elements)
            if option_elements_len > 0:
                print(option_elements)
                for product in option_elements:
                    a = product.get_attribute('href')
                    product_urls_list.append(a)
                    print(product_urls_list)
                self.driver.get(str(url_vaporizers) + "/" + str(i))
            else:
                option_elements = element.find_elements(By.XPATH,
                                                        "//body[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[*]/div[1]/a[1]")
                for product in option_elements:
                    a = product.get_attribute('href')
                    product_urls_list.append(a)
                    print(product_urls_list)
                self.driver.get(str(url_vaporizers) + "/" + str(i))

        print(product_urls_list)
        return product_urls_list

    def vuj_com_get_urls(self):
        url_vaporizers = "https://URL"
        product_frame = "//body[1]/div[3]/main[1]/div[3]/div[1]/div[2]/div[2]"
        next_btn ="//body[1]/div[3]/main[1]/div[3]/div[1]/div[2]/div[3]/div[2]/ul[1]/li[3]/a[1]"
        self.driver.get(url_vaporizers)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)
        product_urls_list = []
        next = True
        while next is True:
            print("next loop")
            time.sleep(2)
            wait.until(EC.presence_of_element_located((By.XPATH, product_frame)))
            element = self.driver.find_element(By.XPATH,product_frame)
            option_elements = element.find_elements(By.XPATH,'//body[1]/div[3]/main[1]/div[3]/div[1]/div[2]/div[2]/ol[1]/li[*]/div[1]/div[1]/a[1]')

            for product in option_elements:
                a = product.get_attribute('href')
                product_urls_list.append(a)
                print(product_urls_list)
            try:
                # Find the element
                next_page = self.driver.find_element(By.XPATH,next_btn)
                # Get the dimensions of the viewport
                viewport_width = self.driver.execute_script("return window.innerWidth;")
                viewport_height = self.driver.execute_script("return window.innerHeight;")
                # Get the location of the element
                element_x = next_page.location["x"]
                element_y = next_page.location["y"]
                element_width = next_page.size["width"]
                element_height = next_page.size["height"]
                # Calculate the scroll position to center the element
                scroll_x = element_x - (viewport_width / 2) + (element_width / 2)
                scroll_y = element_y - (viewport_height / 2) + (element_height / 2)
                # Scroll to the calculated position
                self.driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", scroll_x, scroll_y)
                time.sleep(2)
                next_page.click()
                next = True
            except:
                print("false")
                next = False
        return product_urls_list

    def vuj_pl_get_urls(self):
        url_vaporizers = "https://URL"
        product_frame = "//body[1]/div[3]/main[1]/div[3]/div[1]/div[2]/div[2]"
        next_btn ="//body[1]/div[3]/main[1]/div[3]/div[1]/div[2]/div[3]/div[2]/ul[1]/li[3]/a[1]"
        self.driver.get(url_vaporizers)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)
        product_urls_list = []

        next = True
        while next is True:
            print("next loop")
            time.sleep(2)
            wait.until(EC.presence_of_element_located((By.XPATH, product_frame)))
            element = self.driver.find_element(By.XPATH,product_frame)
            option_elements = element.find_elements(By.XPATH,'//body[1]/div[3]/main[1]/div[3]/div[1]/div[2]/div[2]/ol[1]/li[*]/div[1]/div[1]/a[1]')

            for product in option_elements:
                a = product.get_attribute('href')
                product_urls_list.append(a)
                print(product_urls_list)
            try:
                # Find the element
                next_page = self.driver.find_element(By.XPATH,next_btn)
                # Get the dimensions of the viewport
                viewport_width = self.driver.execute_script("return window.innerWidth;")
                viewport_height = self.driver.execute_script("return window.innerHeight;")
                # Get the location of the element
                element_x = next_page.location["x"]
                element_y = next_page.location["y"]
                element_width = next_page.size["width"]
                element_height = next_page.size["height"]
                # Calculate the scroll position to center the element
                scroll_x = element_x - (viewport_width / 2) + (element_width / 2)
                scroll_y = element_y - (viewport_height / 2) + (element_height / 2)
                # Scroll to the calculated position
                self.driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", scroll_x, scroll_y)
                time.sleep(2)
                next_page.click()
                next = True
            except:
                print("false")
                next = False
        return product_urls_list

    def mv_com_get_urls(self):
        url_vaporizers_p = "https://URL"
        url_vaporizers_s ="https://URL"
        product_frame = "//ol[@id='vapefilter-all']"
        self.driver.get(url_vaporizers_p)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)
        product_urls_list = []
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, product_frame)))
        element = self.driver.find_element(By.XPATH,product_frame)
        option_elements = element.find_elements(By.XPATH,'//body[1]/div[2]/main[1]/div[6]/div[1]/div[2]/ol[1]/li[*]/div[1]/a[1]')
        for product in option_elements:
            a = product.get_attribute('href')
            product_urls_list.append(a)
            print(product_urls_list)
        self.driver.get(url_vaporizers_s)
        element = self.driver.find_element(By.XPATH,product_frame)
        option_elements = element.find_elements(By.XPATH,'//body[1]/div[2]/main[1]/div[6]/div[1]/div[2]/ol[1]/li[*]/div[1]/a[1]')
        for product in option_elements:
            a = product.get_attribute('href')
            product_urls_list.append(a)
            print(product_urls_list)
        return product_urls_list

    def mv_de_get_urls(self):
        url_vaporizers_p = "https://URL"
        url_vaporizers_s ="https://URL"
        product_frame = "//ol[@id='vapefilter-all']"
        self.driver.get(url_vaporizers_p)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)
        product_urls_list = []
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, product_frame)))
        element = self.driver.find_element(By.XPATH,product_frame)
        option_elements = element.find_elements(By.XPATH,'//body[1]/div[2]/main[1]/div[6]/div[1]/div[2]/ol[1]/li[*]/div[1]/a[1]')
        for product in option_elements:
            a = product.get_attribute('href')
            product_urls_list.append(a)
            print(product_urls_list)
        self.driver.get(url_vaporizers_s)
        element = self.driver.find_element(By.XPATH,product_frame)
        option_elements = element.find_elements(By.XPATH,'//body[1]/div[2]/main[1]/div[6]/div[1]/div[2]/ol[1]/li[*]/div[1]/a[1]')
        for product in option_elements:
            a = product.get_attribute('href')
            product_urls_list.append(a)
            print(product_urls_list)
        return product_urls_list
    def mv_nl_get_urls(self):
        url_vaporizers_p = "https://URL"
        url_vaporizers_s ="https://URL"
        product_frame = "//ol[@id='vapefilter-all']"

        self.driver.get(url_vaporizers_p)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)
        product_urls_list = []
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, product_frame)))
        element = self.driver.find_element(By.XPATH,product_frame)
        # option_elements = element.find_elements(By.XPATH,'//body[1]/div[2]/main[1]/div[6]/div[1]/div[2]/ol[1]/li[*]/div[1]/a[1]')
        option_elements = element.find_elements(By.XPATH,'//body[1]/div[2]/main[1]/div[7]/div[1]/div[2]/ol[1]/li[*]/div[1]/a[1]')
        for product in option_elements:
            a = product.get_attribute('href')
            product_urls_list.append(a)
            print(product_urls_list)
        self.driver.get(url_vaporizers_s)
        element = self.driver.find_element(By.XPATH,product_frame)
        option_elements = element.find_elements(By.XPATH,'//body[1]/div[2]/main[1]/div[6]/div[1]/div[2]/ol[1]/li[*]/div[1]/a[1]')
        for product in option_elements:
            a = product.get_attribute('href')
            product_urls_list.append(a)
            print(product_urls_list)
        return product_urls_list

    def mv_sk_get_urls(self):
        url_vaporizers_p = "https://URL"
        url_vaporizers_s ="https://URL"
        product_frame = "//ol[@id='vapefilter-all']"
        self.driver.get(url_vaporizers_p)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)
        product_urls_list = []
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, product_frame)))
        element = self.driver.find_element(By.XPATH,product_frame)
        option_elements = element.find_elements(By.XPATH,'//body[1]/div[2]/main[1]/div[6]/div[1]/div[2]/ol[1]/li[*]/div[1]/a[1]')
        for product in option_elements:
            a = product.get_attribute('href')
            product_urls_list.append(a)
            print(product_urls_list)
        self.driver.get(url_vaporizers_s)
        element = self.driver.find_element(By.XPATH,product_frame)
        option_elements = element.find_elements(By.XPATH,'//body[1]/div[2]/main[1]/div[6]/div[1]/div[2]/ol[1]/li[*]/div[1]/a[1]')
        for product in option_elements:
            a = product.get_attribute('href')
            product_urls_list.append(a)
            print(product_urls_list)
        return product_urls_list

    def mv_it_get_urls(self):
        url_vaporizers_p = "https://URL"
        url_vaporizers_s ="https://URL"
        product_frame = "//ol[@id='vapefilter-all']"
        self.driver.get(url_vaporizers_p)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)
        product_urls_list = []
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, product_frame)))
        element = self.driver.find_element(By.XPATH,product_frame)
        option_elements = element.find_elements(By.XPATH,'//body[1]/div[2]/main[1]/div[6]/div[1]/div[2]/ol[1]/li[*]/div[1]/a[1]')
        for product in option_elements:
            a = product.get_attribute('href')
            product_urls_list.append(a)
            print(product_urls_list)
        self.driver.get(url_vaporizers_s)
        element = self.driver.find_element(By.XPATH,product_frame)
        option_elements = element.find_elements(By.XPATH,'//body[1]/div[2]/main[1]/div[6]/div[1]/div[2]/ol[1]/li[*]/div[1]/a[1]')
        for product in option_elements:
            a = product.get_attribute('href')
            product_urls_list.append(a)
            print(product_urls_list)
        return product_urls_list

    def mv_es_get_urls(self):
        url_vaporizers_p = "https://URL"
        url_vaporizers_s = "https://URL"
        product_frame = "//ol[@id='vapefilter-all']"
        self.driver.get(url_vaporizers_p)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)
        product_urls_list = []
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, product_frame)))
        element = self.driver.find_element(By.XPATH,product_frame)
        option_elements = element.find_elements(By.XPATH,
                                                '//body[1]/div[2]/main[1]/div[6]/div[1]/div[2]/ol[1]/li[*]/div[1]/a[1]')

        for product in option_elements:
            a = product.get_attribute('href')
            product_urls_list.append(a)
            print(product_urls_list)
        self.driver.get(url_vaporizers_s)
        element = self.driver.find_element(By.XPATH,product_frame)
        option_elements = element.find_elements(By.XPATH,
                                                '//body[1]/div[2]/main[1]/div[6]/div[1]/div[2]/ol[1]/li[*]/div[1]/a[1]')
        for product in option_elements:
            a = product.get_attribute('href')
            product_urls_list.append(a)
            print(product_urls_list)
        return product_urls_list

    def vn_com_get_urls(self):
        url_vaporizers = "https://URL"
        product_frame = "//div[@id='result-wrapper']"
        next_btn = "//li[contains(@class,'next')]//a"
        self.driver.get(url_vaporizers)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)
        product_urls_list = []
        #Age handler
        yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='fskYes']")))
        yes_button.click()
        # cookies accept handler
        yes_button2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='cbtn cbtn-secondary bugmenot']")))
        yes_button2.click()
        yes_button3 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ws_oss_close']")))
        yes_button3.click()
        next = True
        while next is True:
            time.sleep(2)
            # wait.until(EC.presence_of_element_located((By.XPATH, product_frame)))
            # element = self.driver.find_element_by_xpath(product_frame)
            option_elements = self.driver.find_elements(By.XPATH,'//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[4]/div[*]/div[1]/a[1]')
            for product in option_elements:
                a = product.get_attribute('href')
                product_urls_list.append(a)
                print(product_urls_list)
            try:
                # Find the element
                next_page = self.driver.find_element(By.XPATH,next_btn)
                # Get the dimensions of the viewport
                viewport_width = self.driver.execute_script("return window.innerWidth;")
                viewport_height = self.driver.execute_script("return window.innerHeight;")
                # Get the location of the element
                element_x = next_page.location["x"]
                element_y = next_page.location["y"]
                element_width = next_page.size["width"]
                element_height = next_page.size["height"]
                # Calculate the scroll position to center the element
                scroll_x = element_x - (viewport_width / 2) + (element_width / 2)
                scroll_y = element_y - (viewport_height / 2) + (element_height / 2)
                # Scroll to the calculated position
                self.driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", scroll_x, scroll_y)
                time.sleep(2)
                next_page.click()
                next = True
            except:
                print("false")
                next = False
        return product_urls_list

    def quit_driver(self):
        print("quit")
        self.driver.quit()