total_bill = 0
pizza_size = input("What size pizza would you like? s / m / l ")

if pizza_size.lower() == "s":
    total_bill += 15
elif pizza_size.lower() == "m":
    total_bill += 20
elif pizza_size.lower() == "l":
    total_bill += 25

with_pepperoni = input("Would you like pepperoni on your pizza? Y/N ")
if with_pepperoni.lower() == "y":
    if pizza_size == "s":
        total_bill += 2
    elif pizza_size == "m" or pizza_size.lower() == "l":
        total_bill += 3
with_cheese = input("Would you like extra cheese? Y/N ")
if with_cheese.lower() == "y":
    total_bill += 1


print(f"Your final bill is: {total_bill}.")

# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# total_bill = 0

# if size.lower() == "s":
#     total_bill += 15
# elif size.lower() == "m":
#     total_bill += 20
# elif size.lower() == "l":
#     total_bill += 25

# if add_pepperoni.lower() == "y":
#     if size == "s":
#         total_bill += 2
#     elif size.lower() == "m" or size.lower() == "l":
#         total_bill += 3
# if extra_cheese.lower() == "y":
#     total_bill += 1

# print(f"Your final bill is: ${total_bill}.")