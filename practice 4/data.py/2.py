from datetime import date,timedelta
today=date.today()
res=today-timedelta(days=1)
res1=res+timedelta(days=1)
print(res,today,res1)