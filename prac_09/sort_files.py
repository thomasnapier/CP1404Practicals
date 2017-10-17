import os
import shutil

filetypes = [".txt", ".xlsx", ".xls", ".png", ".jpg", ".gif", ".docx", ".doc"]
os.chdir("FilesToSort")

for filetype in filetypes:
    name = filetype.split('.')[1]
    os.mkdir("{}".format(name))
    for filename in os.listdir('.'):
        if not os.path.isdir(filename):
            if name in filename:
                shutil.move(filename, name)

