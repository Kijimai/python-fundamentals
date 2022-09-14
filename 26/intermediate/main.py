with open('./file1.txt') as file:
  file_one = file.readlines()
file_one = [item.strip() for item in file_one]

with open('./file2.txt') as file:
  file_two = file.readlines()
file_two = [item.strip() for item in file_two]  

result = [int(num) for num in file_one if num in file_two]
# Write your code above 👆

print(result)