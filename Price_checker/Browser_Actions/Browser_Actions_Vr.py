
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

class BrowserActionsVr:

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
        variant_selector = "//body[1]/main[1]/section[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/ul[1]/li[*]"
        try:
            wait = WebDriverWait(self.driver, 1)
            wait.until(EC.element_to_be_clickable((By.XPATH, variant_selector)))
            variant_elements = self.driver.find_elements(By.XPATH,variant_selector)

            return(len(variant_elements))
        except TimeoutException:
            return(0)

    def take_variable_product_price(self):
        selector = "//span[@class='product-price current-price-value']"
        selector2 = "//span[@class='regular-price']"
        variant_selector = "//body[1]/main[1]/section[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/ul[1]/li[*]"
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, variant_selector)))
        variant_elements = self.driver.find_elements(By.XPATH,variant_selector)
        variant_prices_and_name = []
        flag = False
        try:
            for i, variant_element in enumerate(variant_elements, start=1):
                if flag == True:
                    wait = WebDriverWait(self.driver, 3)
                    wait.until(EC.visibility_of_element_located((By.XPATH, "//body[1]/main[1]/section[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/ul[1]/li["+str(i)+"]")))
                    variant_el = self.driver.find_element(By.XPATH,"//body[1]/main[1]/section[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/ul[1]/li["+str(i)+"]/input[1]")
                    self.driver.execute_script("arguments[0].click();", variant_el)
                try:
                    time.sleep(0.5)
                    wait = WebDriverWait(self.driver, 3)
                    wait.until(EC.visibility_of_element_located((By.XPATH, selector)))
                    element1 = self.driver.find_element(By.XPATH,selector)
                    element2 = self.driver.find_element(By.XPATH,selector2)
                    variant_names = self.driver.find_element(By.XPATH,"//body[1]/main[1]/section[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/ul[1]/li["+str(i)+"]/span[1]/span[1]")
                    variant_prices_and_name.append([element1.text,variant_names.text,element2.text])
                    flag = True
                except NoSuchElementException:
                    wait = WebDriverWait(self.driver, 3)
                    wait.until(EC.visibility_of_element_located((By.XPATH, selector)))
                    element = self.driver.find_element(By.XPATH,selector)
                    variant_names = self.driver.find_element(By.XPATH,"//body[1]/main[1]/section[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/ul[1]/li["+str(i)+"]/span[1]/span[1]")
                    variant_prices_and_name.append([element.text, variant_names.text])
                    flag = True
        except:
            wait = WebDriverWait(self.driver, 2)
            pn = wait.until(EC.visibility_of_element_located((By.XPATH, "//body[1]/main[1]/section[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/ul[1]/li["+str(i)+"]/span[1]/span[1]")))
            product_name = pn.text
            variant_prices_and_name.append(["Nie mogłem pobrać", str(product_name)])
            print(variant_prices_and_name)
            pass
        print(variant_prices_and_name)
        return (variant_prices_and_name)

    def take_simple_product_price(self):
        selector = "//span[@class='product-price current-price-value']"
        selector2 = "//span[@class='regular-price']"
        try:
            try:
                wait = WebDriverWait(self.driver,1)
                wait.until(EC.visibility_of_element_located((By.XPATH,selector)))
                element1 =self.driver.find_element(By.XPATH,selector)
                element2 =self.driver.find_element(By.XPATH,selector2)
                print(element1.text,element2.text)
                return([element1.text, element2.text])
            except NoSuchElementException:
                wait = WebDriverWait(self.driver,2)
                wait.until(EC.visibility_of_element_located((By.XPATH,selector)))
                element = self.driver.find_element(By.XPATH,selector)
                print(element.text)
                return (element.text)
        except:
            return("Nie mogłem pobrać produktu")

    def find_element_title(self):
        selector_nazwy = "//h1[@class='h1 page-title']"
        element = self.driver.find_element(By.XPATH,selector_nazwy)
        return (element.text)

    def veryf_handler(self):
        try:
            wait = WebDriverWait(self.driver, 2)
            yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='iqitcookielaw-accept']")))
            yes_button.click()
        except:
            pass

    def quit_driver(self):
        print("quit")
        self.driver.quit()

