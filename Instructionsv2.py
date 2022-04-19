def check_string(valid, question):
    answer = input(question).lower()
    if answer == "x":
        return "quit"
    for item in valid.keys():
        if answer in valid[item]:
            return item
    return "Not valid"


def instructions():
    while True:
        response = check_string(yes_no_dict, "\nWould you like to see the instructions? ")
        if response != "yes" and response != "no":
            print("Please enter a valid input")
        if response == "yes":
            print(instructionser)
            return
        elif response == "no":
            print("No instructions")
            return


yes_no_dict = {"yes": ["yes", "y"], "no": ["no", "n"]}
instructionser = "The program will tell you how many of each ticket remain \n" \
               "The program will ask you your name for each ticket\n" \
                 "It will then ask you your age, this is to put you in the correct price bracket\n" \
                 "Then you will be asked whether you would like snacks,\n" \
                 " the method for ordering snacks is relatively straightforward\n" \
                 "you will be asked what snack you would like to order," \
                 " then how many of the snack you would like to order\n" \
                 "\nThen you will be asked for a valid method of payment\n" \
                 "be advised that using a credit card will add a 5% surcharge onto your order\n" \
                 "once each order is complete, you will have the option to quit, by typing 'xxx' when it asks for yo" \
                 "ur name"

instructions()
