year = int(input("Type in a year, we'll see if it is a leap year."))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap Year.")
else:
    print("Not leap year.")
