MIN_LIKES = 500
MIN_SHARES = 100
LIKE = 400
SHARE = 80

if LIKE >= MIN_LIKES and SHARE >= MIN_SHARES:
    print("Spełniona promocja")
else:
    if LIKE < MIN_LIKES:
        print("Za mało like")
    else:
        if SHARE < MIN_SHARES:  
            print("Za mało shares")                
        else:
            print("Promocja niespełniona")


if LIKE >= MIN_LIKES and SHARE >= MIN_SHARES:
    print("Spełniona promocja")
elif LIKE < MIN_LIKES:
    print("Za mało like")
else:
    print("Promocja niespełniona")



print('---','\n','---')

isPizzaOrdered = False
isBigDrinkOrdered = True
isWeekend = True

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Jest kupon")
else:
    if isWeekend:
        print("Promocja tylko w dni robocze")
    else:
        print("Nie ma wymaganego zamówienia")


print('-----')

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Jest kupon")
elif isWeekend:
    print("Promocja tylko w dni robocze")
else:
    print("Nie ma wymaganego zamówienia")

    



