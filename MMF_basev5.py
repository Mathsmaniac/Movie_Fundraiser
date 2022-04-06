"""
Added Age_Price_Check v3
Improved line spacing and changed a few words
"""


# Import statements

# Functions
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

#   Get age (between 12 and 130)

#   Ask for snacks

#   Calculate snack price

#   Ask for method of payment (apply surcharge if needed)


# Output data to file
