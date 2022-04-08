def get_snacks():
    while True:
        reply = check_string(yes_no_dict, "Would you like some snacks? We've "
                                          "got; popcorn, m&ms, pita chips, "
                                          "and water. ")
        if reply == "yes":
            while True:
                reply = check_string(snacks_dict, "What snacks would you like "
                                                  "to order? ")
                if reply != "Not valid" and reply != "quit":
                    print(f"You want {reply}")
                elif reply == "Not valid":
                    print("That's not a snack!")
                elif reply == "quit":
                    return
        elif reply == "no":
            print("Okay, no snacks")
            return
        else:
            print("That was not a valid answer, please type yes or no")


def check_string(valid, question):
    answer = input(question).lower()
    if answer == "x":
        return "quit"
    for item in valid.keys():
        if answer in valid[item]:
            return item
    return "Not valid"


yes_no_dict = {"yes": ["yes", "y"], "no": ["no", "n"]}
snacks_dict = {"popcorn": ["popcorn", "corn", "1", "p"],
               "m&ms": ["m&ms", "mms", "m", "2"],
               "pita chips": ["pita chips", "chips", "pc", "pita", "c", "3"],
               "water": ["water", "w", "4"]}

get_snacks()
