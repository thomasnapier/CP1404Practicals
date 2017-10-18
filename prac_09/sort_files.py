"""
CP1404/CP5632 Practical 09
Program which moves files into corresponding folders based on their extension
"""

import os
import shutil


def main():
    filetypes = [".txt", ".xlsx", ".xls", ".png", ".jpg", ".gif", ".docx", ".doc"]
    os.chdir("FilesToSort1")
    for filetype in filetypes:
        #  splits the name into a list based on the dot and takes the name element
        name = filetype.split('.')[1]
        os.mkdir("{}".format(name))
        for filename in os.listdir('.'):
            if not os.path.isdir(filename):
                if name in filename:
                    shutil.move(filename, name)

main()
