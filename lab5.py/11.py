import re
s=input()
z=re.findall(r"[A-Z]",s)
print(len(z))