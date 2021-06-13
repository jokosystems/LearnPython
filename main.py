# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    user_string = input("Enter your name: ")
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {user_string}')  # Press Ctrl+F8 to toggle the breakpoint.
    vowels = 0
    consonants = 0
    blanks = 0
    unknown = 0

    for each_character in user_string:
        if(each_character == 'a' or each_character == 'e' or each_character == 'i' or
           each_character == 'o' or each_character == 'u'):
            vowels += 1
        elif "a" < each_character < "z":
            consonants += 1
        elif each_character == " ":
            blanks += 1
        else:
            unknown += 1
    print(f"Total number of Vowels in user entered string is {vowels}")
    print(f"Total number of Consonants in user entered string is {consonants}")
    print(f"Total number of Blanks in user entered string is {blanks}")
    print(f"Total number of Unknown in user entered string is {unknown}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
