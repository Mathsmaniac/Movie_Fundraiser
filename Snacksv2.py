def get_snacks():
    snackers = [0, 0, 0, 0]
    while True:
        reply = check_string(yes_no_dict, "Would you like some snacks? We've "
                                          "got; popcorn, m&ms, pita chips, "
                                          "and water. ")
        if reply == "yes":
            while True:
                reply = check_string(snacks_dict, "What snacks would you like "
                                                  "to order? Press 'x' to"
                                                  " finish: ")
                if reply != "Not valid" and reply != "quit":
                    print(f"You want {reply}")
                    if reply == "popcorn":
                        snackers[0] += 1
                    elif reply == "m&ms":
                        snackers[1] += 1
                    elif reply == "pita chips":
                        snackers[2] += 1
                    else:
                        snackers[3] += 1
                elif reply == "Not valid":
                    print("That's not a snack!")
                elif reply == "quit":
                    return snackers
        elif reply == "no":
            print("Okay, no snacks")
            return []
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

amounts = get_snacks()
print(f"You ordered {amounts[0]} popcorns")
print(f"You ordered {amounts[1]} m&ms")
print(f"You ordered {amounts[2]} pita chips")
print(f"You ordered {amounts[3]} waters")
