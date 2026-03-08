import re
s=input()
a=re.findall(r"\d{2,}",s)
print(*a)