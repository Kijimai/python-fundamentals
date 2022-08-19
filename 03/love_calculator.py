lower_name1 = input("What is your name? ").lower()
lower_name2 = input("What is your crush's name? ").lower()

score1 = 0
score2 = 0

score1 += lower_name1.count('t')
score1 += lower_name2.count('t')
score1 += lower_name1.count('r')
score1 += lower_name2.count('r')
score1 += lower_name1.count('u')
score1 += lower_name2.count('u')
score1 += lower_name1.count('e')
score1 += lower_name2.count('e')

score2 += lower_name1.count('l')
score2 += lower_name2.count('l')
score2 += lower_name1.count('o')
score2 += lower_name2.count('o')
score2 += lower_name1.count('v')
score2 += lower_name2.count('v')
score2 += lower_name1.count('e')
score2 += lower_name2.count('e')

stringed_score = int(str(score1) + str(score2))
if stringed_score < 10 or stringed_score > 90:
  print(f"Your score is **{stringed_score}**, you go together like coke and mentos.")
elif stringed_score < 50 and stringed_score > 40:
  print(f"Your score is **{stringed_score}**, you are alright together.")
else:
  print(f"Your score is **{stringed_score}**.")  