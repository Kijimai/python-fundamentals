# numbers = [1, 2, 3]
# new_list = [number + 1 for number in numbers]
# print(numbers)
# print(new_list)

# name_of_me = "john"
# new_name = [l + "-" for l in name_of_me]
# print(new_name)

# doubled_range = [n * 2 for n in range(1, 5)]
# print(doubled_range)

# conditional list comprehension


names = ["Alex", "Beth", "Dave", "Caroline", "Elanor", "Freddie"]

new_names = [name for name in names if len(name) < 5]
print(new_names)

capitalized_names = [name.upper() for name in names if len(name) > 5]

print(capitalized_names)