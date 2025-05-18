import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Crawlers import Crawlers

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('keysEUR.json', scope)
client = gspread.authorize(creds)

workbook = client.open("client_EUR")

class UpdateUrlsEUR:
    Crawlers = Crawlers()
    def kon_com_get_urls(self):
        sheet_kon_urls = workbook.worksheet("KonCOM URLS")
        sheet_kon_urls.clear()
        urls = self.Crawlers.kon_com_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list
        sheet_kon_urls.update('A2', data)
        self.Crawlers.quit_driver()

    def update_vs_urls(self):
        sheet_vs_urls = workbook.worksheet("VsCOM URLS")
        sheet_vs_urls.clear()
        urls = self.Crawlers.vs_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list

        # Update the sheet with the URLs
        sheet_vs_urls.update('A2', data)
        self.Crawlers.quit_driver()

    def update_vsDE_urls(self):
        sheet_vsDE_urls = workbook.worksheet("VsDE URLS")
        sheet_vsDE_urls.clear()
        urls = self.Crawlers.vsDE_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list

        # Update the sheet with the URLs
        sheet_vsDE_urls.update('A2', data)
        self.Crawlers.quit_driver()

    def update_vsNL_urls(self):
        sheet_vs_urls = workbook.worksheet("VsNL URLS")
        sheet_vs_urls.clear()
        urls = self.Crawlers.vsNL_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list

        # Update the sheet with the URLs
        sheet_vs_urls.update('A2', data)
        self.Crawlers.quit_driver()
    def update_vsFR_urls(self):
        sheet_vs_urls = workbook.worksheet("VsFR URLS")
        sheet_vs_urls.clear()
        urls = self.Crawlers.vsFR_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list

        # Update the sheet with the URLs
        sheet_vs_urls.update('A2', data)
        self.Crawlers.quit_driver()
    def update_vsES_urls(self):
        sheet_vs_urls = workbook.worksheet("VsES URLS")
        sheet_vs_urls.clear()
        urls = self.Crawlers.vsES_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list

        # Update the sheet with the URLs
        sheet_vs_urls.update('A2', data)
        self.Crawlers.quit_driver()


    def cbdr_com_get_urls(self):
        sheet_cbdr_urls = workbook.worksheet("CbdRCOM URLS")
        sheet_cbdr_urls.clear()
        urls = self.Crawlers.cbdr_com_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list

        sheet_cbdr_urls.update('A2', data)
        self.Crawlers.quit_driver()

    def vuj_com_get_urls(self):
        sheet_vs_urls = workbook.worksheet("VujCOM URLS")
        sheet_vs_urls.clear()
        urls = self.Crawlers.vuj_com_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list

        sheet_vs_urls.update('A2', data)
        self.Crawlers.quit_driver()

    def mv_com_get_urls(self):
        sheet_mv_urls = workbook.worksheet("MvCOM URLS")
        sheet_mv_urls.clear()
        urls = self.Crawlers.mv_com_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list

        # Update the sheet with the URLs
        sheet_mv_urls.update('A2', data)
        self.Crawlers.quit_driver()


    def mv_de_get_urls(self):
        sheet_mv_urls = workbook.worksheet("MvDE URLS")
        sheet_mv_urls.clear()
        urls = self.Crawlers.mv_de_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list

        # Update the sheet with the URLs
        sheet_mv_urls.update('A2', data)
        self.Crawlers.quit_driver()

    def mv_nl_get_urls(self):
        sheet_mv_urls = workbook.worksheet("MvNL URLS")
        sheet_mv_urls.clear()
        urls = self.Crawlers.mv_nl_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list

        # Update the sheet with the URLs
        sheet_mv_urls.update('A2', data)
        self.Crawlers.quit_driver()

    def mv_sk_get_urls(self):
        sheet_mv_urls = workbook.worksheet("MvSK URLS")
        sheet_mv_urls.clear()
        urls = self.Crawlers.mv_sk_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list

        # Update the sheet with the URLs
        sheet_mv_urls.update('A2', data)
        self.Crawlers.quit_driver()

    def mv_it_get_urls(self):
        sheet_mv_urls = workbook.worksheet("MvIT URLS")
        sheet_mv_urls.clear()
        urls = self.Crawlers.mv_it_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list

        # Update the sheet with the URLs
        sheet_mv_urls.update('A2', data)
        self.Crawlers.quit_driver()

    def mv_es_get_urls(self):
        sheet_mv_urls = workbook.worksheet("MvES URLS")
        sheet_mv_urls.clear()
        urls = self.Crawlers.mv_es_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list

        # Update the sheet with the URLs
        sheet_mv_urls.update('A2', data)
        self.Crawlers.quit_driver()

    def vn_com_get_urls(self):
        sheet_vn_urls = workbook.worksheet("Vn URLS")
        sheet_vn_urls.clear()
        urls = self.Crawlers.vn_com_get_urls()
        data = [[url] for url in urls]  # Convert each URL into a nested list

        # Update the sheet with the URLs
        sheet_vn_urls.update('A2', data)
        self.Crawlers.quit_driver()








