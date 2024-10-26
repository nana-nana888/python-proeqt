# #davaleba 1 
# def is_anagram():
#     str1 = input('please input a string:    ')
#     str2 = input('please input a string:    ')
#     return sorted(str1.replace(' ', '').lower()) == sorted(str2.replace(' ', '').lower())


# print (is_anagram())



# #davaleba 2

# def count_character(string, char):
#     return string.count(char)

# result = count_character("python is program language", "a")
# print(result)  


# davaleba 3 

def fibonachi(n):
    fibonachi1 = []
    a, b = 0, 1

    for _ in range(n):
        fibonachi1.append(a)
        a, b = b, a + b

    return fibonachi1

n = int(input('please input a number:  '))
result = fibonachi(n)
print(result)
