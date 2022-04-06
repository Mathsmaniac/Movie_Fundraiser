def price_check(age):
    low_range = range(12, 16)
    middle_range = range(16, 65)
    child_price = 7.50
    middle_price = 10.50
    old_price = 6.50
    if age in low_range:
        ticket_price = child_price
    elif age in middle_range:
        ticket_price = middle_price
    else:
        ticket_price = old_price
    return ticket_price


while True:
    user_age = int(input("Age? "))
    print(f"The cost of the tickets is ${price_check(user_age):.2f}")
