"""
Added Age_Int_Checkv3
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


# Main routine

# Data structures

# Ask for instructions

# Loop to get ticket details:

#   Get name (can't be blank)
TICKETS = 5
count = 0
name = ""
LOWER = 12
UPPER = 110
while count != TICKETS and name != "Xxx":
    if TICKETS - count > 1:
        print(f"\nYou have {TICKETS - count} seats left")
    else:
        print("\nYou have ONLY ONE ticket remaining")
    name = name_not_blank("What is your name? ")
    if name != "Xxx":
        age = check_int("\nPlease enter the age of the ticket-holder: ")
        while True:
            if age < LOWER:
                print("Sorry, you are too young for this movie")
                break
            else:
                if age <= UPPER:
                    count += 1
                    break
                else:
                    age = check_int(f"\nAt {age}, {name} is very old, please"
                                    f" re-enter his age: ")

if count < TICKETS:
    print(f"\nYou have sold {count} tickets\nThere are still {TICKETS - count}"
          f" left")
else:
    print("\nYou have sold all the available tickets")


#   Get age (between 12 and 130)

#   Calculate ticket price

#   Ask for snacks

#   Calculate snack price

#   Ask for method of payment (apply surcharge if needed)

# Calculate total sales and profit

# Output data to file
