import os , pickle
from google.auth.transport.requests import Request
#from google_auth_oauthlib.flow import InstalledAppFlow
from oauth2client.service_account import ServiceAccountCredentials


token_path = './json/token.pickle'
#email= 'uranaifree123@gmail.com'
json_gmail = './json/linesales20230706-02-02dec7f26b1a.json'


scopes_gmail = [
    "https://www.googleapis.com/auth/gmail.compose",
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/gmail.modify"
]


# 認証フローが初めて完了したときに自動的にtoken.jsonが作成されます
def get_credential_gmail():
    """
    アクセストークンの取得
    カレントディレクトリに pickle 形式でトークンを保存し、再利用できるようにする。（雑ですみません。。）
    """
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_gmail, scopes=scopes_gmail)

    return creds
    


################ spreadsheet ####################
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

