"""
Export graph to csv
"""

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


def snack_price_(corn, mms, pc, water):
    total = 0
    total += POPCORN * corn
    total += WATER * water
    total += PC * pc
    total += MMS * mms
    return total


class Person:
    def __init__(self, age_, person, popcorns, mms, pc, waters):
        self.age_ = age_
        self.person = person
        self.mms = mms
        self.popcorns = popcorns
        self.pc = pc
        self.waters = waters
        self.ticket_price = price_check(age_)
        self.snack_price = snack_price_(popcorns, mms, pc, waters)
        self.total_price = self.ticket_price + self.snack_price
        self.surcharge = surcharge(self.total_price)
        self.snack_profit = self.snack_price * SNACK_PROFIT_MULTIPLIER
        self.ticket_profit = self.ticket_price - TICKET_COST
        if self.surcharge != 0:
            print(f"There is a surcharge of ${self.surcharge:.2f} for your order due to you using a credit card.")
        self.total_price += self.surcharge
        self.profit = self.ticket_profit + self.snack_profit
        print("-----------------------------------------------------")
        print(f"The total price for your order is ${self.total_price:.2f}")
        print("-----------------------------------------------------")
        self.total_price = currify(self.total_price)
        self.snack_price = currify(self.snack_price)
        self.surcharge = currify(self.surcharge)
        self.ticket_price = currify(self.ticket_price)


def surcharge(amount):
    while True:
        payment_method = check_string(pay_choices, "\nWhat payment method "
                                                   "will you be using; "
                                                   "credit or cash? ")
        if payment_method == "quit" or payment_method == "Not valid":
            print("Sorry, that's not a payment method")
        else:
            break
    if payment_method == "credit":
        return amount * SURCHARGE_MULTIPLIER
    else:
        return 0


def currify(number):
    return f"${number:.2f}"


# Main routine

# Data structures

# Ask for instructions

# Loop to get ticket details:

TICKETS = 5
ticket_count = 0
pay_choices = {"credit": ["cr", "credit"], "cash": ["cash", "coins", "ca"]}
SURCHARGE_MULTIPLIER = 0.05
TICKET_COST = 5
SNACK_PROFIT_MULTIPLIER = 0.2
POPCORN = 2.5
MMS = 3
PC = 4.5
WATER = 2
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
                    snacks = get_snacks()
                    appender = Person(age, name, snacks[0],
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


print("For more details, check out 'Snack_Profit_Data.csv', and 'All_Data.csv'")
chonk_zip = zip([item.person for item in names], [item.pc for item in names], [item.popcorns for item in names],
                [item.waters for item in names], [item.mms for item in names], [item.ticket_price for item in names],
                [item.snack_price for item in names], [item.surcharge for item in names],
                [item.total_price for item in names])
cdf = pandas.DataFrame(chonk_zip, columns=["Name", "Chips", "Popcorn", "Water", "M&Ms",
                                           "Ticket Cost", "Snack Cost", "Surcharge", "Total Cost"])
cdf = cdf.set_index("Name")
try:
    cdf.to_csv("All_Data.csv")
except PermissionError:
    pass
print("--*-- Summary data --*--")
zipped = zip([item.person for item in names], [item.ticket_price for item in names],
             [item.snack_price for item in names], [item.surcharge for item in names],
             [item.total_price for item in names])
df = pandas.DataFrame(zipped, columns=["Name", "Ticket Cost", "Snack Cost",
                                       "Surcharge", "Total Cost"])
df = df.set_index("Name")
print(df)
print("\n--*-- Snack/Profit summary --*--")
total_corn = (sum(item.popcorns for item in names))
total_water = (sum(item.waters for item in names))
total_mms = (sum(item.mms for item in names))
total_chips = (sum(item.pc for item in names))
snack_profits = (sum(item.snack_profit for item in names))
ticket_profits = (sum(item.ticket_profit for item in names))
total_profits = (sum(item.profit for item in names))
snack_dict = [{"Corn": total_corn, "Water": total_water, "M&Ms": total_mms, "Chips": total_chips,
              "Snack Profit": currify(snack_profits), "Ticket Profit": currify(ticket_profits),
               "Total Profit": currify(total_profits)}]
odf = pandas.DataFrame(snack_dict)
print(odf)
try:
    odf.to_csv("Snack_Profit_Data.csv")
except PermissionError:
    pass

#   Get age (between 12 and 130)

#   Ask for snacks

#   Calculate snack price

#   Ask for method of payment (apply surcharge if needed)


# Output data to file
