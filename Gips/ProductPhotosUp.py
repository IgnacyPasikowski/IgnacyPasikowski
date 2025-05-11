import gspread
from oauth2client.service_account import ServiceAccountCredentials
from NordActions import NordActions


scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
client = gspread.authorize(creds)

workbook = client.open("GipsProdukty")
sheet = workbook.worksheet("ElewPhotoURLs")

URL = "https://URL.URL/"
NordActions = NordActions()
NordActions.driver_get(URL)
all_prod = []
category = NordActions.crawl_through_cat()
print(category)
prod_data = []
a = 1
update_cells_list = []
for cat in category:
    if "Do montażu" in cat[1]:
        print("tego nie chcemy")
    else:
        NordActions.driver_get(cat[0])
        all_prod.append(NordActions.crawl_through_prod())
for cat_list in all_prod:
    i = 0
    cat_name = cat_list[0]
    for prod in cat_list:
        if i == 0:
            pass
        else:
            print("cat"+str(cat_name))
            product = NordActions.take_product_photo(prod)
            product.extend([cat_name])
            prod_data.append(product)
            print(prod_data)
        i = i + 1

for prod in prod_data:
    a = a + 1
    output_row = a
    cell_b = gspread.Cell(output_row, 1)
    cell_c = gspread.Cell(output_row, 2)
    cell_d = gspread.Cell(output_row, 3)


    cell_b.value = prod[0]
    cell_c.value = prod[1]
    cell_d.value = prod[2]

    update_cells_list.append(cell_b)
    update_cells_list.append(cell_c)
    update_cells_list.append(cell_d)


sheet.update_cells(update_cells_list, value_input_option="USER_ENTERED")
