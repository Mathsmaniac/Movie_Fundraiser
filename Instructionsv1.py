def check_string(valid, question):
    answer = input(question).lower()
    if answer == "x":
        return "quit"
    for item in valid.keys():
        if answer in valid[item]:
            return item
    return "Not valid"


yes_no_dict = {"yes": ["yes", "y"], "no": ["no", "n"]}

while True:
    response = check_string(yes_no_dict, "\nWould you like to see the instructions? ")
    if response != "yes" and response != "no":
        print("Please enter a valid input")
    if response == "yes":
        print("Show instructions")
    elif response == "no":
        print("No instructions")
