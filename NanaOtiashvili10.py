# davaleba 1
# a = (1, 2, 3)
# b= ('a', 'b', 'c')
# x = zip (a,b)
# print (tuple(x))


# davaleba 2

# lst = [1, 2, 3, 4, 5, 6, 7]
# even_numbers = list(filter(lambda x: x % 2 == 0, lst))
# print(even_numbers)

# davaleba 3

# lst1 = [1, -2, -3, -4, 5, 6, 7]
# positive_numbers = list(filter(lambda x: x>0, lst1))
# print(positive_numbers)


# davaleba 4

# lst2 = ["nana", "ana", "asa", "sos" "lambda"]
# palindromes = list(filter(lambda x: x == x[::-1], lst2))
# print(palindromes)


# davaleba 5
# from functools import partial, reduce
# try:
#     lst3 = [1, 2, 3, 4, 5]
#     sum_of_number = reduce(lambda a, b: a * b, lst3)
#     print(sum_of_number)
# except TypeError as e:
#     print ('Its type error')

# davaleba 6
try:
    string1 = ['hello', 'world', 'coding', 'nod']
    ending = 'ing'
    
    if not isinstance(string1, list) or not isinstance(ending, str):
        raise TypeError("error")

    output = list(filter(lambda x: x.endswith(ending), string1))
    print(output)

except TypeError as e:
    print('error:')
