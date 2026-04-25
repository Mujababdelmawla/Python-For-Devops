import os 

folders = input("Please provide list of directories:").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder")
        continue

    print("====== listing the files ======" + folder)

    for file in files:
        print(files)
