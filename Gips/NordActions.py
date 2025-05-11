import gspread
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

class NordActions:
    driver = None

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    def driver_get(self, URL):
        self.driver.get(URL)
        self.driver.maximize_window()
    def crawl_through_cat(self):
        # ten jest do gipsowej
        # cat_list ="//div[@id='div_block-4-1278']/a[*]"
        # ten jest do elewacyjnej
        cat_list ="//div[@id='div_block-8-1280']/a[*]"
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.XPATH, cat_list)))
        list = self.driver.find_elements(By.XPATH,cat_list)
        cat_urls = []
        print(len(list))
        for cat in list:
            a = cat.get_attribute('href')
            cat_name =cat.text
            cat_urls.append([str(a),cat_name])
            print(a,cat_name)
        return cat_urls


    def crawl_through_prod(self):
        # Ten jest do gips
        # prod_list = "//body/section[@id='section-2-1282']/div[1]/div[1]/div[2]/div[1]/ul[1]/li[*]/a[1]"
        # ten jest do elewacyjnej
        prod_list = "//body/section[@id='section-2-1291']/div[1]/div[1]/div[2]/div[1]/ul[1]/li[*]/a[1]"
        next_page_btn = "//a[@class='next page-numbers']"
        cat_xpath = "//h1[@class='page-title']"
        wait = WebDriverWait(self.driver, 15)
        cat_name = wait.until(EC.presence_of_element_located((By.XPATH, cat_xpath)))
        cat = cat_name.text
        product_url = [cat]
        next = True
        while next is True:
            wait.until(EC.presence_of_element_located((By.XPATH, prod_list)))
            list = self.driver.find_elements(By.XPATH, prod_list)
            for product in list:
                print(product)

                a = product.get_attribute('href')
                print(str(a))
                product_url.append(str(a))


            try:
                next_page = self.driver.find_element(By.XPATH,next_page_btn)
                next_page.click()
                next = True
            except:
                print("Brak next buttona")
                next = False

        return(product_url)

    def take_product(self,URL):

        self.driver.get(URL)
        self.driver.maximize_window()

        prod_name = "//h1[@id='-product-title-10-1286']"
        prod_desc = "//div[@id='-product-description-11-1286']"
        prod_price = "//body[1]/section[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/p[1]/span[1]/bdi[1]"
        wait = WebDriverWait(self.driver, 15)
        name = wait.until(EC.presence_of_element_located((By.XPATH, prod_name)))
        desc = wait.until(EC.presence_of_element_located((By.XPATH, prod_desc)))
        price = wait.until(EC.presence_of_element_located((By.XPATH, prod_price)))
        prod = [name.text,desc.text,price.text]
        print(prod)
        return(prod)

    def take_product_photo(self,URL):

        self.driver.get(URL)
        self.driver.maximize_window()

        prod_name = "//h1[@id='-product-title-10-1286']"
        photo_set_url = "/html[1]/body[1]/section[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/img[1]"
        single_photo_url = "/html[1]/body[1]/section[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]"
        wait = WebDriverWait(self.driver, 15)
        name = wait.until(EC.presence_of_element_located((By.XPATH, prod_name)))
        wait = WebDriverWait(self.driver, 2)
        try:
            photo = wait.until(EC.presence_of_element_located((By.XPATH, photo_set_url)))
            photo = photo.get_attribute("srcset")

        except TimeoutException:
            photo = wait.until(EC.presence_of_element_located((By.XPATH, single_photo_url)))
            photo = photo.get_attribute("src")


        prod = [name.text,photo]
        print(prod)
        return(prod)








