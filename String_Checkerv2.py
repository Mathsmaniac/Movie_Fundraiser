def check_string(valid, question):
    answer = input(question).lower()
    if answer == "x":
        return "quit"
    for item in valid.keys():
        if answer in valid[item]:
            return item
    return "Not valid"


snacks_dict = {"popcorn": ["popcorn", "corn", "1", "p"],
               "m&ms": ["m&ms", "mms", "m", "2"],
               "pita chips": ["pita chips", "chips", "pc", "pita", "c", "3"],
               "water": ["water", "w", "4"]}
while True:
    snack = check_string(snacks_dict, "What snack would you like? ")
    if snack == "quit":
        quit()
    else:
        print(snack)
