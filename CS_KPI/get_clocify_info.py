import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
client = gspread.authorize(creds)

workbook = client.open("bl_zamowienia_all")
sheet = workbook.worksheet("Clockify")
sheetvalues = sheet.col_values(1)
column_length_sheet2 = len(sheetvalues)

def run_clockify_get_data():
    api_key="xyz"
    data = {'x-api-key': api_key}
    # workspaceId = "64ec9d6159d1113e2d4f4d7c"
    # userid = "64ec9d6159d1113e2d4f4d7b"
    users = requests.get("https://api.clockify.me/api/v1/workspaces/xyz/users", headers=data)
    users = users.json()
    user_list = []
    i = 1
    final_list = []
    update_cells_list=[]

    for user in users:
        id = user.get("id")
        name = user.get('name')
        user_list.append([id,name])
        print(user_list)

    for agent in user_list:
        print(agent[0])
        time_entries = requests.get('https://api.clockify.me/api/v1/workspaces/xyz/user/'+agent[0]+'/time-entries', headers=data)
        time_entries = time_entries.json()
        for project in time_entries:
            user_name = agent[1]
            projectId = project.get("projectId")
            description = project.get("description")
            if description == "":
                description="brak"
            start = project.get("timeInterval").get("start")
            end = project.get("timeInterval").get("end")
            duration = project.get("timeInterval").get("duration")
            final_list.append([projectId,description,start,end,duration,user_name])
            print(projectId,description,start,end,duration,user_name)

    for data in final_list:
        i = i + 1
        output_row = i
        cell_b = gspread.Cell(output_row, 1)
        cell_c = gspread.Cell(output_row, 2)
        cell_d = gspread.Cell(output_row, 3)
        cell_e = gspread.Cell(output_row, 4)
        cell_f = gspread.Cell(output_row, 5)
        cell_g = gspread.Cell(output_row, 6)

        cell_b.value = data[0]
        cell_c.value = data[1]
        cell_d.value = data[2]
        cell_e.value = data[3]
        cell_f.value = data[4]
        cell_g.value = data[5]

        update_cells_list.append(cell_b)
        update_cells_list.append(cell_c)
        update_cells_list.append(cell_d)
        update_cells_list.append(cell_e)
        update_cells_list.append(cell_f)
        update_cells_list.append(cell_g)
    sheet.update_cells(update_cells_list, value_input_option="USER_ENTERED")
if __name__ == '__main__':
    run_clockify_get_data()

