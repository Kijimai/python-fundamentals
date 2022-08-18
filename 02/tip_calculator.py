total_bill = float(input("What was the total bill?\n"))
tip_percent = int(
    input("What percentage tip would you like to give? 10, 12 or 15?\n"))
person_count = int(input("How many people to split the bill with?\n"))
split_amount = round(total_bill * ((tip_percent / 100) + 1) / person_count, 2)

# Alternate rounding method
# split_amount = "{:.2f}".format(total_bill * ((tip_percent / 100) + 1) / person_count)

print(f"Each person should pay: ${split_amount}")
