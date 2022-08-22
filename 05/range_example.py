# for n in range(1, 100, 3):
  # print(n)

# Up to but not including 101
total = 0
for n in range(1, 101):
  if n % 2 == 0:
    total += n
print(total)    

# with step included
# for n in range(0, 101, 2):
#   total += n
# print(total)  