import datetime as dt
import calendar
def get_num_days_per_period(period_type, date_string):
    date = dt.datetime.strptime(date_string, "%Y-%m-%d")
    if period_type=="month":
        num_days = calendar.monthrange(date.year, date.month)[1]
    elif period_type=="quarter":
        quarter = (date.month - 1) // 3 + 1
        first_month = (quarter - 1) * 3 + 1
        final_month = quarter * 3
        num_days = 0
        for i in range(first_month, final_month+1):
            num_days += calendar.monthrange(date.year, i)[1]
    elif period_type=="year":
        num_days = 366 if calendar.isleap(date.year) else 365
    return num_days