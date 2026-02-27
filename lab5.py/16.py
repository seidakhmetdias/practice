import re
s=input()
m=re.search(r"name:\s*(\w+),\s*age:\s*(\d+)",s)

if m:
    print(m.group(1),m.group(2))