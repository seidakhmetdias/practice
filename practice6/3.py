with open("sample.txt", "a") as file:
    file.write("This line was appended\n")

with open("sample.txt", "r") as file:
    print(file.read())