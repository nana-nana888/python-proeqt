# davaleba1
number = int(input ("please enter number: "))
while number > 0:
    print (number)
    number -=1

print ("finished while cycle")


#davaleba2

total_sum = 0

while True:
    txt = input ("please enter text sum or number:  ")
    
    if txt == "sum":
        print(f"sum: {total_sum}")
        break

    try:

        number1 = int(txt)

        # number1 = int(input ("please enter number1:  "))

        if number1 > 0:
           total_sum += number1

    except ValueError:
        print ("please insert correct number or 'sum' ")
    
  
print ("finished while cycle")
        
    
# davaleba 3

import random
rand_numb = random.randint(1, 100)
lives = 5

print ("insert number from1 to 100, have 5 chance")

while lives > 0:
    numb = int (input("please write number: "))
    if numb == rand_numb:
        print ("this is random number")
        break
    elif numb > rand_numb:
        print ("this number is high")
    else:
        print ("this number is law")
    
    lives-=1
    print (f"lives: {lives}")
    

else:
    print (f"your live is up: {rand_numb}")   



   
