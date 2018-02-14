# display total files and directories in a folder
import os

base_dir = "D:\Development\pycharmWorkspace\python3"
all_dirs = os.listdir(base_dir)
file_count = 0
dir_count = 0

for file in all_dirs:
    path = os.path.join(base_dir,file)
    if os.path.isdir(path):
        dir_count+=1
    else:
        file_count+=1

print(file_count, dir_count)


