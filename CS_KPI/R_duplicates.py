import gspread

from oauth2client.service_account import ServiceAccountCredentials

class RemoveDuplicates:

    def remove_dup_tidio(self):
        scope = ['https://www.googleapis.com/auth/spreadsheets',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
        client = gspread.authorize(creds)
        workbook = client.open("client")
        sheet2 = workbook.worksheet("worksheet")
        values = sheet2.get_all_values()
        # Tworzenie listy unikalnych wartości z zachowaniem kolejności
        unique_values = []
        seen_values = set()
        for row in values:
            key = (row[0],row[1],row[2],row[3],row[4],row[5])
            if key not in seen_values:
                unique_values.append(row)
                seen_values.add(key)
        # Wyczyszczenie istniejących danych na arkuszu
        sheet2.clear()
        # Zapis unikalnych wartości z zachowaniem kolejności
        sheet2.append_rows(unique_values, value_input_option="USER_ENTERED")

    def remove_dup_fresh(self):
        scope = ['https://www.googleapis.com/auth/spreadsheets',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
        client = gspread.authorize(creds)
        workbook = client.open("client")
        sheet2 = workbook.worksheet("workbook")
        values = sheet2.get_all_values()
        # Tworzenie listy unikalnych wartości z zachowaniem kolejności
        unique_values = []
        seen_values = set()
        for row in values:
            key = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[9],row[10],row[11])
            if key not in seen_values:
                unique_values.append(row)
                seen_values.add(key)
        # Wyczyszczenie istniejących danych na arkuszu
        sheet2.clear()
        # Zapis unikalnych wartości z zachowaniem kolejności
        sheet2.append_rows(unique_values, value_input_option="USER_ENTERED")

    def remove_dup_zdarma(self):
        scope = ['https://www.googleapis.com/auth/spreadsheets',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
        client = gspread.authorize(creds)
        workbook = client.open("client")
        sheet2 = workbook.worksheet("worksheet")
        values = sheet2.get_all_values()
        # Tworzenie listy unikalnych wartości z zachowaniem kolejności
        unique_values = []
        seen_values = set()
        for row in values:
            key = (row[0],row[1], row[2], row[3], row[4], row[5])
            if key not in seen_values:
                unique_values.append(row)
                seen_values.add(key)
        # Wyczyszczenie istniejących danych na arkuszu
        sheet2.clear()
        # Zapis unikalnych wartości z zachowaniem kolejności
        sheet2.append_rows(unique_values, value_input_option="USER_ENTERED")
