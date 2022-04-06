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


TICKET_COST_PRICE = 5.00
profit = 0
for i in range(4):
    user_age = int(input("\nAge? "))
    user_name = input("Name? ")
    profit += price_check(user_age) - TICKET_COST_PRICE
    print(f"For {user_name}, the cost of the ticket is"
          f" ${price_check(user_age):.2f}")
print(f"\nTotal profit is ${profit:.2f}")
