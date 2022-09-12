# file = open("./my_txt.txt")

# the "with" keyword allows users to ensure that a resource is "cleaned up" when the code that uses it finishes running, even if exceptions are thrown.
# Advanced: Also provides syntactic sugar for try/finally blocks

# with open("./my_txt.txt") as file:
#     contents = file.read()
#     print(contents)

# w = overwrite, a = append, adds on top of existing text.
with open("./my_txt.txt", mode="a") as file:
    file.write("\nI overwrote the previous txt.")

# Manually close the file, so no resources are taken up if its not in use
# file.close()
