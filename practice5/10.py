import re
s = input()   
result = re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()
print(result)