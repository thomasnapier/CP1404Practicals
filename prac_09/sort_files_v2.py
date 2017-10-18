import os
import shutil

extensions = []
file_groups = {"Docs": [], "Spreadsheets": [], "Image": []}
os.chdir("FilesToSort2")
for filename in os.listdir(os.getcwd()):
    extension = filename.split(".")[1]
    extensions.append(extension)
file_types = set(extensions)

for file_type in file_types:
    user_choice = input("What category would you like to sort {} files into? ".format(file_type))
    while user_choice not in file_groups:
        print("Invalid category")
        user_choice = input("What category would you like to sort {} files into? ".format(file_type))
    file_groups[user_choice].append(file_type)

for file_group in file_groups:
    os.mkdir(file_group)

for filename in os.listdir(os.getcwd()):
    if "." in filename:
        file_extension = filename.split(".")[1]
        for files, file_type in file_groups.items():
            if file_extension in file_type:
                shutil.move(filename, files)