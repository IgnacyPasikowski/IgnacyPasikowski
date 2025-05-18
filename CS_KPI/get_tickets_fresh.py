## This script requires "requests": http://docs.python-requests.org/
## To install: pip install requests
from datetime import date
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from R_duplicates import RemoveDuplicates
import time

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Fresh/keys.json', scope)
client = gspread.authorize(creds)

workbook = client.open("bl_zamowienia_all")
sheet = workbook.worksheet("Fresh")
sheetvalues = sheet.col_values(1)
column_length_sheet2 = len(sheetvalues)

api_key = "xyz"
domain = "xyz"
password = "xyz"
today = date.today()
Remove = RemoveDuplicates()

def run_fresh_tickets_get():
    r = requests.get("https://" + domain + ".freshdesk.com/api/v2/tickets?updated_since=" + str(
        today) + "&per_page=100&page=1&include=stats", auth=(api_key, password)).json()
    tickes_list = []
    update_cells_list = []
    i = 1
    line= column_length_sheet2
    print(len(r))
    while len(r) >= 1:
        i = i + 1
        print(len(r))
        for ticket in r:
            print(ticket)

            id = ticket.get('id')
            responder_id = ticket.get("responder_id")
            created_at = ticket.get("created_at")
            agent_responded_at = ticket.get("stats").get("agent_responded_at")
            first_responded_at = ticket.get("stats").get("first_responded_at")
            resolved_at = ticket.get("stats").get("resolved_at")
            closed_at = ticket.get("stats").get("closed_at")
            status = ticket.get("status")
            source = ticket.get("source")
            priority = ticket.get("priority")

            subject = ticket.get("subject")
            tickes_list.append([id,responder_id,created_at,agent_responded_at,first_responded_at,resolved_at,closed_at,subject,status,source,priority])

        r =requests.get("https://" + domain + ".freshdesk.com/api/v2/tickets?updated_since=" + str(today) + "&per_page=100&page="+str(i)+"&include=stats", auth=(api_key, password)).json()
        print(i)
    for ticket_details in tickes_list:
        line = line + 1
        output_row = line

        cell_b = gspread.Cell(output_row, 1)
        cell_c = gspread.Cell(output_row, 2)
        cell_d = gspread.Cell(output_row, 3)
        cell_e = gspread.Cell(output_row, 4)
        cell_f = gspread.Cell(output_row, 5)
        cell_g = gspread.Cell(output_row, 6)
        cell_h = gspread.Cell(output_row, 7)
        cell_i = gspread.Cell(output_row, 8)
        cell_j = gspread.Cell(output_row, 9)
        cell_k = gspread.Cell(output_row, 10)
        cell_l = gspread.Cell(output_row, 11)
        cell_m = gspread.Cell(output_row, 12)

        cell_b.value = ticket_details[0]
        cell_c.value = ticket_details[1]
        cell_d.value = f"=JEŻELI(B{output_row}=\"\";\"\";X.WYSZUKAJ(B{output_row};'Fresh słownik'!K2:K;'Fresh słownik'!J2:J;\"Brak Agenta\"))"
        cell_e.value = ticket_details[2]
        cell_f.value = ticket_details[3]
        cell_g.value = ticket_details[4]
        cell_h.value = ticket_details[5]
        cell_i.value = ticket_details[6]
        cell_j.value = ticket_details[7]
        cell_k.value = f"=X.WYSZUKAJ({ticket_details[8]};'Fresh słownik'!E2:E;'Fresh słownik'!D2:D)"
        cell_l.value = f"=X.WYSZUKAJ({ticket_details[9]};'Fresh słownik'!B2:B;'Fresh słownik'!A2:A)"
        cell_m.value = f"=X.WYSZUKAJ({ticket_details[10]};'Fresh słownik'!H2:H;'Fresh słownik'!G2:G)"


        update_cells_list.append(cell_b)
        update_cells_list.append(cell_c)
        update_cells_list.append(cell_d)
        update_cells_list.append(cell_e)
        update_cells_list.append(cell_f)
        update_cells_list.append(cell_g)
        update_cells_list.append(cell_h)
        update_cells_list.append(cell_i)
        update_cells_list.append(cell_j)
        update_cells_list.append(cell_k)
        update_cells_list.append(cell_l)
        update_cells_list.append(cell_m)

    sheet.update_cells(update_cells_list, value_input_option="USER_ENTERED")
    Remove.remove_dup_fresh()
if __name__ == '__main__':
    run_fresh_tickets_get()