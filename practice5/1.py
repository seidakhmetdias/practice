import re
pattern = r'ab*'   
text = input()
if re.fullmatch(pattern, text):
    print("Match")
else:
    print("No match")