due=50
while due>0:
    print("Amount Due:", due)
    coin=int(input("Insert Coin: "))
    if coin==5 or coin ==10 or coin==25:
        due=due-coin
        if due==0:
            print("Change Owed:", 0)
        elif due<0:
            print("Change Owed:", -due)

