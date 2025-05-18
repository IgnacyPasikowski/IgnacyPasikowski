
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

class BrowserActionsVuj:
    driver= None
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--headless=new')
        self.driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    def driver_get(self, URL):
        self.driver.get(URL)
        self.driver.maximize_window()

    def check_if_variant(self):
        variant_field= "//select[@id='attribute92']"
        try:
            select_element = self.driver.find_element(By.XPATH, variant_field)
            option_elements = select_element.find_elements('tag name', 'option')
            variant_elements = len(option_elements)
            print("Number of options:", variant_elements)
            return(variant_elements)
        except NoSuchElementException:
            return(0)

    def take_variable_product_price(self):
        selector_sale_price = "//span[@class='normal-price']//span[@class='price']"
        selector_base_price = "//span[@class='price']"
        selector_base_price_while_on_sale = "//span[@class='old-price sly-old-price no-display']//span[@class='price']"
        variant_selector = "//select[@id='attribute92']"
        variant_field = "//select[@id='attribute92']"
        variant_name = "//select[@id='attribute92']/option"
        # Find the select element with id 'attribute92'
        select_element = self.driver.find_element(By.XPATH,variant_field)
        # Find all the option elements within the select element
        option_elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH,variant_name )))
        variant_prices_and_name = []
        for option_element in option_elements:
            option_element.click()
            try:
                wait = WebDriverWait(self.driver, 2)
                wait.until(EC.visibility_of_element_located((By.XPATH, selector_sale_price)))

                element1 = self.driver.find_element(By.XPATH,selector_sale_price)
                element2 = self.driver.find_element(By.XPATH,selector_base_price_while_on_sale)
                variant_names = option_element
                variant_prices_and_name.append([element1.text,variant_names.text,element2.text])
            except NoSuchElementException:
                wait = WebDriverWait(self.driver, 2)
                wait.until(EC.visibility_of_element_located((By.XPATH, selector_base_price)))
                element = self.driver.find_element(By.XPATH,selector_base_price)
                variant_names = option_element
                variant_prices_and_name.append([element.text, variant_names.text])

        print(variant_prices_and_name)
        return (variant_prices_and_name)

    def take_simple_product_price(self):
        selector_sale_price = "//span[@class='special-price']//span[@class='price']"
        selector_base_price = "//span[@class='price']"
        selector_base_price_while_on_sale ="//span[@class='old-price']//span[@class='price']"
        try:
            try:
                wait = WebDriverWait(self.driver,1)
                wait.until(EC.visibility_of_element_located((By.XPATH,selector_sale_price)))
                element1 =self.driver.find_element(By.XPATH,selector_sale_price)
                element2 =self.driver.find_element(By.XPATH,selector_base_price_while_on_sale)
                print(element1.text,element2.text)
                return([element1.text, element2.text])
            except TimeoutException:
                wait = WebDriverWait(self.driver,2)
                wait.until(EC.visibility_of_element_located((By.XPATH,selector_base_price)))
                element = self.driver.find_element(By.XPATH,selector_base_price)

                print(element.text)
                return (element.text)
        except:
            return("")

    def find_element_title(self):
        selector_nazwy = "//span[@class='base']"
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

