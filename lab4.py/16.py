from datetime import datetime, timedelta

def parse_utc(s):
    # YYYY-MM-DD HH:MM:SS UTC±HH:MM
    date_part, time_part, tz_part = s.split()

    local_dt = datetime.strptime(
        date_part + " " + time_part,
        "%Y-%m-%d %H:%M:%S"
    )

    sign = 1 if '+' in tz_part else -1
    hh, mm = map(int, tz_part[4:].split(':'))
    offset = timedelta(hours=hh, minutes=mm) * sign

    return local_dt - offset  # UTC time

start_utc = parse_utc(input())
end_utc = parse_utc(input())

duration = int((end_utc - start_utc).total_seconds())
print(duration)