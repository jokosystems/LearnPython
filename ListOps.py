""" # Program to Dynamically Build User Input as a List' \
list_items = input("Enter list items separated by a space ").split()
print(f"List items are {list_items}")

asc = des = True
temp = sorted(list_items)
temp1 = sorted(list_items, reverse=True)


if list_items != temp:
    asc = False
if list_items != temp1:
    des = False

if asc:
    print("Items in list are in Ascending order")
elif des:
    print("Items in list are in Descending order")
else:
    print("Items in list are not sorted")"""


# Write Python Program to Sort Words in a Sentence in Decreasing
# Order of Their Length. Display the Sorted Words along with Their Length
def sort_words(user_input):
    list_of_words = user_input.split()
    words = list()
    for each_word in list_of_words:
        words.append((len(each_word), each_word))
    print(words)
    words.sort(reverse=True)

    print("After sorting")
    print(words)

    for length, word in words:
        print(f'The word "{word}" is of {length} characters')


def main():
    sentence = input("Enter a sentence ")
    sort_words(sentence)


if __name__ == "__main__":
    main()

# Everything you can imagine is real
