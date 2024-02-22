import os
path = "Python.txt"
print(path)

if os.path.exists(path):
    print("that file exists!")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("that is a directory")
else:
    print("that file doesnt exists!")            