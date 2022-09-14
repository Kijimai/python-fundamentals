weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
def convert_c_to_f(celsius):
  return celsius * (9/5) + 32

weather_f = {day: round(convert_c_to_f(temp), 1) for (day, temp) in weather_c.items()}


print(weather_f)