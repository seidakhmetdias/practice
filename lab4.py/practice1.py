from datetime import datetime
s=input()

user_date=datetime.strptime(s,"%Y-%m-%d")
today=datetime.now()

diff=today-user_date

print(diff.days)