import datetime

def solve(a,b):
    months = []
    for year in range(a, b + 1):
        for month in range(1, 13):
            first = datetime.datetime(year, month, 1, 0, 0, 0)
            last = datetime.datetime(year, month % 12 + 1, 1, 0, 0 , 0)
            days = (last - datetime.timedelta(days=1)).day
            if first.weekday() == 4 and days == 31:
                months.append(first.strftime("%b").capitalize())

    return (months[0], months[-1], len(months))
