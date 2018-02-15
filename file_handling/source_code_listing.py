# Take a path and print all '.py' files with name, content along with line numbers
# filter files that contain only 'file' in filename
import os

base_dir = "F:\\DevEnv\\workspace\\PyCharmProjects\\python3\\file_handling"
pattern = "emp"
files = os.listdir(base_dir)
try:
    for file in files:
        if file.endswith(".py") and file.find(pattern) != -1:
            file_full_path = os.path.join(base_dir,file)
            print(file_full_path)
            print("-" * len(file_full_path))
            with open(file_full_path) as f:
                lines = f.readlines()
                linenum = 1
                for line in lines:
                    print( "{0:3d} {1}".format(linenum, line), end="")
                    linenum += 1
            print()
            print("=" * len(file_full_path))


except Exception as ex:
    print("Error: ",ex)