#Option 1: Original code with minor changes

total = 50

while total > 0:                                                            # Loop until total is zero or less
    amount = int(input("Insert Coin: "))                                    # Ask user for coin input
    if amount == 25 or amount == 10 or amount == 5:                         # Check if the coin is valid, can also use if amount in (25, 10, 5):
        total -= amount                                                     #if valid, subtract from total
        if total > 0:                                                       # If total is still positive, print amount due
            print(f"Amount Due: {total}")                                   
        else:                                                               # If total is zero or less, exit loop
            break
    else:
        print(f"Amount Due: {total}")                                       # If coin is not valid, continue to next iteration
        continue
    
change = abs(total)                                                         # Calculate change owed
print(f"Change Owed: {change}")


#Functions practice
''''
def main():
    total = 50

    while total > 0:
        coin = get_coin()
        if coin in (25, 10, 5):
            total -= coin
            if total > 0:
                print(f"Amount Due: {total}")
            else:
                break
        else:
            print(f"Amount Due: {total}")
            continue
    
    change = abs(total)
    print(f"Change Owed: {change}")


def get_coin():
    amount = int(input("Insert Coin: "))
    return amount


main()
'''
