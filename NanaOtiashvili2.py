# davaleba1
number = int(input ("please enter number: "))
if number % 2 == 0:
    print ("even")
else:
     print ("odd")

# davaleba2

text1 = input ("please enter text:  ")
if text1 in "small":
     print ("small")
elif text1 in "tall":
     print ("tall")
elif text1 in "middle":
     print ("middle")
else:
     print ("ტექსტში ეს სამი სიტყვა არ მოიძებნა")
     

#davaleba3

number1 = int(input ("please enter number1: "))
number2 = int(input ("please enter number2: "))
operator = input ("please enter math operator: ")
if operator == "+":
     print ("number1 + number2 =", number1 + number2)
elif operator == "-":
     print("number1 - number2 =", number1 - number2)
elif operator == "*":
     print("number1 * number2 =", number1 * number2)
elif operator == "/":
     print("number1 / number2 =", number1 / number2)
elif operator == "//":
     print("number1 // number2 =", number1 // number2)
elif operator == "%":
     print("number1 % number2 =", number1 % number2)
else:
     print("number1 ** number2 =", number1 ** number2)
