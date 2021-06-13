def count_email():
    """This program scans through an a file and extracts the email addresses
    The dates of the email and the domain. It then prints the list and the highest number
    """
    import re
    filename = "mbox.txt"
    file_loc = "C:/Users/johnn/Google Drive/Programming/Coursera/Python/code3/"
    f_hand = open(file_loc + filename)
    file_handle = open("mbox_email.txt", "w")
    print("Checking each line in the text file")
    email_count = dict()
    email_domain = {}
    day_of_week = dict()
    hour_time = dict()
    count_letters = dict()
    for each_line in f_hand:
        # Counts each word in the file
        striped_line = re.sub('[^A-Za-z]+', '', each_line)  # Remove all non alphabet characters
        striped_line = striped_line.lower()
        for each_word in striped_line:
            count_letters[each_word] = count_letters.get(each_word, 0) + 1
        # Examines only lines that starts with "From "
        if each_line.startswith("From "):
            file_handle.write(each_line)
            pieces = each_line.split()
            email = pieces[1]
            domain = email.split("@")
            # Get hour time of day for each commit
            timestamp = pieces[5].split(":")
            hour_time[timestamp[0]] = hour_time.get(timestamp[0], 0) + 1
            email_count[email] = email_count.get(email, 0) + 1
            email_domain[domain[1]] = email_domain.get(domain[1], 0) + 1
            if len(pieces) > 2:
                day_of_week[pieces[2]] = day_of_week.get(pieces[2], 0) + 1
    f_hand.close()
    file_handle.close()
    print(email_count)
    print({key: value for key, value in email_count.items() if value == max(email_count.values())})
    print(day_of_week)
    print("This line will sort the dictionary according to day of week")
    print(sorted(day_of_week.items()))
    print(sum(sorted(day_of_week.values())))  # Prints the sum of all commits
    print(sorted(day_of_week.values()))  # Prints number of commits
    # Printed the day of the week in sorted order
    sorted_day_of_week = dict(sorted(day_of_week.items(), key=lambda x: x[1], reverse = True))
    print(sorted_day_of_week)
    [print(key, ':', value) for key, value in sorted_day_of_week.items()]
    print({key: value for key, value in day_of_week.items() if value == max(day_of_week.values())})
    # MaxDictVal = max(day_of_week, key=day_of_week.get)
    print(email_domain)
    # [print(key, ':', value) for key, value in email_domain.items()]
    max_email_domain = {key: value for key, value in email_domain.items() if value == max(email_domain.values())}
    print(f'The domain with highest users is ', max_email_domain)
    print("hourly distribution of commit: ")
    # [print(key,':',value) for key, value in hour_time.items()]
    print(count_letters)
    # print the letter occurrence in ascending order
    sorted_letter_count_by_value = dict(sorted(count_letters.items(), key=lambda x: x[1], reverse=True))
    # print(sorted_letter_count_by_key)
    [print(key, ':', value) for key, value in sorted_letter_count_by_value.items()]
    # sort the letter counts by keys (alphabet)
    sorted_letter_count_by_key = {}
    for i in sorted(count_letters):
        sorted_letter_count_by_key[i] = count_letters[i]
    from termcolor import colored
    print("\n")
    print("The letters occurrence in file: " + colored(filename, "green", attrs = ["bold"]) + " sorted alphabetically")
    print("The letters occurrence in " '\033[91m' + filename + '\033[0m' " sorted alphabetically")
    print("\n")
    [print(key, ':', value) for key, value in sorted_letter_count_by_key.items()]


count_email()
