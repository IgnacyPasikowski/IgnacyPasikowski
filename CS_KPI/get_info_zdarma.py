from zadarma import api
from datetime import date
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
from R_duplicates import RemoveDuplicates

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
client = gspread.authorize(creds)

API_TOKEN = 'xyz'

workbook = client.open("client")
sheet = workbook.worksheet("worksheet")
sheetvalues = sheet.col_values(1)
Remove =RemoveDuplicates()

def run_zdarma_data():
    column_length_sheet2 = len(sheetvalues)
    update_cells_list = []
    call_list = []
    i = column_length_sheet2
    today = date.today()
    z_api = api.ZadarmaAPI(key='xyz', secret='xyz')
    # get tariff information
    stats = z_api.call('/v1/statistics/pbx/', {"status":"success", "start":str(today)+" 00:00:00", "end":str(today)+" 18:00:00","version":2})
    data_dict = json.loads(stats)
    stats = data_dict['stats']
    for stat in stats:
        call_id = stat.get('call_id')
        sip = stat.get('sip')
        callstart = stat.get("callstart")
        clid =stat.get("clid")
        duration =stat.get('seconds')
        call_list.append([call_id,callstart,duration,clid,sip])
    print(call_list)
    for call in call_list:
        i = i + 1
        output_row = i
        cell_b = gspread.Cell(output_row, 1)
        cell_c = gspread.Cell(output_row, 2)
        cell_d = gspread.Cell(output_row, 3)
        cell_e = gspread.Cell(output_row, 4)
        cell_f = gspread.Cell(output_row, 5)
        cell_g = gspread.Cell(output_row, 6)

        cell_b.value = call[0]
        cell_c.value = call[1]
        cell_d.value = call[2]
        cell_e.value = call[3]
        cell_f.value = call[4]
        cell_g.value = f"=X.WYSZUKAJ(E{i};'Sip słownik'!A$2:A;'Sip słownik'!B$2:B)"

        update_cells_list.append(cell_b)
        update_cells_list.append(cell_c)
        update_cells_list.append(cell_d)
        update_cells_list.append(cell_e)
        update_cells_list.append(cell_f)
        update_cells_list.append(cell_g)
    sheet.update_cells(update_cells_list, value_input_option="USER_ENTERED")
    Remove.remove_dup_zdarma()

if __name__ == '__main__':
    run_zdarma_data()
