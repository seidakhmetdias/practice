import re
pattern = r'ab{2,3}'   
text = input()
if re.fullmatch(pattern, text):
    print("Match")
else:
    print("No match")