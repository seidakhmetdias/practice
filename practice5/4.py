import re

a=r'[A-Z][a-z]+'
s=input()
res=re.findall(a,s)
print(res)