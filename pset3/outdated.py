# implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636
# Then output that same date in YYYY-MM-DD format
# If the user’s input is not a valid date in either format, prompt the user again

months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
months2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]


def main():
    s = outdated("Enter date: ")
    print(s)

def outdated(prompt):
        while True:
            date = input(prompt)
            if '/' in date:
                date1 = date.split('/')
                try:
                    if '/' in date:
                        date1 = date.split('/')
                    x = int(date1[0])
                    y = int(date1[1])
                    z = int(date1[2])
                except (ValueError):
                    pass
                else:
                    if x not in months2:
                        pass
                    elif y not in days:
                        pass
                    else:
                        a = f"{z}-{x:02}-{y:02}"
                        return a
            elif ',' in date:
                try:
                    if ',' in date:
                        date1 = date.replace(",", "").split(" ")
                    x = date1[0]
                    y = int(date1[1])
                    z = int(date1[2])
                except (ValueError):
                    pass
                else:
                    if x not in months:
                        pass
                    elif y not in days:
                        pass
                    else:
                        for i in range(len(months)):
                            if x == months[i]:
                                a = f"{z}-{(i + 1):02}-{y:02}"
                                return a

main()