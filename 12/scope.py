enemies = ['Zenos Yae Galvus', 'Zombie', 'Cactuar']

game_level = 3

# Globally Scoped variable
if game_level < 5:
    new_enemy = enemies[0]
print(new_enemy)

# Function Scoped Variable

def my_func():
    new_enemy = "Devil Dragon"
    print(new_enemy)


my_func()

# Constanst - Must be written in upper case to make into a global scope

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@BigBoi "