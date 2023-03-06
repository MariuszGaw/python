
print('\n---1---\n')
number = 1
previousNumber = 0

while number <= 50:
    print(number, previousNumber,'+',number,'=', previousNumber+number)
    number+=1
    previousNumber+=1
          

print('\n---2---\n')

import random
my_number = random.randint(0,20)
guess=-1
trials = 0

print("Guess my number!")
 
while guess != my_number :
 
    guess = int(input())
    trials+ = 1
    
    if guess == my_number:
        print("You are right! It was:",my_number," Liczba prób:", trials)
    elif guess>my_number:
        print("Sorry- my number is smaller than", guess, "Try again!")
    else:
        print("Sorry- my number is greater than", guess, "Try again!")

