import os

path = ".."

# read in all filenames
file_names = set()
for file in os.listdir(path):
    if file.endswith(".asc") | file.endswith(".prj"):
        file_names.add(file)


# create needed dirs
dirs = set()
for file in file_names:
    dirs.add(file[:2])

for this_dir in dirs:
    if not os.path.exists(path + "/" + this_dir):
        os.makedirs(path + "/" + this_dir)

# move files
for file in file_names:
    os.replace(path + "/" + file, path + "/" + file[:2] + "/" + file)


