def check_int(question):
    while True:
        try:
            number = int(input(question))
        except ValueError:
            print("Please enter a whole number")
        else:
            return number


LOWER = 12
UPPER = 110
age = check_int("\nPlease enter the age of the ticket-holder: ")
while True:
    if age < LOWER:
        print("Sorry, you are too young for this movie")
        break
    else:
        if age <= UPPER:
            print(f"Age = {age}")
            break
        else:
            age = check_int(f"\nPlease enter a whole number between {LOWER} "
                            f"and {UPPER}: ")
