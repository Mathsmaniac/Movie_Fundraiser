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
while not UPPER >= age >= LOWER:
    age = check_int("\nPlease enter an integer between 12 and 110: ")
print(f"Age = {age}")
