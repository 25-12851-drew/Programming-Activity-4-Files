total = 0
items = 0

price = float(input("Price (0 to stop): "))

while price != 0:
    total = total + price
    items = items + 1

    price = float(input("Price (0 to stop): "))

print("Items:", items)
print("Total:", format(total, ".2f"))

if items > 0:
    average = total / items
    print("Average:", format(average, ".2f"))