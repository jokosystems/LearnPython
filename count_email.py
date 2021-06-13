def count_email():
    """This program scans through an a file and extracts the email addresses
    The dates of the email and the domain. It then prints the list and the highest number
    """
    f_hand = open("C:/Users/johnn/Google Drive/Programming/Coursera/Python/code3/mbox.txt")
    file_handle = open("mbox_email.txt", "w")
    print("Checking each line in the text file")
    email_count = dict()
    email_domain = {}
    day_of_week = dict()
    hour_time = dict()
    for each_line in f_hand:
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
    print(sum(sorted(day_of_week.values()))) # Prints the sum of all commits
    print(sorted(day_of_week.values())) # Prints number of commits
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



count_email()
