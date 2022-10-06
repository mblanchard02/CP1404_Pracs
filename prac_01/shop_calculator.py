'''
shop_calculator program
Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92
'''

total = 0
amount = int(input("amount of items: "))
while amount < 0:
    print("not possible")
    amount = int(input("amount of items: "))
for i in range(amount):
    cost = float(input("cost of item: "))

    total += cost
    # to add discount when above $100
if total > 100:
    total *= 0.9

print("Total cost for {} items is ${:.1f}".format(amount, total))