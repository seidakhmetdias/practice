import re
s=input()
p=input()
a=re.search(p,s)
if a:
    print("Yes")
else:
    print("No")