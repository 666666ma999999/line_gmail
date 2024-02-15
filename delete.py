from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from sub.credential import get_credential_gmail , get_credential_gs
from sub.aggregation import period
from sub.gmail import collect_gmail_id , collect_gmail_data
from sub.spreadsheet import gs_overwrite , gs_delete


import sys

if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO


#呼び出しspシート
file_name = 'LineSales'
sheet_name = 'sheet1'



def main(end_date , start_date):
	#集計設定

	day = period()
	creds_gs = get_credential_gs()
	gs_delete(creds_gs , file_name , sheet_name , day[0] ,end_date ,  start_date )

	print(day[0])

	
if __name__ == "__main__":
	main(-55 , -30)
