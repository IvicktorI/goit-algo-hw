import datetime as dt
from datetime import datetime as dtdt
import os
os.system('cls')

date='2011-11-11'

def get_days_from_today(date):
    try:
        tempDate=dtdt.strptime(date, "%Y-%m-%d").date()
        return (dt.date.toordinal(dtdt.today().date()) - dt.date.toordinal(tempDate))
    except Exception:
        return 'Incorrect data'
   
print(get_days_from_today(date))