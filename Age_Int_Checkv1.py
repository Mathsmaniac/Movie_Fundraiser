def check_int(question, low, high):
    error = f"please enter a whole number between {low} and {high} (inclusive)"
    while True:
        try:
            number = int(input(question))
            if number > high or number < low:
                print(error)
            else:
                return number
        except ValueError:
            print(error)


age = check_int("\nPlease enter the age of the ticket-holder: ", 12, 110)
print(f"Age = {age}")
