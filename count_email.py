def count_email():
    fhand = open("C:/Users/johnn/Google Drive/Programming/Coursera/Python/code3/mbox-short.txt")
    filehand = open("mbox_email.txt", "w")
    print("Checking each line in the text file")
    emailcount = dict()
    emaildomain = {}
    DayOfWeek = dict()
    for each_line in fhand:
        if each_line.startswith("From "):
            filehand.write(each_line)
            pieces = each_line.split()
            email = pieces[1]
            domain = email.split("@")
            emailcount[email] = emailcount.get(email, 0) + 1
            emaildomain[domain[1]] = emaildomain.get(domain[1], 0) + 1
            if len(pieces) >2:
                DayOfWeek[pieces[2]] = DayOfWeek.get(pieces[2], 0) + 1
    fhand.close()
    filehand.close()
    print(emailcount)
    print(max(emailcount))
    print(DayOfWeek)
    MaxDictVal = max(DayOfWeek, key=DayOfWeek.get)
    print(MaxDictVal)
    print(max(DayOfWeek))
    print(emaildomain)
    MaxDictVal2 = max(emaildomain, key=emaildomain.get)
    print(MaxDictVal2)
    print(max(emaildomain))

count_email()
