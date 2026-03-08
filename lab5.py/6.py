import re
s = input()
a = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]+", s)
if a:
    print(a.group())
else:
    print("No email")