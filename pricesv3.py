"""
Added a profit attribute
"""


def price_check(user_age):
    low_range = range(12, 16)
    middle_range = range(16, 65)
    child_price = 7.50
    middle_price = 10.50
    old_price = 6.50
    if user_age in low_range:
        ticket_price = child_price
    elif user_age in middle_range:
        ticket_price = middle_price
    else:
        ticket_price = old_price
    return ticket_price


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
        return amount * SURCHARGE_MULTIPLIER
    else:
        return 0


def snack_price_(corn, mms, pc, water):
    total = 0
    total += POPCORN * corn
    total += WATER * water
    total += PC * pc
    total += MMS * mms
    return total


pay_choices = {"credit": ["cr", "credit"], "cash": ["cash", "coins", "ca"]}
SURCHARGE_MULTIPLIER = 0.05
POPCORN = 2.5
MMS = 3
PC = 4.5
WATER = 2


class Person:
    def __init__(self, age_, person, popcorns, mms, pc, waters):
        self.age_ = age_
        self.person = person
        self.mms = mms
        self.popcorns = popcorns
        self.pc = pc
        self.waters = waters
        self.ticket_price = price_check(age_)
        self.snack_price = snack_price_(popcorns, mms, pc, waters)
        self.total_price = self.ticket_price + self.snack_price
        self.surcharge = surcharge(self.total_price)
        self.total_price += self.surcharge
        self.profit = (self.ticket_price - 5) + (self.snack_price * 0.2)
        print(f"Ticket price: ${self.ticket_price:.2f}")
        print(f"Snack price: ${self.snack_price:.2f}")
        print(f"Surcharge: ${self.surcharge:.2f}")
        print(f"Total price: ${self.total_price:.2f}")
        print(f"Profit: ${self.profit:.2f}")


# For testing purposes
marge = Person(85, "marge", 5, 0, 0, 0)
homer = Person(55, "homer", 2, 4, 7, 5)
lisa = Person(15, "lisa", 2, 3, 2, 0)
bart = Person(36, "bart", 4, 0, 2, 3)
