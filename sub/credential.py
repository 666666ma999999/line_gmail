import os , pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

token_path = './json/token.pickle'
email= 'uranaifree123@gmail.com'
json_gmail = './json/client_secret_296625983555-3kt08t3evu4pgqr6qk2le1mthsqm4co6.apps.googleusercontent.com.json'
#json_gmail = './json/client_secret_296625983555-nfpr21385o91bar9hd8d4i5lnqrrmqh6.apps.googleusercontent.com.json'


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
    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        
        else:
            flow = InstalledAppFlow.from_client_secrets_file(json_gmail , scopes_gmail)
            creds = flow.run_console()

    with open("token.pickle", "wb") as token:
        pickle.dump(creds, token)

    return creds


################ spreadsheet ####################
import gspread
from google.oauth2 import service_account


# 設定
json_spread = './json/linesales20230706-02-6b4702d6fd96.json'

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




'''
# 認証フローが初めて完了したときに自動的にtoken.jsonが作成されます
def get_credential_gmail():
    """
    アクセストークンの取得
    カレントディレクトリに pickle 形式でトークンを保存し、再利用できるようにする。（雑ですみません。。）
    """
    creds = None
    
    if os.path.exists(token_path):
        with open(token_path, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(json_gmail, scopes_gmail)
            creds = flow.run_console()
            
        with open(token_path, "wb") as token:
            pickle.dump(creds, token)

    return creds
'''
