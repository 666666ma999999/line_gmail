# 変数設定（日付）
import datetime
from dateutil.relativedelta import relativedelta

#before_date = datetime.datetime.now()
def period(start , end): 
    start_date = datetime.datetime.now()+ relativedelta(days=start)
    finish_date = start_date + relativedelta(days=end)
    return start_date , finish_date