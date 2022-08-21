student_heights = input("Please input a list of student heights. ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

student_count = 0
total_height = 0
for height in student_heights:
    student_count += 1
    total_height += height
print(round(total_height / student_count))
