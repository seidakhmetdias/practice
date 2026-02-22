from datetime import datetime, timedelta

def parse_moment(s):
    d, tz = s.split()
    date = datetime.strptime(d, "%Y-%m-%d")
    sign = 1 if tz[3] == '+' else -1    
    h, m = map(int, tz[4:].split(':'))
    return date - timedelta(hours=h, minutes=m) * sign

m1 = parse_moment(input().strip())
m2 = parse_moment(input().strip())

print(int(abs((m1 - m2).total_seconds()) // 86400))