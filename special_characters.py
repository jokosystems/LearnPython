"""
import re


def main():
    pattern = re.compile(r"\b\d{3}-?\d{2}-?\d{4}\b")
    match_object = pattern.search("Social Security Number for James is 916-30-2017")
    if match_object:
        print(f"Extracted Social Security Number is {match_object.group()}")
    else:
        print("No Match")


if __name__ == "__main__":
    main()


ptern = re.compile(r'(?P<word>\b\w+\b)')
match_obj = ptern.search('laugh3 out2 loud')
match_obj.group('word')
print(match_obj.group(1))


# Write Python Program to Change the File Extension from .txt
# to .csv of All the Files (Including from Sub Directories) for a Given Path
import os
import glob


def rename_files_recursively(directory_path):
    print("File extension changed from .txt to .csv")
    for file_path in glob.glob(directory_path + '\**\*.txt', recursive=True):
        print(f"File with .txt extension {file_path} changed to", end="")
        try:
            pre, ext = os.path.splitext(file_path)
            print(f" File with .csv extension {pre + '.csv'} ")
            os.rename(file_path, pre + '.csv')
        except Exception as e:
            print(e)


def main():
    directory_path = input('Enter the directory path from which you want to convert the files recursively ')
    rename_files_recursively(directory_path)


if __name__ == "__main__":
    main()


# Write a Python program to search the numbers (0–9) of length between 1 to 3 in a given string.
import re

def rem_3_digits():
    pattern = re.compile(r'\s([0-9]{2,4})\s')
    strings = input('Enter the string to search within: ')
    found = pattern.search(strings)
    print(found.group())


if __name__ == "__main__":
    rem_3_digits()
"""

# Write a Python program to read a file and to convert a date of yyyy-mm-dd format
# to mm-dd-yyyy format.
import re
def change_date_format(dt):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\2-\\3-\\1', dt)


dt1 = "2026-01-28"
print("Original date in YYYY-MM-DD Format: ",dt1)
print("New date in MM-DD-YYYY Format: ",change_date_format(dt1))

# Check if the string starts with "The" and ends with "Spain":
txt = "Then rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x.group())
if x:
  print("YES! We have a match!")
else:
  print("No match")