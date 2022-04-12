"""
Added Snacksv4.py
"""


# Import statements
import pandas


# Functions
def check_string(valid, question):
    answer = input(question).lower()
    if answer == "x":
        return "quit"
    for e in valid.keys():
        if answer in valid[e]:
            return e
    return "Not valid"


def get_snacks():
    snackers = [0, 0, 0, 0]
    while True:
        reply = check_string(yes_no_dict, "Would you like some snacks? We've "
                                          "got; popcorn, m&ms, pita chips, "
                                          "and water. ")
        if reply == "yes":
            while True:
                reply = check_string(snacks_dict, "\nWhat snacks would you like "
                                                  "to order? Press 'x' to"
                                                  " finish: ")
                if reply != "Not valid" and reply != "quit":
                    amount = check_int("How many of these do you want? ")
                    if reply == "popcorn":
                        snackers[0] += amount
                    elif reply == "m&ms":
                        snackers[1] += amount
                    elif reply == "pita chips":
                        snackers[2] += amount
                    else:
                        snackers[3] += amount
                elif reply == "Not valid":
                    print("That's not a snack!")
                elif reply == "quit":
                    for a in snackers:
                        if a < 0:
                            snackers[snackers.index(a)] = 0
                    if snackers != [0, 0, 0, 0]:
                        print("\nSummary of your order: ")
                        print(f"You ordered {snackers[0]} popcorns")
                        print(f"You ordered {snackers[1]} m&ms")
                        print(f"You ordered {snackers[2]} pita chips")
                        print(f"You ordered {snackers[3]} waters")
                    return snackers
        elif reply == "no":
            print("Okay, no snacks")
            return snackers
        else:
            print("That was not a valid answer, please type yes or no")


def name_not_blank(question):
    while True:
        namer = input(question).title()
        if namer == "" or namer.isspace():
            print("Please ensure you have entered this correctly, and not lef"
                  "t it blank")
        else:
            return namer


def check_int(question):
    while True:
        try:
            number = int(input(question))
        except ValueError:
            print("Please enter a whole number")
        else:
            return number


def price_check(user_age):
    low_range = range(12, 16)
    middle_range = range(16, 65)
    child_price = 7.50
    middle_price = 10.50
    old_price = 6.50
    if user_age in low_range:
        ticket_price = child_price
    elif user_age in middle_range:
        ticket_price = middle_price
    else:
        ticket_price = old_price
    return ticket_price


class Person:
    def __init__(self, age_, ticket_price, person, popcorns, mms, pc, waters):
        self.age_ = age_
        self.ticket_price = ticket_price
        self.person = person
        self.mms = mms
        self.popcorns = popcorns
        self.pc = pc
        self.waters = waters


# Main routine

# Data structures

# Ask for instructions

# Loop to get ticket details:

TICKETS = 5
TICKET_COST_PRICE = 5
ticket_count = 0
name = ""
LOWER = 12
UPPER = 110
profit = 0
names = []
namers = []
ticket_prices = []
yes_no_dict = {"yes": ["yes", "y"], "no": ["no", "n"]}
snacks_dict = {"popcorn": ["popcorn", "corn", "1", "p"],
               "m&ms": ["m&ms", "mms", "m", "2"],
               "pita chips": ["pita chips", "chips", "pc", "pita", "c", "3"],
               "water": ["water", "w", "4"]}
while ticket_count != TICKETS and name != "Xxx":
    if TICKETS - ticket_count > 1:
        print(f"\nYou have {TICKETS - ticket_count} tickets left")
    else:
        print("\nYou have ONLY ONE ticket remaining")
    name = name_not_blank("What is your name? ")
    #   Get name (can't be blank)
    if name != "Xxx":
        age = check_int(f"\nPlease enter {name}'s age: ")
        while True:
            if age < LOWER:
                print(f"Sorry, {name} is too young for this movie")
                break
            else:
                if age <= UPPER:
                    ticket_count += 1
                    #   Calculate ticket price
                    print(f"The price for {name}'s ticket is"
                          f" ${price_check(age):.2f}")
                    profit += price_check(age) - TICKET_COST_PRICE
                    snacks = get_snacks()
                    appender = Person(age, price_check(age), name, snacks[0],
                                      snacks[1], snacks[2], snacks[3])
                    names.append(appender)
                    break
                else:
                    age = check_int(f"\nAt {age}, {name} is very old, please"
                                    f" re-enter his age: ")
# Calculate total sales and profit
if ticket_count < TICKETS:
    print(f"\nYou have sold {ticket_count} tickets\nThere are sti"
          f"ll {TICKETS - ticket_count}"
          f" left")
else:
    print("\nYou have sold all the available tickets")
print(f"Total profit is ${profit:.2f}")
for item in names:
    namers.append(item.person)
    ticket_prices.append(item.ticket_price)
zipped = zip(namers, ticket_prices)
df = pandas.DataFrame(zipped, columns=["Name", "Prices"])
df = df.set_index("Name")
print(df)

#   Get age (between 12 and 130)

#   Ask for snacks

#   Calculate snack price

#   Ask for method of payment (apply surcharge if needed)


# Output data to file
