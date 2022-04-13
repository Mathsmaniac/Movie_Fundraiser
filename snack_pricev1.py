def snack_price_(corn, mms, pc, water):
    total = 0
    total += snack_prices["popcorn"] * corn
    total += snack_prices["water"] * water
    total += snack_prices["chips"] * pc
    total += snack_prices["m&m"] * mms
    return total


snack_prices = {
    "popcorn": 2.5,
    "water": 2,
    "chips": 4.5,
    "m&m": 3,
}

print(snack_price_(int(input("Corn ")), int(input("mms ")), int(input("pc ")),
                   int(input("Water "))))
