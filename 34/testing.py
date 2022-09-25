def check_age_legal(age: int) -> bool:
  if age >= 21:
    return True
  else:
    return False
can_drink = check_age_legal(20)    
if can_drink:
  print("I can drink!")
else:
  print("I can't drink! :(")