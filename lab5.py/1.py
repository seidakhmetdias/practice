import re
x=input()
a = re.findall("^Hello", x)
if a:
  print("Yes")
else:
  print("No")