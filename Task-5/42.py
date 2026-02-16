import os
path = input("Enter directory path: ")
if os.path.exists(path):
    print("Directory exists")
else:
    print("Directory does not exist")
