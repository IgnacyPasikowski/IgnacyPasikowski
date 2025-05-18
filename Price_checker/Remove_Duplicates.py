import gspread

from oauth2client.service_account import ServiceAccountCredentials

class RemoveDuplicates:

    def remove_dup_eur(self,subsheet_name,dictrionary):
        scope = ['https://www.googleapis.com/auth/spreadsheets',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('keysEUR.json', scope)
        client = gspread.authorize(creds)
        workbook = client.open("client_EUR")
        sheet2 = workbook.worksheet(subsheet_name)
        # Pobranie wszystkich wartości z arkusza
        values = sheet2.get_all_values()
        # Tworzenie listy unikalnych wartości z zachowaniem kolejności
        unique_values = []
        seen_values = set()
        for row in values:
            row[2] = row[2].replace('€', '')
            row[2] = row[2].replace('.', ',')
            row[3] = row[3].replace('€', '')
            row[3] = row[3].replace('.', ',')
            key = (row[1], row[2], row[3])
            if key not in seen_values:
                unique_values.append(row)
                seen_values.add(key)
        # Wyczyszczenie istniejących danych na arkuszu
        sheet2.clear()
        # Przywrócenie niezmienionych wartości z kolumny B i wstawienie funkcji FINDSIMILARTEXT()
        for i, row in enumerate(unique_values):
            # formula = f"=PROMPTLOOP_LABEL(A{i+1};'PM tłumaczenie'!E$2:E$208)"
            formula = f"=X.WYSZUKAJ(B{i+1};{dictrionary}!A$2:A;{dictrionary}!C$2:C;\"Brak Produktu\")"
            row[0] = formula
            # formula2 = f"=FINDSIMILARTEXT(A{i+1};'PM tłumaczenie'!E$2:E$208;0,6)"
            # row[2] = formula2
            # formula2 = f"=JEŻELI(NIE(CZY.PUSTA(C{i+1}));B{i+1};\"\")"
            # row[3] = formula2
        # Zapis unikalnych wartości z zachowaniem kolejności
        sheet2.append_rows(unique_values, value_input_option="USER_ENTERED")

    def remove_dup_pln(self,subsheet_name,dictrionary):
        scope = ['https://www.googleapis.com/auth/spreadsheets',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('keysPLN.json', scope)
        client = gspread.authorize(creds)
        workbook = client.open("client_PLN")
        sheet2 = workbook.worksheet(subsheet_name)
        # Pobranie wszystkich wartości z arkusza
        values = sheet2.get_all_values()
        # Tworzenie listy unikalnych wartości z zachowaniem kolejności
        unique_values = []
        seen_values = set()
        for row in values:
            row[2] = row[2].strip().replace('zł', '')
            row[2] = row[2].replace(' ', '')
            row[2] = row[2].replace('.', ',')
            row[2] = row[2].replace(',00', '')
            row[3] = row[3].strip().replace('zł', '')
            row[3] = row[3].replace(' ', '')
            row[3] = row[3].replace('.', ',')
            row[3] = row[3].replace(',00', '')
            key = (row[1], row[2], row[3])
            if key not in seen_values:
                unique_values.append(row)
                seen_values.add(key)
        # Wyczyszczenie istniejących danych na arkuszu
        sheet2.clear()
        # Przywrócenie niezmienionych wartości z kolumny B i wstawienie funkcji FINDSIMILARTEXT()
        for i, row in enumerate(unique_values):
            formula = f"=X.WYSZUKAJ(B{i+1};{dictrionary}!A$2:A;{dictrionary}!C$2:C;\"Brak Produktu w VapeFully\")"
            row[0] = formula
        # Zapis unikalnych wartości z zachowaniem kolejności
        sheet2.append_rows(unique_values, value_input_option="USER_ENTERED")

    def remove_dup_kon_pln(self, subsheet_name, dictrionary):
        scope = ['https://www.googleapis.com/auth/spreadsheets',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('keysPLN.json', scope)
        client = gspread.authorize(creds)
        workbook = client.open("client_PLN")
        sheet2 = workbook.worksheet(subsheet_name)
        # Pobranie wszystkich wartości z arkusza
        values = sheet2.get_all_values()
        # Tworzenie listy unikalnych wartości z zachowaniem kolejności
        unique_values = []
        seen_values = set()
        for row in values:
            row[2] = row[2].replace('zł', '')
            row[2] = row[2].replace(',', '')
            row[2] = row[2].replace('.', ',')
            row[3] = row[3].replace('zł', '')
            row[3] = row[3].replace(',', '')
            row[3] = row[3].replace('.', ',')
            key = (row[1], row[2], row[3])
            if key not in seen_values:
                print(key)
                unique_values.append(row)
                seen_values.add(key)
        # Wyczyszczenie istniejących danych na arkuszu
        sheet2.clear()
        # Przywrócenie niezmienionych wartości z kolumny B i wstawienie funkcji FINDSIMILARTEXT()
        for i, row in enumerate(unique_values):
            formula = f"=X.WYSZUKAJ(B{i+1};{dictrionary}!A$2:A;{dictrionary}!C$2:C;\"Brak Produktu\")"
            row[0] = formula
        # Zapis unikalnych wartości z zachowaniem kolejności
        sheet2.append_rows(unique_values, value_input_option="USER_ENTERED")



