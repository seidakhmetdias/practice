from datetime import datetime
today=datetime.today()
res=today.replace(microsecond=0)
print(res)