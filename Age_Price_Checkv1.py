def price_check(age):
    LOW_RANGE = range(12, 16)
    MIDDLE_RANGE = range(16, 65)
    CHILD_PRICE = 7.50
    MIDDLE_PRICE = 10.50
    OLD_PRICE = 6.50
    if age in LOW_RANGE:
        ticket_price = CHILD_PRICE
    elif age in MIDDLE_RANGE:
        ticket_price = MIDDLE_PRICE
    else:
        ticket_price = OLD_PRICE
    return ticket_price


while True:
    user_age = int(input("Age? "))
    print(f"The cost of the tickets is ${price_check(user_age):.2f}")
