from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from sub.credential import get_credential_gmail , get_credential_gs
from sub.aggregation import period
#from sub.spreadsheet import get_credential_gs



import sys

if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO



#呼び出しシート
file_name = 'LineSales'
sheet_name1 = 'sheet1'
sheet_name2 = 'sheet2'


'''
import os
token_path = './json/token.pickle'
print(os.path.exists(token_path))
'''

def search_query():

	#集計設定
	day = period(0 , -1)

	# メールの検索クエリ設定
	attachment = 'has:attachment'
	target_email = 'dev-line-fortune@linecorp.com'
	target_date = f'before:{day[0].strftime("%Y/%m/%d")} after:{day[1].strftime("%Y/%m/%d")}'


	query = f'from:{target_email} {target_date} {attachment}'

	return query

# Gmail APIのクライアントを作成
creds = get_credential_gmail()
service = build('gmail', 'v1', credentials=creds, cache_discovery=False)


'''
email= 'uranaifree123@gmail.com'
service = build('gmail', 'v1', credentials=creds, cache_discovery=False)
result = service.users().messages().list(userId=email).execute()
labels = result.get('labels', [])
'''




if __name__ == "__main__":
	query = search_query()
	#gc = get_credential_gs()
	#sh = gc.open(file_name)
	print(query)