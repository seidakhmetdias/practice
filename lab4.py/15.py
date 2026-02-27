from datetime import datetime, timedelta

def parse_datetime(s):
    date_part, tz_part = s.split()
    sign = 1 if '+' in tz_part else -1
    hh, mm = map(int, tz_part[4:].split(':'))
    offset = timedelta(hours=hh, minutes=mm) * sign

    local_dt = datetime.strptime(date_part, "%Y-%m-%d")
    utc_dt = local_dt - offset
    return utc_dt, local_dt.month, local_dt.day, offset

def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

birth_utc, b_month, b_day, birth_offset = parse_datetime(input())
current_utc, _, _, _ = parse_datetime(input())

year = current_utc.year

while True:
    day = b_day
    if b_month == 2 and b_day == 29 and not is_leap(year):
        day = 28

    birthday_local = datetime(year, b_month, day)
    birthday_utc = birthday_local - birth_offset

    if birthday_utc >= current_utc:
        break

    year += 1

diff_seconds = int((birthday_utc - current_utc).total_seconds())

if diff_seconds <= 0:
    print(0)
else:
    days_left = (diff_seconds + 86400 - 1) // 86400
    print(days_left)