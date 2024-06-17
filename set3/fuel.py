
while True:
    try:
        str=input("Fraction: ")
        a, b=str.split('/')
        an=int(a)
        bn=int(b)
        if an>bn:
            raise ValueError
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if an/bn>=0.99:
            print("F")
        elif an/bn<=0.01:
            print("E")
        else:
            print(f"{round(100*an/bn)}%")
        break
    
