# 1 year - 365 days, 52 weeks, 12 months
age_of_death = 90
age = int(input("How old are you?\n"))
years_remaining = age_of_death - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
