import os
print(os.getcwd())
try:
    with open("C:\\Users\\akhil\\Desktop\\canyoufindme.txt") as file: #no need to mention the path as it is in CWD (current working directory)
        print(file.read())
    print(file.closed)
except FileNotFoundError:
    print("file is not found")    