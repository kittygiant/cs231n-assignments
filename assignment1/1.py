import pandas as pd


# s = "Date,Price,Volume\n2014-01-27,550.50,1387\n2014-06-23,910.83,4361\n2014-05-20,604.51,5870"
# date_idx = s.split('\n')[0].split(',').index('Date')
# dates = [s.split(',')[date_idx] for s in s.split('\n')[1:]]

# p = pd.to_datetime(dates).sort_values()
# (p[-1] - p[0]).days


def diff_days(s: str) -> int:
    date_idx = s.split('\n')[0].split(',').index('Date')
    dates = [s.split(',')[date_idx] for s in s.split('\n')[1:]]
    dates = [d for d in dates if d]

    p = pd.to_datetime(dates).sort_values()
    return (p[-1] - p[0]).days


print(diff_days("Date,Price,Volume\n2014-01-27,550.50,1387\n2014-06-23,910.83,4361\n2014-05-20,604.51,5870"))
print(diff_days('Date\n2000-01-01\n2000-01-01\n'))
