from baselinker import Baselinker
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
client = gspread.authorize(creds)

API_TOKEN = 'xyz'

workbook = client.open("client")
sheet = workbook.worksheet("workbook")
sheetvalues = sheet.col_values(1)
column_length_sheet2 = len(sheetvalues)

def run():
    # Create a baselinker client instance
    baselinker = Baselinker(API_TOKEN)
    # Prints 100 orders from baselinker
    # orders = baselinker.orders.get_orders()
    orders = baselinker.orders.get_orders().get('orders')
    order_list_all = []
    update_cells_list = []
    i = 1
    while len(orders)>=1:

        for order in orders:
            order_id =order.get('order_id')
            order_page =order.get('order_page')
            phone_numb = order.get('phone')
            data_comfirmed = order.get('date_confirmed')
            status_id = order.get('order_status_id')
            order_list_all.append([order_id,order_page,phone_numb,status_id,data_comfirmed])
        print("ostatni " + str(order_list_all[-1][4]))
        last_order = order_list_all[-1][4]
        orders = baselinker.orders.get_orders(date_confirmed_from=last_order + 1).get('orders')
    print(order_list_all)

    for data_from_order in order_list_all:
        i = i + 1
        output_row = i
        cell_b = gspread.Cell(output_row, 1)
        cell_c = gspread.Cell(output_row, 2)
        cell_d = gspread.Cell(output_row, 3)
        cell_e = gspread.Cell(output_row, 4)
        cell_g = gspread.Cell(output_row, 5)

        cell_b.value = data_from_order[0]
        cell_c.value = data_from_order[1]
        cell_d.value = data_from_order[2]
        cell_e.value = data_from_order[3]
        cell_g.value = f"=X.WYSZUKAJ(D{i};Statusy!A$1:A;Statusy!B$1:B;\"Brak statusu\")"

        update_cells_list.append(cell_b)
        update_cells_list.append(cell_c)
        update_cells_list.append(cell_d)
        update_cells_list.append(cell_e)
        update_cells_list.append(cell_g)
    sheet.update_cells(update_cells_list, value_input_option="USER_ENTERED")

if __name__ == '__main__':
    run()
