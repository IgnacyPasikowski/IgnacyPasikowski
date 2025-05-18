
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class BrowserActionsVs:
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
        variant_selector = "//label[@class='media-swatch  border']"
        try:
            wait = WebDriverWait(self.driver, 1)
            wait.until(EC.visibility_of_element_located((By.XPATH, variant_selector)))
            variant_elements = self.driver.find_elements(By.XPATH,variant_selector)

            return(len(variant_elements))
        except TimeoutException:
            return(0)

    def take_variable_product_price(self):
        selector = "//sale-price[@class='text-lg text-on-sale']//span[@class='money']"
        selector2 = "//sale-price[@class='text-lg']//span[@class='money']"
        selector3 = "//price-list[contains(@class,'price-list price-list--lg')]//compare-at-price[@class='text-subdued line-through']//span[@class='money']"
        variant_selector = "//label[@class='media-swatch  border']"
        variant_name = "//variant-option-value[@for='option1']"
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, variant_selector)))
        variant_elements = self.driver.find_elements(By.XPATH,variant_selector)
        variant_prices_and_name = []
        try:
            for variant_element in variant_elements:
                variant_element.click()
                try:
                    wait = WebDriverWait(self.driver, 1)
                    wait.until(EC.visibility_of_element_located((By.XPATH, selector)))

                    element1 = self.driver.find_element(By.XPATH,selector)
                    element2 = self.driver.find_element(By.XPATH,selector3)
                    variant_names = self.driver.find_element(By.XPATH,variant_name)
                    variant_prices_and_name.append([element1.text,variant_names.text,element2.text])
                except TimeoutException:
                    wait = WebDriverWait(self.driver, 2)
                    wait.until(EC.visibility_of_element_located((By.XPATH, selector2)))
                    element = self.driver.find_element(By.XPATH,selector2)
                    variant_names = self.driver.find_element(By.XPATH,variant_name)
                    variant_prices_and_name.append([element.text, variant_names.text])
        except:

            wait = WebDriverWait(self.driver, 2)
            pn = wait.until(EC.visibility_of_element_located((By.XPATH, variant_name)))
            product_name = pn.text
            variant_prices_and_name.append(["Nie mogłem pobrać", str(product_name)])
            print(variant_prices_and_name)
            pass

        print(variant_prices_and_name)
        return (variant_prices_and_name)

    def take_simple_product_price(self):
        selector = "//sale-price[@class='text-lg text-on-sale']//span[@class='money']"
        selector2 = "//sale-price[@class='text-lg']//span[@class='etrans-money']"
        selector3 ="//price-list[contains(@class,'price-list price-list--lg')]//compare-at-price[@class='text-subdued line-through']//span[@class='money']"
        try:
            try:
                wait = WebDriverWait(self.driver,1)
                wait.until(EC.visibility_of_element_located((By.XPATH,selector)))
                element1 =self.driver.find_element(By.XPATH,selector)
                element2 =self.driver.find_element(By.XPATH,selector3)
                print(element1.text,element2.text)
                return([element1.text, element2.text])
            except TimeoutException:
                wait = WebDriverWait(self.driver,2)
                wait.until(EC.visibility_of_element_located((By.XPATH,selector2)))
                element = self.driver.find_element(By.XPATH,selector2)

                print(element.text)
                return (element.text)
        except:

            return("Nie mogłem pobrać")

    def find_element_title(self):
        selector_nazwy = "//h1[@class='product-info__title h2']"
        element = self.driver.find_element(By.XPATH,selector_nazwy)
        return (element.text)

    def veryf_handler(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='fancyboxAge-iframe']")))
            self.driver.switch_to.frame(iframe)
            yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='enter']")))
            yes_button.click()
            self.driver.switch_to.default_content()
        except TimeoutException:
            pass

    def quit_driver(self):
        print("quit")
        self.driver.quit()

