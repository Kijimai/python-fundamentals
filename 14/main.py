from random import randint
from art import logo, vs
from game_data import data
print(logo)


def get_data():
    found_item = data[randint(0, len(data))]
    return found_item


def compare(user_input: str, a_item: dict, b_item: dict):
    """Takes 3 paraments, the user input, and 2 dictionaries. Returns either the object passed in that has a larger follower count, or False."""
    a_follower, b_follower = a_item["follower_count"], b_item["follower_count"]
    print(a_follower, b_follower)
    if user_input == 'a' and a_follower > b_follower:
        return a_item
    elif user_input == 'b' and b_follower > a_follower:
        return b_item
    else:
        return False


def start_game():
    game_over = False
    winner = None
    score = 0
    while not game_over:
        a_item = winner or get_data()
        b_item = get_data()
        if b_item["name"] == a_item["name"]:
            b_item = get_data()
        a_name, b_name = a_item["name"], b_item["name"]
        a_description, b_description = a_item["description"], b_item["description"]
        a_country, b_country = a_item["country"], b_item["country"]

        print(f"Compare A: {a_name}, a {a_description} from {a_country}.")
        print(vs)
        print(f"Against B: {b_name}, a {b_description} from {b_country}.")
        user_input = input(
            "Who has more followers? Type 'A' or 'B':\n").lower()
        result = compare(user_input, a_item, b_item)

        if result:
            score += 1
            winner = result
            print(f"You're right! Current score: {score}")
        else:
            game_over = True
            print(f"Sorry that's wrong, Final score: {score}")


start_game()
