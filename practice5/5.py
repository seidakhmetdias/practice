import re
a=r'^a.*b$'
s=input()
res=re.findall(a,s)
print(res)