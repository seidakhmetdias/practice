import re
s=input()
a=re.search(r"[A-Za-z]+@[A-Za-z]+\.[A-Za-z]{2,}",s) 
if a:
    print(a.group())
