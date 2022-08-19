# reminder: BMI = weight / height ** 2
height = float(input("How tall are you in meters?\n"))
weight = float(input("How much do you weigh in kgs?\n"))
bmi = weight / (height ** 2)
print(bmi)

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal Weight")
elif bmi >= 25 and bmi < 30:
    print("overweight")
elif bmi >= 30 and bmi < 35:
    print("obese")
elif bmi >= 35:
    print("clinically obese")
