def check_string(valid, question):
    answer = input(question).lower()
    if answer == "x":
        return "quit"
    for e in valid.keys():
        if answer in valid[e]:
            return e
    return "Not valid"


def surcharge(amount):
    while True:
        payment_method = check_string(pay_choices, "\nWhat payment method "
                                                   "will you be using; "
                                                   "credit or cash? ")
        if payment_method == "quit" or payment_method == "Not valid":
            print("Sorry, that's not a payment method")
        else:
            break
    if payment_method == "credit":
        return amount + amount * SURCHARGE_MULTIPLIER
    else:
        return amount


pay_choices = {"credit": ["cr", "credit"], "cash": ["cash", "coins", "ca"]}
SURCHARGE_MULTIPLIER = 0.05

print(surcharge(int(input("Amount: "))))
