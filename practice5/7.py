import re
text = input()
result = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), text)
print(result)