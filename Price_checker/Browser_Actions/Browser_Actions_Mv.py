
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

class BrowserActionsMv:
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
        variant_selector = "//body[1]/div[2]/main[1]/div[5]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/ul[1]"
        variant_selector_len = "//body[1]/div[2]/main[1]/div[5]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/ul[1]/li[*]"
        try:
            wait = WebDriverWait(self.driver, 1)
            wait.until(EC.visibility_of_element_located((By.XPATH, variant_selector)))
            variant_elements = self.driver.find_elements(By.XPATH,variant_selector_len)
            print("var "+str(len(variant_elements)))
            return(len(variant_elements))
        except NoSuchElementException:
            return(0)
        except TimeoutException:
            return(0)

    def check_if_variant_kit(self):
        variant_selector_main = "//body[1]/div[2]/main[1]/div[5]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[*]/label[1]"
        try:
            wait = WebDriverWait(self.driver, 1)
            wait.until(EC.visibility_of_element_located((By.XPATH, variant_selector_main)))
            variant_elements = self.driver.find_elements(By.XPATH,variant_selector_main)
            print("kit "+str(len(variant_elements)))
            return(len(variant_elements))
        except TimeoutException:
            print(0)
            return(0)

    def take_variable_product_price(self):
        selector_sale_price = "//span[@class='price-wrapper price']//span[@class='price']"
        selector_base_price = "//span[@class='price-wrapper price']//span[@class='price']"
        selector_base_price_while_on_sale = "//span[@class='old-price map-old-price base']//span[@class='price-wrapper price ']"
        variant_selector = "//body[1]/div[2]/main[1]/div[5]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/ul[1]"
        variant_selector_len = "//body[1]/div[2]/main[1]/div[5]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/ul[1]/li[*]"
        variant_name = "//body[1]/div[2]/main[1]/div[5]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/fieldset[1]/div[1]/label[1]/span[2]"
        variant_name_if_no_variant = "//body[1]/div[2]/main[1]/div[5]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/ul[1]/li[*]/div[1]/a[1]/label[1]"

        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, variant_selector)))
        variant_elements = self.driver.find_elements(By.XPATH,variant_selector_len)
        variant_prices_and_name = []
        i =0
        for variant_element in variant_elements:
            i +=1
            variant_element.click()
            try:
                wait = WebDriverWait(self.driver, 1)
                wait.until(EC.visibility_of_element_located((By.XPATH, selector_sale_price)))
                element1 = self.driver.find_element(By.XPATH,selector_sale_price)
                element2 = self.driver.find_element(By.XPATH,selector_base_price_while_on_sale)
                variant_names = self.driver.find_element(By.XPATH,variant_name)
                variant_prices_and_name.append([element1.text,variant_names.text,element2.text])
            except NoSuchElementException:
                wait = WebDriverWait(self.driver, 2)
                wait.until(EC.visibility_of_element_located((By.XPATH, selector_base_price)))
                element = self.driver.find_element(By.XPATH,selector_base_price)
                variant_names = self.driver.find_element(By.XPATH,"//body[1]/div[2]/main[1]/div[5]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/ul[1]/li["+str(i)+"]")
                variant_prices_and_name.append([element.text, variant_names.text])
        print(variant_prices_and_name)
        return (variant_prices_and_name)

    def take_variable_kit_product_price(self):
        selector_sale_price = "//span[@class='price-wrapper price']//span[@class='price']"
        selector_base_price = "//span[@class='price-wrapper price']//span[@class='price']"
        selector_base_price_while_on_sale = "//span[@class='old-price map-old-price base']//span[@class='price-wrapper price ']"
        variant_selector_len = "//body[1]/div[2]/main[1]/div[5]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/ul[1]/li[*]"
        kit_selector = "//body[1]/div[2]/main[1]/div[5]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[*]/label[1]"
        variant_name = "//body[1]/div[2]/main[1]/div[5]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/fieldset[1]/div[1]/label[1]/span[2]"
        variant_name = "//label[@class='label color-label']/span[2]"
        actions = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.element_to_be_clickable((By.XPATH, kit_selector)))
        kit_element = self.driver.find_elements(By.XPATH,kit_selector)
        variant_prices_and_name = []
        try:
            for swithes in kit_element:
                print(swithes)
                swithes.click()
                variant_elements = self.driver.find_elements(By.XPATH,variant_selector_len)
                for variant_element in variant_elements:
                    try:
                        variant_element.click()
                    except ElementNotInteractableException:
                        continue
                    time.sleep(1)
                    print(variant_element.text)
                    # Wykonaj operacje na danym elemencie, np. wybierz go
                    wait = WebDriverWait(self.driver, 1)
                    wait.until(EC.visibility_of_element_located((By.XPATH, selector_sale_price)))
                    element1 = self.driver.find_element(By.XPATH,selector_sale_price)
                    element2 = self.driver.find_element(By.XPATH,selector_base_price_while_on_sale)
                    variant_kit_name = swithes
                    variant_names = self.driver.find_element(By.XPATH,variant_name)
                    variant_prices_and_name.append(
                        [element1.text, str(variant_kit_name.text) + " " + str(variant_names.text), element2.text])
        except NoSuchElementException:
            for swithes in kit_element:
                print(swithes)
                swithes.click()
                variant_elements = self.driver.find_elements(By.XPATH,variant_selector_len)
                for variant_element in variant_elements:
                    try:
                        variant_element.click()
                    except ElementNotInteractableException:
                        continue
                    time.sleep(1)
                    print(variant_element.text)
                    # Wykonaj operacje na danym elemencie, np. wybierz go
                    wait = WebDriverWait(self.driver, 1)
                    wait.until(EC.visibility_of_element_located((By.XPATH, selector_base_price)))
                    element1 = self.driver.find_element(By.XPATH,selector_base_price)
                    variant_kit_name = swithes
                    variant_names = self.driver.find_element(By.XPATH,variant_name)
                    variant_prices_and_name.append(
                        [element1.text, str(variant_kit_name.text) + " " + str(variant_names.text)])
        print(variant_prices_and_name)
        return (variant_prices_and_name)

    def take_only_kit_product_price(self):
        selector_base_price = "//span[@class='price-wrapper price']//span[@class='price']"
        kit_selector = "//body[1]/div[2]/main[1]/div[5]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/ul[1]/li[*]"
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.element_to_be_clickable((By.XPATH, kit_selector)))
        kit_element = self.driver.find_elements(By.XPATH,kit_selector)
        variant_prices_and_name = []
        for swithes in kit_element:
            print(swithes)
            swithes.click()
            wait = WebDriverWait(self.driver, 1)
            wait.until(EC.visibility_of_element_located((By.XPATH, selector_base_price)))
            element1 = self.driver.find_element(By.XPATH,selector_base_price)
            variant_kit_name = swithes
            variant_prices_and_name.append(
                [element1.text, str(variant_kit_name.text)])
        print(variant_prices_and_name)
        return (variant_prices_and_name)

    def take_simple_product_price(self):
        selector_sale_price = "//span[@class='price-container price-final_price tax weee']"
        selector_base_price = "//span[@class='price-container price-final_price tax weee']"
        selector_base_price_while_on_sale = "//span[@class='old-price map-old-price base']//span[@class='price-wrapper price ']"

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

    def find_element_title(self):
        selector_nazwy = "//span[@class='base']"
        element = self.driver.find_element(By.XPATH,selector_nazwy)
        return (element.text)

    def quit_driver(self):
        print("quit")
        self.driver.quit()

