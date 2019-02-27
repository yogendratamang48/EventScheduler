from datetime import datetime, timedelta
import pudb
#pudb.set_trace()
start_date = 'Saturday, Feb 23 2019'
start_hhmm = '12:30'
raw_date = ' '.join([start_date.split(', ')[-1], start_hhmm])
print(raw_date)
_date = datetime.strptime(raw_date, '%b %d %Y %H:%M')
print(_date)

_date1 = datetime.strptime('Feb 27 2019 15:00', '%b %d %Y %H:%M')
_date2 = datetime.strptime('Feb 27 2019 17:30', '%b %d %Y %H:%M')
_date3 = datetime.strptime('Feb 27 2019 20:30', '%b %d %Y %H:%M')

def check_live(start_time):
    end_time = start_time + timedelta(hours=2)
    if datetime.now() > start_time and datetime.now() < end_time:
        print("Match running")
        return 1
    elif datetime.now() < start_time:
        print("Match to happen")
        return 2

    elif datetime.now() > end_time:
        print("Match already happend")
        return 3

print("Completed")
check_live(_date1)
print("Running Check")
check_live(_date2)
print("To Happen")
check_live(_date3)
