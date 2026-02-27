import re
a=r'[a-z]+_[a-z]'
s=input()
res=re.findall(a,s)
print(*res)
