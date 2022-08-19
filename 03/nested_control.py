print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  age = int(input("How old are you?\n"))
  if age > 15:
    print("You can ride the rollercoaster!.. for 5 bucks.")
  elif age >= 18:
    print("Ticket's gonna cost you 9$")  
  else:
    print("You are not old enough to ride the rollercoaster!")   
elif height == 69:
  print("Nice.")
else: 
  print("You're not tall enough to ride the rollercoaster, sorry.")