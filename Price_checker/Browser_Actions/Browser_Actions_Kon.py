
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class BrowserActionsKon:

    driver= None
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--headless=new')
        self.driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    def driver_get(self, URL):
        self.driver.get(URL)
        self.driver.maximize_window()

    def take_simple_product_price(self):
        selector_sale_price = "//section[@id='main']//div[@itemprop='price']"
        selector_base_price = "//section[@id='main']//div[@itemprop='price']"
        selector_base_price_while_on_sale ="//div[@class='col-12 col-lg-6 col-xl-6 d-flex flex-wrap ps-lg-2']//span[@class='regular-price']"
        try:
            try:
                wait = WebDriverWait(self.driver,1)
                wait.until(EC.visibility_of_element_located((By.XPATH,selector_sale_price)))
                element1 =self.driver.find_element(By.XPATH,selector_sale_price)
                element2 =self.driver.find_element(By.XPATH,selector_base_price_while_on_sale)
                print(element1.text,element2.text)
                return([element1.text, element2.text])
            except NoSuchElementException:
                wait = WebDriverWait(self.driver,2)
                wait.until(EC.visibility_of_element_located((By.XPATH,selector_base_price)))
                element = self.driver.find_element(By.XPATH,selector_base_price)
                print(element.text)
                return (element.text)
        except NoSuchElementException:
            print("URL error")
            pass

    def find_element_title(self):
        selector_nazwy = "//h1[@itemprop='name']"
        element = self.driver.find_element(By.XPATH,selector_nazwy)
        return (element.text)

    def veryf_handler(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='fancyboxAge-iframe']")))
            self.driver.switch_to.frame(iframe)
            yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='enter']")))
            yes_button.click()
            self.driver.switch_to.default_content()
        except:
            pass

    def quit_driver(self):
        print("quit")
        self.driver.quit()

    def choose_eur_currency(self):
        switch_to_eur ="//a[@title='Euro']"
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, switch_to_eur)))
        element.click()





