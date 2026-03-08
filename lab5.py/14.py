import re
s=input()
a=re.compile(r"^\d+$")
if a.match(s):
    print("Match")
else:
    print("No match")