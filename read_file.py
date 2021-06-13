def read_file():
    file_handler = open("egypt.txt")
    print("Printing each line in the text file")
    for each_line in file_handler:
        print(each_line)
    file_handler.close()


read_file()
