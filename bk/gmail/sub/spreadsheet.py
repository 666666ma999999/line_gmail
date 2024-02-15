
import gspread
from google.oauth2 import service_account


# 設定
json_spread = './json/linesales20230706-02-25146e4e9b26.json'

scopes_spreadsheet = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive" ,
    "https://www.googleapis.com/auth/drive.file" ,
    "https://www.googleapis.com/auth/spreadsheets"
]

def get_credential_gs():

    credentials = service_account.Credentials.from_service_account_file(json_spread, scopes=scopes_spreadsheet)
    gc = gspread.authorize(credentials)


    return gc

