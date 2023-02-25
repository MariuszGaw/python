musclePain = False
fever = True
weakness = True

if musclePain and fever and weakness:
    print("Suspicion of influenza")
else:
    print("The flu is unlikely")



print("Check")

if musclePain and fever and weakness:
    print("Suspicion of influenza")
elif weakness:
    print("Take a rest")
else: 
    print("You may be cold")


print('----')

isMan = True

if (musclePain and fever and weakness) or (isMan and (musclePain or fever or weakness)):
    print("Suspicion of influenza")
elif weakness:
    print("Take a rest")
else: 
    print("You may be cold")



print('---')

isCheckCompleted = False

print("Check is cpmpleted" if isCheckCompleted else "Check not done yet!")
    

    
