MIN_LIKES = 500
MIN_SHARES = 100
LIKE = 300
SHARE = 200

if LIKE >= MIN_LIKES and SHARE >= MIN_SHARES:
    print("Spełniona promocja")
else:
    print("Promocja niespełniona")






isPizzaOrdered = False
isBigDrinkOrdered = True
isWeekend = False

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Jest kupon")
else:
    print("Nie ma kuponu")




diskSize = 150
diskSizeUsed = 155
fileSize = 10

if diskSize - diskSizeUsed >= fileSize:
    print("File can be downloaded")

else:
    print("There is no space left")


