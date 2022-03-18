"""
Added Name_Not_Blank v3
"""


# Import statements

# Functions
def name_not_blank(question):
    while True:
        try:
            name = input(question)
            if name == "" or name.isspace():
                raise ValueError
        except ValueError:
            print("Please ensure you have entered this correctly, and not lef"
                  "t it blank")
        else:
            return name


# Main routine

# Data structures

# Ask for instructions

# Loop to get ticket details:

#   Get name (can't be blank)
name_not_blank("\nwhat is your name?")

#   Get age (between 12 and 130)

#   Calculate ticket price

#   Ask for snacks

#   Calculate snack price

#   Ask for method of payment (apply surcharge if needed)

# Calculate total sales and profit

# Output data to file
