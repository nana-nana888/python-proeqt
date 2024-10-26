 # davaleba 1

mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9 , 12, 34, 49]
sum = ( mylist[3] +  mylist[9] +  mylist[14] )
print ("sum=", sum)

 # davaleba 2

import random

rand_list=[]
n=20
for i in range(n):
	rand_list.append(random.randint (0,100))
print(rand_list)

newlist = [num for num in rand_list if num % 2 != 0]

if newlist:
    smallest = newlist[0]
    largest = newlist[0]

    for num in newlist:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    print("smallest number:", smallest)
    print("largest number:", largest)
else:
    print("no odd number")

# davaleba 3

my_list = [43, '22', 12, 66, 210, ["hi"]]

print (my_list.index(210))

my_list.append("hello")

my_list.pop(2)
print (my_list)

my_list2 = my_list.copy()
my_list2.clear()
print (my_list)
print (my_list2)

# davaleba 4

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

def add_matrices(mat_1, mat_2):
    result = []
    for i in range(len(mat_1)):
        sum = []
        for j in range(len(mat_1[i])):
            sum.append(mat_1[i][j] + mat_2[i][j])
        result.append(sum)
    return result

result_matrix = add_matrices(matrix1, matrix2)
print("matrix sum:")
for sum in result_matrix:
    print(sum)


# davaleba 5

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def transpose_matrix(mat):
    transposed = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat[i])):
            row.append(mat[j][i])
        transposed.append(row)
    return transposed
transposed_matrix = transpose_matrix(matrix)


print("transposed matrix:")
for row in transposed_matrix:
    print(row)


# davaleba 6

import random

matrix = [[random.randint(1, 100) for _ in range(4)] for _ in range(4)]

for rand_matrix in matrix:
    print(rand_matrix)

