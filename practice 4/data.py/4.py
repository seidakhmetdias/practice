from datetime import datetime, timedelta
today=datetime(2024, 6, 1,  12, 1, 30)
yesterday=datetime(2024, 6, 1, 12, 1, 0)
res=today-yesterday
print(int(res.total_seconds()))