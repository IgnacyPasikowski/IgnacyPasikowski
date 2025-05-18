from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class BrowserActionsVn:
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
        first_dd_oppen = "//span[@class='filter-option pull-left']"
        first_field_variants = "//div[contains(@itemprop,'mainEntity')]//li[*]//a[1]//span[1]"
        try:

            wait = WebDriverWait(self.driver, 2)
            op = wait.until(EC.visibility_of_element_located((By.XPATH, first_dd_oppen)))
            op.click()
            elemt = self.driver.find_elements(By.XPATH, first_field_variants)
            # Print the number of options
            op = wait.until(EC.visibility_of_element_located((By.XPATH, first_dd_oppen)))
            op.click()
            print("Number of options:", len(elemt))
            return(len(elemt))
        except TimeoutException:
            print("Number of options:", 0)
            return(0)

    def check_if_variant_kit(self):
        variant_selector_main = "//body/div/div/div/div/div/div/div[contains(@itemprop,'mainEntity')]/form[contains(@method,'post')]/div/div/div/div/div[contains(@itemprop,'offers')]/div/div/dl/dd[*]/div/button/span[1]"
        try:
            wait = WebDriverWait(self.driver, 2)
            wait.until(EC.visibility_of_element_located((By.XPATH, variant_selector_main)))
            elemt = self.driver.find_elements(By.XPATH, variant_selector_main)
            print("Number of variable fields " + str(len(elemt)))
            return (len(elemt))
        except TimeoutException:
            print("Number of variable fields ",0)
            return (0)

    def take_variable_kit_product_price(self):
        selector_sale_price = "//div[@class='price font-weight-bold text-nowrap special-price']"
        selector_base_price = "//div[@class='col-xs-7']//div[@class='price font-weight-bold text-nowrap']//span"
        selector_base_price_while_on_sale = "//del[@class='value']"
        all_dd_lists= "//body/div/div/div/div/div/div/div[contains(@itemprop,'mainEntity')]/form[contains(@method,'post')]/div/div/div/div/div[contains(@itemprop,'offers')]/div/div/dl/dd[*]/div/button/span[1]"
        first_dd_oppen= "//body/div[@id='main-wrapper']/div[@id='content-wrapper']/div[@class='container']/div[@class='container-block beveled']/div[@class='row']/div[@id='content']/div[@id='result-wrapper']/form[@id='buy_form']/div[@class='vapo_detail_form_inner']/div[@id='product-offer']/div[@class='product-info col-xs-12 col-sm-7 col-md-5']/div[@class='product-info-inner']/div[@class='product-offer']/div[@class='variations switch-variations top15 row']/div[@class='col-xs-12']/dl/dd[1]/div[1]/button[1]"
        secound_dd_oppen= "//body/div[@id='main-wrapper']/div[@id='content-wrapper']/div[@class='container']/div[@class='container-block beveled']/div[@class='row']/div[@id='content']/div[@id='result-wrapper']/form[@id='buy_form']/div[@class='vapo_detail_form_inner']/div[@id='product-offer']/div[@class='product-info col-xs-12 col-sm-7 col-md-5']/div[@class='product-info-inner']/div[@class='product-offer']/div[@class='variations switch-variations top15 row']/div[@class='col-xs-12']/dl/dd[2]/div[1]/button[1]"
        first_field_variants= "//div[contains(@class,'btn-group bootstrap-select show-tick form-control open')]//li[*]//a[1]//span[1]"
        secound_field_variants= "//div[@class='btn-group bootstrap-select show-tick form-control open']//li[*]//a[1]//span[1]"
        selector_nazwy = "//h1[@class='fn product-title']"
        wait = WebDriverWait(self.driver, 3)

        wait.until(EC.visibility_of_element_located((By.XPATH, all_dd_lists)))
        variant_prices_and_name = []
        oppen_kit_field = self.driver.find_element(By.XPATH, first_dd_oppen)
        viewport_width = self.driver.execute_script("return window.innerWidth;")
        viewport_height = self.driver.execute_script("return window.innerHeight;")
        element_x = oppen_kit_field.location["x"]
        element_y = oppen_kit_field.location["y"]
        element_width = oppen_kit_field.size["width"]
        element_height = oppen_kit_field.size["height"]
        scroll_x = element_x - (viewport_width / 2) + (element_width / 2)
        scroll_y = element_y - (viewport_height / 2) + (element_height / 2)
        self.driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", scroll_x, scroll_y)
        oppen_kit_field.click()
        time.sleep(1)
        kit_field_variants = self.driver.find_elements(By.XPATH, first_field_variants)
        flag = True
        try:
            for  k , swithes in enumerate(kit_field_variants, start=1):
                wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'btn-group bootstrap-select show-tick form-control open')]//li["+str(k)+"]//a[1]")))
                new_kit_field_elements = self.driver.find_element(By.XPATH,"//div[contains(@class,'btn-group bootstrap-select show-tick form-control open')]//li["+str(k)+"]//a[1]")
                new_kit_field_elements.click()
                wait.until(EC.visibility_of_element_located((By.XPATH, secound_dd_oppen)))
                oppen_variant_field = self.driver.find_element(By.XPATH, secound_dd_oppen)
                oppen_variant_field.click()
                if flag == True:
                    # time.sleep(3)
                    wait = WebDriverWait(self.driver, 5)
                    wait.until(EC.visibility_of_element_located((By.XPATH, secound_field_variants)))
                    variant_field_elements = self.driver.find_elements(By.XPATH, secound_field_variants)
                    flag = False
                for i, variant_element in enumerate(variant_field_elements, start=1):
                    wait = WebDriverWait(self.driver, 2)
                    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='btn-group bootstrap-select show-tick form-control open']//li["+str(i)+"]")))
                    new_variant_field_elements = self.driver.find_element(By.XPATH, "//div[@class='btn-group bootstrap-select show-tick form-control open']//li["+str(i)+"]")
                    new_variant_field_elements.click()
                    try:
                        time.sleep(1)
                        pn = wait.until(EC.visibility_of_element_located((By.XPATH, selector_nazwy)))
                        product_name = pn.text
                        wait.until(EC.visibility_of_element_located((By.XPATH, selector_base_price)))
                        element1 = self.driver.find_element(By.XPATH, selector_base_price)
                        variant_prices_and_name.append([element1.text, str(product_name)])
                        print(variant_prices_and_name)
                    except TimeoutException:
                        wait = WebDriverWait(self.driver, 2)
                        time.sleep(1)
                        pn = wait.until(EC.visibility_of_element_located((By.XPATH, selector_nazwy)))
                        product_name = pn.text
                        wait = WebDriverWait(self.driver, 2)
                        wait.until(EC.visibility_of_element_located((By.XPATH, selector_sale_price)))
                        element1 = self.driver.find_element(By.XPATH, selector_sale_price)
                        wait = WebDriverWait(self.driver, 2)
                        wait.until(EC.visibility_of_element_located((By.XPATH, selector_base_price_while_on_sale)))
                        element2 = self.driver.find_element(By.XPATH, selector_base_price_while_on_sale)
                        variant_prices_and_name.append(
                                    [element1.text, str(product_name),element2.text])
                        print(variant_prices_and_name)
                    wait.until(EC.visibility_of_element_located((By.XPATH, secound_dd_oppen)))
                    oppen_variant_field = self.driver.find_element(By.XPATH, secound_dd_oppen)
                    oppen_variant_field.click()
                wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='btn-group bootstrap-select show-tick form-control open']//li["+str(i)+"]")))
                new_variant_field_elements = self.driver.find_element(By.XPATH, "//div[@class='btn-group bootstrap-select show-tick form-control open']//li["+str(i)+"]")
                new_variant_field_elements.click()
                wait.until(EC.visibility_of_element_located((By.XPATH, first_dd_oppen)))
                oppen_kit_field = self.driver.find_element(By.XPATH, first_dd_oppen)
                oppen_kit_field.click()
                time.sleep(1)
        except:
            wait = WebDriverWait(self.driver, 2)
            pn = wait.until(EC.visibility_of_element_located((By.XPATH, selector_nazwy)))
            product_name = pn.text
            variant_prices_and_name.append(["Nie mogłem pobrać", str(product_name)])
            print(variant_prices_and_name)
            pass
        return (variant_prices_and_name)

    def take_variable_product_price(self):
        selector_sale_price = "//div[@class='price font-weight-bold text-nowrap special-price']"
        selector_base_price = "//div[@class='col-xs-7']//div[@class='price font-weight-bold text-nowrap']//span"
        selector_base_price_while_on_sale = "//del[@class='value']"
        selector_recommended_retail_rice_base = "//div[@class='col-xs-7']//div[@class='price font-weight-bold text-nowrap']"
        first_dd_oppen = "//span[@class='filter-option pull-left']"
        first_field_variants = "//div[contains(@itemprop,'mainEntity')]//li[*]//a[1]//span[1]"
        selector_nazwy = "//h1[@class='fn product-title']"
        wait = WebDriverWait(self.driver, 5)
        oppen_kit_field = self.driver.find_element(By.XPATH, first_dd_oppen)
        oppen_kit_field.click()
        time.sleep(1)
        kit_field_variants = self.driver.find_elements(By.XPATH, first_field_variants)
        variant_prices_and_name = []
        try:
            for k, swithes in enumerate(kit_field_variants, start=1):

                    try:
                        try:
                            wait = WebDriverWait(self.driver, 2)
                            wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@itemprop,'mainEntity')]//li[" + str(k) + "]//a[1]//span[1]")))
                            new_kit_field_elements = self.driver.find_element(By.XPATH, "//div[contains(@itemprop,'mainEntity')]//li[" + str(k) + "]//a[1]//span[1]")
                            new_kit_field_elements.click()
                            time.sleep(1)
                            pn = wait.until(EC.visibility_of_element_located((By.XPATH, selector_nazwy)))
                            product_name = pn.text
                            wait = WebDriverWait(self.driver, 1)
                            wait.until(EC.visibility_of_element_located((By.XPATH, selector_base_price)))
                            element1 = self.driver.find_element(By.XPATH, selector_base_price)
                            variant_prices_and_name.append([element1.text, str(product_name)])
                            print(variant_prices_and_name)
                        except TimeoutException:
                            wait = WebDriverWait(self.driver, 2)
                            wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@itemprop,'mainEntity')]//li[" + str(k) + "]//a[1]//span[1]")))
                            new_kit_field_elements = self.driver.find_element(By.XPATH,"//div[contains(@itemprop,'mainEntity')]//li[" + str(k) + "]//a[1]//span[1]")
                            new_kit_field_elements.click()
                            time.sleep(1)
                            pn = wait.until(EC.visibility_of_element_located((By.XPATH, selector_nazwy)))
                            product_name = pn.text
                            wait = WebDriverWait(self.driver, 1)
                            wait.until(EC.visibility_of_element_located((By.XPATH, selector_sale_price)))
                            element1 = self.driver.find_element(By.XPATH, selector_sale_price)
                            wait.until(EC.visibility_of_element_located((By.XPATH, selector_base_price_while_on_sale)))
                            element2 = self.driver.find_element(By.XPATH, selector_base_price_while_on_sale)
                            variant_prices_and_name.append([element1.text, str(product_name), element2.text])
                            print(variant_prices_and_name)
                        oppen_kit_field = self.driver.find_element(By.XPATH, first_dd_oppen)
                        oppen_kit_field.click()
                    except TimeoutException:
                        try:
                            pn = wait.until(EC.visibility_of_element_located((By.XPATH, selector_nazwy)))
                            product_name = pn.text
                            wait = WebDriverWait(self.driver, 1)
                            wait.until(EC.visibility_of_element_located((By.XPATH, selector_recommended_retail_rice_base)))
                            element1 = self.driver.find_element(By.XPATH, selector_recommended_retail_rice_base)
                            variant_prices_and_name.append([element1.text, str(product_name)])
                            print(variant_prices_and_name)

                        except TimeoutException:
                            wait = WebDriverWait(self.driver, 2)
                            wait.until(EC.visibility_of_element_located((By.XPATH, selector_sale_price)))
                            element1 = self.driver.find_element(By.XPATH, selector_sale_price)
                            wait.until(EC.visibility_of_element_located((By.XPATH, selector_base_price_while_on_sale)))
                            element2 = self.driver.find_element(By.XPATH, selector_base_price_while_on_sale)
                            variant_prices_and_name.append([element1.text, str(product_name), element2.text])
                            print(variant_prices_and_name)
                        oppen_kit_field = self.driver.find_element(By.XPATH, first_dd_oppen)
                        oppen_kit_field.click()
        except TimeoutException:
            pn = wait.until(EC.visibility_of_element_located((By.XPATH, selector_nazwy)))
            product_name = pn.text
            variant_prices_and_name.append(["Nie mogłem pobrać", str(product_name)])
            print(variant_prices_and_name)
            pass
        return (variant_prices_and_name)

    def take_simple_product_price(self):
        selector_sale_price = "//div[@class='price font-weight-bold text-nowrap special-price']"
        selector_base_price = "//div[@class='col-xs-7']//div[@class='price font-weight-bold text-nowrap']"
        selector_base_price_while_on_sale = "//del[@class='value']"
        selector_nazwy = "//h1[@class='fn product-title']"
        try:
            try:
                wait = WebDriverWait(self.driver, 5)
                wait.until(EC.visibility_of_element_located((By.XPATH, selector_base_price)))
                element = self.driver.find_element(By.XPATH, selector_base_price)
                print(element.text)
                return (element.text)
            except TimeoutException:
                wait = WebDriverWait(self.driver,1)
                wait.until(EC.visibility_of_element_located((By.XPATH,selector_sale_price)))
                element1 =self.driver.find_element(By.XPATH,selector_sale_price)
                element2 =self.driver.find_element(By.XPATH,selector_base_price_while_on_sale)
                print(element1.text,element2.text)
                return([element1.text, element2.text])
        except:
            pn = wait.until(EC.visibility_of_element_located((By.XPATH, selector_nazwy)))
            product_name = pn.text
            print(["Nie mogłem pobrać", str(product_name)])
            return(["Nie mogłem pobrać", str(product_name)])
            pass

    def find_element_title(self):
        selector_nazwy = "//h1[@class='fn product-title']"
        element = self.driver.find_element(By.XPATH, selector_nazwy)
        return (element.text)
    def veryf_handler(self):
        try:
            wait = WebDriverWait(self.driver, 2)
            yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='fskYes']")))
            yes_button.click()
            yes_button2 = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='cbtn cbtn-secondary bugmenot']")))
            yes_button2.click()
            yes_button3 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ws_oss_close']")))
            yes_button3.click()
        except:
            pass

    def quit_driver(self):
        print("quit")
        self.driver.quit()

