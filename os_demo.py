# using OS module
import os

# current working directory
curr_dir = os.getcwd()
print(curr_dir)

# list of directories and files
dirs = os.listdir(r"D:\Development\pycharmWorkspace\python3")
# for d in dirs:
#     print(d)


all_dirs = os.walk(r"D:\Development\pycharmWorkspace\python3\oop")

for (dirname, directories, files) in all_dirs:
    print("Directory :", dirname)
    print("============" + "="*len(dirname))
    for file in files:
        print(file)