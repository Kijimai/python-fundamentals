from art import logo
# from replit import clear
# HINT: You can call clear() to clear the output in the console.

print(logo)
keep_going = True

all_bidders = []


def add_bidder(name, bid_amount):
    print()
    all_bidders.append({"bidder": name, "bid": bid_amount})
    print(all_bidders)


def find_largest_bid():
    winner = {"bid": 0, "bidder": ""}
    for bidder in all_bidders:
        if bidder["bid"] > winner["bid"]:
            winner["bid"] = bidder["bid"]
            winner["bidder"] = bidder["bidder"]
    print(
        f"The largest bid was {winner['bid']} by {winner['bidder']}!")


while keep_going:
    name=input("What is the bidder's name? ")
    bid_price=int(input("What is their bid? $"))
    add_bidder(name, bid_price)
    answer=input("Bidder added! Keep going? type 'yes' or 'no'").lower()
    if answer == "yes":
        keep_going=True
    else:
        keep_going=False
        find_largest_bid()
