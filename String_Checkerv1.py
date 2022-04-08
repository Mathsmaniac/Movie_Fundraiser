def check_string(valid, question):
    snack = input(question).lower()
    for item in valid.keys():
        if snack in valid[item]:
            return item
    return "Not valid"


snacks_dict = {"popcorn": ["popcorn", "corn", "1", "p"],
               "m&ms": ["m&ms", "mms", "m", "2"],
               "pita chips": ["pita chips", "chips", "pc", "pita", "c", "3"],
               "water": ["water", "w", "4"]}
while True:
    print(check_string(snacks_dict, "What snack would you like? "))
