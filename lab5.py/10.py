import re
s=input()
if (re.findall(r"dog",s))or(re.findall(r"cat",s)):
    print("Yes")
else:
    print("No")