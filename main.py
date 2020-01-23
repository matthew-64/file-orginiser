import os
path = "."

# read in all filenames
print("Reading all file names")
file_names = set()
for file in os.listdir(path):
    if file.endswith(".asc") | file.endswith(".prj"):
        file_names.add(file)

# create needed dirs
print("Creating needed directories")
dirs = set()
for file in file_names:
    dirs.add(file[:2])

sorted_dirs = list(dirs)
sorted(sorted_dirs)
for this_dir in sorted_dirs:
    if not os.path.exists(path + "/" + this_dir):
        os.makedirs(path + "/" + this_dir)

# move files
print("Moving files")
for file in file_names:
    os.replace(path + "/" + file, path + "/" + file[:2] + "/" + file)

print("done")
