from print_hi import print_hi
import sys

print("Hello World")
print_hi('PyCharm')


def function_definition_with_no_argument():
    print("This is a function definition with NO Argument")


def function_definition_with_one_argument(message):
    print(f'This is a function definition with {message}')


def ken():
    function_definition_with_no_argument()
    function_definition_with_one_argument("One Argument")


ken()


def main():
    print(f"sys.argv prints all the arguments at the command line including filename {sys.argv}")
    print(f"len(sys.argv) prints the total number of command line arguments including file name {len(sys.argv)}")
    print("You can use for loop to traverse through sys.argv")


for arg in sys.argv:
    print(arg)


if __name__ == "__main__":
    main()
