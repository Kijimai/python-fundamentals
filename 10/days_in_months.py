# Docstring

def is_leap(year):
    """Take a year and returns a Boolean value if the year passed in is a leap year or not."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
                return True
            else:
                print("Not leap year.")
                return False
        else:
            print("Leap year.")
            return True
    else:
        print("Not leap year.")
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        if month - 1 == 1:
            return month_days[month-1] + 1
        else:
            return month_days[month - 1]
    elif not is_leap(year):
        return month_days[month-1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
