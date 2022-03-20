TICKETS = 5
count = 0
name = ""
while count != TICKETS and name != "Xxx":
    if TICKETS - count > 1:
        print(f"\nYou have {TICKETS - count} seats left")
    else:
        print("\nYou have ONLY ONE ticket remaining")
    name = input("What is your name? ").title()
    count += 1

if count < TICKETS:
    print(f"\nYou have sold {count} tickets\nThere are still {TICKETS - count}"
          f" left")
else:
    print("\nYou have sold all the available tickets")
