"""
Added Name_Not_Blank v4
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


# Main routine

# Data structures

# Ask for instructions

# Loop to get ticket details:

#   Get name (can't be blank)
TICKETS = 5
count = 0
name = ""
while count != TICKETS and name != "Xxx":
    if TICKETS - count > 1:
        print(f"\nYou have {TICKETS - count} seats left")
    else:
        print("\nYou have ONLY ONE ticket remaining")
    name = name_not_blank("What is your name? ")
    if name != "Xxx":
        count += 1

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
