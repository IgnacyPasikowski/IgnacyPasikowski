import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Browser_Actions.Browser_Actions_Mv import BrowserActionsMv
from Remove_Duplicates import RemoveDuplicates
from selenium.common.exceptions import NoSuchElementException
from Update_URLs.UpdateURLsEUR import UpdateUrlsEUR

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('keysEUR.json', scope)
client = gspread.authorize(creds)

workbook = client.open("client_EUR")
sheet = workbook.worksheet("MvDE URLS")
sheet2 = workbook.worksheet("MvDE prices")
subsheet_name = "MvDE prices"
dictrionary = "MvDict"
UpdateURLsEUR = UpdateUrlsEUR()
row_index = 1
column_number = 1
values = sheet.col_values(column_number)
column_length_sheet1 = len(values)

column_a_values = sheet.col_values(1)[1:]

update_cells_list = []
i = 0

sheet2values = sheet2.col_values(1)
column_length_sheet2 = len(sheet2values)
Browser = BrowserActionsMv()
first_iteration = True

UpdateURLsEUR.update_vsDE_urls()
for value in column_a_values:
    try:
        value = str(value)
        print(value)
        Browser.driver_get(value)
        Remove = RemoveDuplicates()
        ilosc_wariantow_kit = Browser.check_if_variant_kit()

        if ilosc_wariantow_kit >=1:
            # for kit in range(ilosc_wariantow_kit):
            ilosc_wariantow = Browser.check_if_variant()
            if ilosc_wariantow >= 1:
                variants = Browser.take_variable_kit_product_price()
                product_name = Browser.find_element_title()
                for variant in variants:
                    i = i + 1
                    output_row = column_length_sheet2 + i
                    cell_b = gspread.Cell(output_row, 2)
                    cell_c = gspread.Cell(output_row, 3)
                    cell_d = gspread.Cell(output_row, 4)
                    if len(variant) == 3:
                        cell_b.value = str(product_name) + " " + str(variant[1])
                        cell_c.value = variant[2]
                        cell_d.value = variant[0]
                    else:
                        cell_b.value = Browser.find_element_title() + " " + variant[1]
                        cell_c.value = variant[0]
                        cell_d.value = ""
                    update_cells_list.append(cell_b)
                    update_cells_list.append(cell_c)
                    update_cells_list.append(cell_d)
            elif ilosc_wariantow <= 1:
                variants = Browser.take_only_kit_product_price()
                product_name = Browser.find_element_title()
                cell_b = gspread.Cell(output_row, 2)
                cell_c = gspread.Cell(output_row, 3)
                cell_d = gspread.Cell(output_row, 4)
                for variant in variants:

                    cell_b.value = Browser.find_element_title() + " " + variant[1]
                    cell_c.value = variant[0]
                    cell_d.value = ""
                update_cells_list.append(cell_b)
                update_cells_list.append(cell_c)
                update_cells_list.append(cell_d)


            else:
                i = i + 1
                output_row = column_length_sheet2 + i
                product_name = Browser.find_element_title()
                product = Browser.take_simple_product_price()
                cell_b = gspread.Cell(output_row, 2)
                cell_c = gspread.Cell(output_row, 3)
                cell_d = gspread.Cell(output_row, 4)
                if len(product) == 2:
                    cell_b.value = product_name
                    cell_c.value = product[1]
                    cell_d.value = product[0]
                else:
                    cell_b.value = product_name
                    cell_c.value = product
                    cell_d.value = ""
                update_cells_list.append(cell_b)
                update_cells_list.append(cell_c)
                update_cells_list.append(cell_d)

        elif ilosc_wariantow_kit <=1:
            ilosc_wariantow = Browser.check_if_variant()
            if ilosc_wariantow >= 1:

                variants = Browser.take_variable_product_price()
                product_name = Browser.find_element_title()
                for variant in variants:
                    i = i + 1
                    output_row = column_length_sheet2 + i
                    cell_b = gspread.Cell(output_row, 2)
                    cell_c = gspread.Cell(output_row, 3)
                    cell_d = gspread.Cell(output_row, 4)
                    if len(variant) == 3:
                        cell_b.value = str(product_name) + " " + str(variant[1])
                        cell_c.value = variant[2]
                        cell_d.value = variant[0]
                    else:
                        cell_b.value = Browser.find_element_title() + " " + variant[1]
                        cell_c.value = variant[0]
                        cell_d.value = ""
                    update_cells_list.append(cell_b)
                    update_cells_list.append(cell_c)
                    update_cells_list.append(cell_d)
            else:
                i = i + 1
                output_row = column_length_sheet2 + i
                product_name = Browser.find_element_title()
                product = Browser.take_simple_product_price()
                cell_b = gspread.Cell(output_row, 2)
                cell_c = gspread.Cell(output_row, 3)
                cell_d = gspread.Cell(output_row, 4)
                if len(product) == 2:
                    cell_b.value = product_name
                    cell_c.value = product[1]
                    cell_d.value = product[0]
                else:
                    cell_b.value = product_name
                    cell_c.value = product
                    cell_d.value = ""
                update_cells_list.append(cell_b)
                update_cells_list.append(cell_c)
                update_cells_list.append(cell_d)
    except NoSuchElementException:
        print("Błąd URL")
        continue



sheet2.update_cells(update_cells_list)
Browser.quit_driver()
Remove.remove_dup_eur(subsheet_name, dictrionary)


