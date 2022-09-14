# new_dict = {new_key:new_value for item in list}
# Good for creating a map
import pandas as pd
from random import randint
# numbers = [1, 2, 3, 4, 5]
# my_dict = {num: num for num in numbers}
# # print(my_dict)
# existing_dict = {
#     "f_name": "James",
#     "l_name": "Bond",
#     "code_name": "007"
# }
# # new_dict = {new_key: new_value for (key, value) in dict.items()}
# newer_dict = {key + "1": value for (key, value) in existing_dict.items()}
# # print(newer_dict)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# scores = [89, 54, 55, 6, 25, 87]
# student_scores = {student: randint(50, 101) for student in names}
# # print(student_scores)
# passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)

student_dict = {
  "student": ["Angela", "James", "Lily"],
  "score": [56, 76, 89]
}

student_df = pd.DataFrame(student_dict)
# print(student_df)

# looping through a DataFrame

# for (key, value) in student_df.items():
#   print(value)

# Loop through rows of a DataFrame
for (index, row) in student_df.iterrows():
  # print(index)
  print(row.name)
  print(row.student)
  print(row.score)