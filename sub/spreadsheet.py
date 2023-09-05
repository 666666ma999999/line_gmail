
import gspread
from google.oauth2 import service_account
import pandas as pd
from gspread_dataframe import set_with_dataframe

def gs_overwrite(credentials , file_name , sheet_name , data_add , get_date):

    sh = credentials.open(file_name)

    #元ファイルを読み込む
    wks = sh.worksheet(sheet_name)
    df_origin = pd.DataFrame(wks.get_all_records())

    #取得ファイルをシートに保存
    newday_wks = sh.add_worksheet(title=get_date.strftime("%Y/%m/%d"), rows='500', cols='3')
    set_with_dataframe(newday_wks, data_add)

    # sheet1の上書き保存
    df_overwrite= pd.merge(df_origin , data_add , on=['title' , 'pf'] , how='outer')

    #nan対策
    df_overwrite = df_overwrite.fillna(0)

    #小数点以下対策
    for c in df_overwrite.columns:
        #print(c, df_overwrite[c].dtype)
        if df_overwrite[c].dtype == 'float64':
            df_overwrite[c] = df_overwrite[c].astype('int64')

    set_with_dataframe(wks, df_overwrite)


def gs_delete(credentials , file_name , sheet_name , start_date , end_term  , start_term):

    from dateutil.relativedelta import relativedelta
    delete_day = [ (start_date + relativedelta(days=r)).strftime("%Y/%m/%d") for r in range(end_term , start_term)]

    sh = credentials.open(file_name)

    for d in delete_day:
        del_sheet = sh.worksheet(d) # passを通さないと 'str' object has no attribute 'id'
        sh.del_worksheet(del_sheet)
    
    print(delete_day)


def gs_connect_test(credentials , file_name):
    sh = credentials.open(file_name)
    wks = sh.add_worksheet(title="new worksheet", rows='100', cols='30')
    sh.del_worksheet(wks)
