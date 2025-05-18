import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Crawlers import Crawlers

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('keysPLN.json', scope)
client = gspread.authorize(creds)

workbook = client.open("client_PLN")

class UpdateUrlsPLN:
    Crawlers = Crawlers()

    def update_kon_pl_urls(self):
        sheet_kon_urls = workbook.worksheet("KonPL URLS")
        sheet_kon_urls.clear()
        urls = self.Crawlers.konopny_pl_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list
        sheet_kon_urls.update('A2', data)
        self.Crawlers.quit_driver()

    def cbdr_pl_get_urls(self):
        sheet_cbdr_urls = workbook.worksheet("Brak")
        sheet_cbdr_urls.clear()
        urls = self.Crawlers.cbdr_pl_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list
        sheet_cbdr_urls.update('A2', data)
        self.Crawlers.quit_driver()

    def vuj_pl_get_urls(self):
        sheet_vuj_urls = workbook.worksheet("VujPL URLS")
        sheet_vuj_urls.clear()
        urls = self.Crawlers.vuj_pl_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list
        sheet_vuj_urls.update('A2', data)
        self.Crawlers.quit_driver()

    def vs_pl_get_urls(self):
        sheet_vs_urls = workbook.worksheet("VsPL URLS")
        sheet_vs_urls.clear()
        urls = self.Crawlers.vaporshop_pl_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list
        sheet_vs_urls.update('A2', data)
        self.Crawlers.quit_driver()














