# 変数設定（日付）
import datetime , pytz
from dateutil.relativedelta import relativedelta

#before_date = datetime.datetime.now()
def period(start=0):
    tz = pytz.timezone('Asia/Tokyo') 
    start_date = datetime.datetime.now(tz)+ relativedelta(days=int(start))
    finish_date = start_date + relativedelta(days=-1)
    return start_date , finish_date