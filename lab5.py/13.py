import re
s=input()
a=re.findall(r"\b\w+\b",s)
print(len(a))