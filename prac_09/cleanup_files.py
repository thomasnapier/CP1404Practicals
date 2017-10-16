"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/Christmas')
    # print a list of all files (test)
    print(os.listdir('.'))

    # make a new directory
    os.mkdir('temp')

    # loop through each file in the (original) directory
    for filename in os.listdir('.'):
        # ignore directories, just process files
        if not os.path.isdir(filename):
            new_name = get_fixed_filename(filename)
            print(new_name)

            # Option 1: rename file to new name - in place
            # os.rename(filename, new_name)

            # Option 2: move file to new place, with new name
            shutil.move(filename, 'temp/' + new_name)

            # Processing subdirectories using os.walk()

            # os.chdir('..')  # .. means "up" one directory
            # for dir_name, subdir_list, file_list in os.walk('.'):
            #     print("In", dir_name)
            #     print("\tcontains subdirectories:", subdir_list)
            #     print("\tand files:", file_list)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # First, replace the spaces and .TXT (the easy part)
    basic_filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    if "_" not in basic_filename:
        filename_letters = list(basic_filename)
        for index, letter in enumerate(filename_letters):
            if index > 0 and letter.isupper() and filename_letters[index - 1].isalpha():
                filename_letters.insert(index, "_")
        basic_filename = "".join(filename_letters)


    return basic_filename


main()