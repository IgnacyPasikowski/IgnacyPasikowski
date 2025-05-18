import requests
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
from R_duplicates import RemoveDuplicates

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
client = gspread.authorize(creds)
# client_id: ci_b62a09776e654590bb2630ba7df0d2b1
# client:secret: cs_2da493e4531e4232ba372959e4776395

workbook = client.open("client")
sheet = workbook.worksheet("workbook")
column_number = 1
values = sheet.col_values(column_number)
column_length_sheet1 = len(values)

Contacts = "https://api.tidio.com/contacts"
headers = {
    "accept": "application/json; version=1",
    "X-Tidio-Openapi-Client-Id": "xyz",
    "X-Tidio-Openapi-Client-Secret": "xyz"
}
contact_list= []
message_list =[]
update_cells_list= []
i =column_length_sheet1

contacts = requests.get(Contacts, headers=headers)
data_dict = json.loads(contacts.text)
Remove = RemoveDuplicates()
for contact in data_dict["contacts"]:
    id = contact.get("id")
    email = contact.get("email")
    date = contact.get("created_at")
    contact_list.append([date,id,email])

for c in contact_list:
    time.sleep(7)
    headers = {
        "accept": "application/json; version=1",
        "X-Tidio-Openapi-Client-Id": "ci_4ffb14392d94499d82caadc4b8d106ce",
        "X-Tidio-Openapi-Client-Secret": "cs_1f40a59ab8244acea2c992b616b0bbbb"
    }
    contact_id = c[1]

    Messages = "https://api.tidio.com/contacts/"+str(contact_id)+"/messages"
    messages =requests.get(Messages, headers=headers)
    messages_j =data_dict_messages = json.loads(messages.text)
    messages_j =messages_j["messages"]
    for message_a in messages_j:
        id = message_a.get('id')
        author_id = message_a.get("author_id")
        created_at = message_a.get("created_at")
        message = message_a.get("message")
        message_list.append([contact_id,id,created_at,message,author_id])
    print(message_list)
for message_b in message_list:

    i = i + 1
    output_row = i
    cell_a = gspread.Cell(output_row, 1)
    cell_b = gspread.Cell(output_row, 2)
    cell_c = gspread.Cell(output_row, 3)
    cell_d = gspread.Cell(output_row, 4)
    cell_e = gspread.Cell(output_row, 5)
    cell_f = gspread.Cell(output_row, 6)


    cell_a.value = message_b[0]
    cell_b.value = message_b[1]
    cell_c.value = message_b[2]
    cell_d.value = message_b[3]
    cell_e.value = message_b[4]
    cell_f.value = f"=JEŻELI(E{i}=\"\";\"Bot\"; X.WYSZUKAJ(E{i};'Tidio słownik'!A$1:A;'Tidio słownik'!B$1:B;\"Klient\"))"


    update_cells_list.append(cell_a)
    update_cells_list.append(cell_b)
    update_cells_list.append(cell_c)
    update_cells_list.append(cell_d)
    update_cells_list.append(cell_e)
    update_cells_list.append(cell_f)

sheet.update_cells(update_cells_list, value_input_option="USER_ENTERED")
Remove.remove_dup_tidio()
