student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

current_highest = 0
for score in student_scores:
  if current_highest < score:
    current_highest = score

print(current_highest)