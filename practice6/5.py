import os

filename = "sample_copy.txt"

if os.path.exists(filename):
    os.remove(filename)
    print("File deleted")
else:
    print("File not found")