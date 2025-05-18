import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Browser_Actions.Browser_Actions_Kon import BrowserActionsKon
from Remove_Duplicates import RemoveDuplicates
from selenium.common.exceptions import NoSuchElementException
from Update_URLs.UpdateURLsPLN import UpdateUrlsPLN
scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('keysPLN.json', scope)
client = gspread.authorize(creds)

workbook = client.open("client")
sheet = workbook.worksheet("KonPL URLS")
sheet2 = workbook.worksheet("KonPL prices")
subsheet_name = "KonPL prices"
dictrionary = "KonDict"
row_index = 1
column_number = 1
values = sheet.col_values(column_number)
column_length_sheet1 = len(values)
UpdateURLsPLN = UpdateUrlsPLN()

column_a_values = sheet.col_values(1)[1:]

update_cells_list = []
i = 0
UpdateURLsPLN.update_kon_pl_urls()
sheet2values = sheet2.col_values(1)
column_length_sheet2 = len(sheet2values)
Browser = BrowserActionsKon()
first_iteration = True

for value in column_a_values:
    try:
        value = str(value)
        print(value)
        Browser.driver_get(value)
        Remove = RemoveDuplicates()
        # Browser.choose_eur_currency()

        i = i +1
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
        pass

sheet2.update_cells(update_cells_list)
Browser.quit_driver()
Remove.remove_dup_kon_pln(subsheet_name, dictrionary)


