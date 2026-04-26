import chardet

with open("contacts.csv", "rb") as f:
    data = f.read()
    print(chardet.detect(data))