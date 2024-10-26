# #davaleba 1

# int_list = [10, 20, 30, 40]

# def add_to_int_list(number):
#     global int_list 
#     int_list.append(number)

# add_to_int_list(50)
# print(int_list)

#davaleba 2

# def sum_of_digits(number):
#     if number == 0:
#         return 0
#     else:
#         return number % 10 + sum_of_digits(number // 10)

# result = sum_of_digits(12345)
# print(result)  

#დავალება 3

# def reverse_string(s):
#     if s == "":
#         return ""
#     else:
#         return s[-1] + reverse_string(s[:-1])
# result = reverse_string("Hello")
# print(result) 

#davaleba 4

def fibonachi(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)
n = 9
result = [fibonachi(i) for i in range(n)]
print(result)  
