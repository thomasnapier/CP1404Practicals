"""
CP1404/CP5632 Practical 09
Program to sort a selection of files based on what the user enters
"""


import os
import shutil


def main():
    os.chdir("FilesToSort2")
    file_types = get_file_types(os.getcwd())
    file_categories = user_organise_files(file_types)
    for file_category in file_categories:
        os.mkdir(file_category)
    for filename in os.listdir(os.getcwd()):
        if "." in filename:
            file_extension = filename.split(".")[1]
            for file_group, file_type in file_categories.items():
                if file_extension in file_type:
                    shutil.move(filename, file_group)


def get_file_types(directory):
    """Return a set of the extensions present in the current directory"""
    extensions = []
    for filename in os.listdir(directory):
        extension = filename.split(".")[1]
        extensions.append(extension)
    return set(extensions)


def user_organise_files(file_types):
    """Organise the files into 3 seperate lists in a dictionary and return the dictionary"""
    user_file_groups = {"Docs": [], "Spreadsheets": [], "Images": []}
    for file_type in file_types:
        user_choice = input("How do you want to categorize {} files?".format(file_type))
        while user_choice not in user_file_groups:
            print("Invalid selection")
            user_choice = input("How do you want to categorize {} files?".format(file_type))
        user_file_groups[user_choice].append(file_type)
    return user_file_groups


main()
