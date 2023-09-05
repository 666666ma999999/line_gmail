from googleapiclient.discovery import build
from apiclient import errors
import logging

import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO


logger = logging.getLogger(__name__)


def collect_gmail_id(creds , query):
	service = build('gmail', 'v1', credentials=creds, cache_discovery=False)

	try:
		response = service.users().messages().list(userId='me', q=query , maxResults=500).execute()
		response_id = response.get('messages', [])
		return response_id

		if response_id["resultSizeEstimate"] == 0:
			logger.warning("no result data!")
			return []

	except errors.HttpError as error:
		print("An error occurred: %s" % error)



sales_daily = []

def collect_gmail_data(creds , list_id , day):
	service = build('gmail', 'v1', credentials=creds, cache_discovery=False)

	# attachmentId 取得
	for message_id in list_id[:]:
		msg = service.users().messages().get(userId='me', id=message_id['id']).execute()

		#partがないと添付ファイルが取れない
		parts =msg['payload']['parts']

		if parts:
			for part in parts:
				if 'filename' in part:
					body = part['body']

		#bodyの中にattachmentIdがないと添付ファイルが取れない
			if 'attachmentId' in body:
				attachment = service.users().messages().attachments().get(userId='me',messageId=message_id['id'],id=body['attachmentId']).execute()

				import csv , base64 , pandas as pd
				data = attachment['data']
				csv_data = base64.urlsafe_b64decode(data).decode('utf-8')
				df = pd.read_csv(StringIO(csv_data))


				web_sales = [df['service_name'][0] , 'web'  , df['web_paid_amount'].sum()]
				ios_sales = [df['service_name'][0] , 'ios'  , df['ios_paid_cost'].sum()]
				android_sales = [df['service_name'][0] , 'android'  , df['android_paid_cost'].sum()]

				sales_daily.append(web_sales)
				sales_daily.append(ios_sales)
				sales_daily.append(android_sales)

			else: print('no attachment')
		else: print('no part')

	df_sales = pd.DataFrame(sales_daily , columns=['title', 'pf', day.strftime("%Y/%m/%d")]) 

	return df_sales

'''
				# 添付ファイルのデータを取得
					hment['data']
						print(data)
		else:
			print('nodata')
			#message_id['id'])

		    # payload.headers[name: "Subject"]
         



		msg = service.users().messages().get(userId='me', id=service['id']).execute()
		payload = msg['payload']
		print(payload)

	return payload


    messages = []

    try:
    	for message in messages[:]:
			response = service.users().messages().list(userId='me', q=query).execute() #, maxResults=500).execute()
		    payload = msg['payload']


	    if 'parts' in payload:
	        parts = payload['parts']
	        for part in parts:
	            if 'filename' in part:
	                filename = part['filename']
	                body = part['body']

	                # 添付ファイルのデータを取得
	                if 'attachmentId' in body:
	                    attachment = service.users().messages().attachments().get(
	                    	userId='me', messageId=message['id'],id=body['attachmentId']
	                    ).execute()

  	except errors.HttpError as error:
    	print("An error occurred: %s" % error)

        # message id を元に、message の内容を確認
        for message_id in message_ids["messages"]:

            message_detail = (
                service.users()
                .messages()
                .get(userId="me", id=message_id["id"])
                .execute()
            )

            message = {}
            message["id"] = message_id["id"]
            
            # 単純なテキストメールの場合
            if 'data' in message_detail['payload']['body']:
                message["body"] = decode_base64url_data(
                    message_detail["payload"]["body"]["data"]
                )
            # html メールの場合、plain/text のパートを使う
            else:
                parts = message_detail['payload']['parts']
                parts = [part for part in parts if part['mimeType'] == 'text/plain']
                message["body"] = decode_base64url_data(
                    parts[0]['body']['data']
                    )

'''