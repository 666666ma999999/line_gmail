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



def search_query(start_date , end_date):

	# メールの検索クエリ設定
	attachment = 'has:attachment'
	target_email = 'dev-line-fortune@linecorp.com'
	target_date = f'before:{start_date.strftime("%Y/%m/%d")} after:{end_date.strftime("%Y/%m/%d")}'

	query = f'from:{target_email} {target_date} {attachment}'


	return query

def main(start_date):
	#集計設定

	print(start_date)
	day = period(start_date)
	#データ集計
	query = search_query(day[0], day[1])
	

	creds_gmail = get_credential_gmail()
	print(creds_gmail)

	print(query)
	list_id = collect_gmail_id(creds_gmail , query)

	list_id = collect_gmail_id(creds_gmail , query)
	data = collect_gmail_data(creds_gmail , list_id , day[1])

	#データ書き込み
	creds_gs = get_credential_gs()
	gs_overwrite(creds_gs , file_name , sheet_name , data ,  day[1])

	print(data[0:1] , day[1])

	


if __name__ == "__main__":
	import sys
	args = sys.argv
	#print(args[1])
	main(args[1])
	#gs_delete(creds_gs , file_name , sheet_name , day[0] , -15 ,  -12)

	'''	
	main()
	'''