def snack_price_(corn, mms, pc, water):
    total = 0
    total += POPCORN * corn
    total += WATER * water
    total += PC * pc
    total += MMS * mms
    return total


POPCORN = 2.5
MMS = 3
PC = 4.5
WATER = 2

print(snack_price_(int(input("Corn ")), int(input("mms ")), int(input("pc ")),
                   int(input("Water "))))
