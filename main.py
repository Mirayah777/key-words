def calculate_change (paid,price):
    change = paid - price
    return change


snack_price = 25
print("======= SNACK VENDING MACHINE ======= ")
print("this snack cost Rs.",snack_price)
print(" only 1,5,10 and 20 Rs. accepted")

total = 0 

while True:
    coin = int(input("insert a coin:"))
    if coin not in (1,5,10,20):
        print("invalid coin please try again")
        continue

    total += coin

    print("total money: ",total)

    if total >= snack_price:
        print("enough money inserted ~!")
        break

change = calculate_change (total,snack_price)
print("here is your snack ")
print(" your change is: ",change)

print(" THANK YOU")