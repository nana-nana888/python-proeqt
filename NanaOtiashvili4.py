# # davaleba 1
text = input("შეიყვანეთ ტექსტი: ")
text1 = ''.join(text.split()).lower()
 
if text1 == text1[::-1]:
    print("შეყვანილი ტექსტი არის პალინდრომი")
else:
    print("შეყვანილი ტექსტი არ არის პალინდრომი")



# davaleba 2


txt = input("შეიყვანეთ ტექსტი: ")
 
ascii = [ord(char) for char in txt]
 
print("ტექსტის სიმბოლოები:   ", ascii)
