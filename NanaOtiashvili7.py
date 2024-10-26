#davaleba 1

squared_numbers = [x for x in range(1, 11)]
set = {x: x**2 for x in range(1, 11)}
print (set)



#davaleba 2

string = input('please input a string:    ')

set_string = set (string)

print (set_string)



#davaleba 3

tuple1 = (1,2,3,4,5,6)
tuple2 = (4,5,5,6,6,7)

whole_tuple = tuple((set(tuple1)).union(set(tuple2)))
print (whole_tuple)

duplicated_values = tuple((set(tuple1)).intersection(set(tuple2)))
print (duplicated_values)




#davaleba 4
tuple1 = (1,2,3,4)
new_tuple = ((tuple1[-1],) + tuple1[1:-1] + (tuple1[0],))

print (tuple1)
print (new_tuple)



#davaleba 5

input_tuple = (1, (2, 3), (4, (5, 6)))

result = []

tuple_one = [input_tuple]  

while tuple_one:
    current = tuple_one.pop()  
    for item in current:
        if isinstance(item, tuple):
            tuple_one.append(item) 
        else:
            result.append(item)  

output_tuple = tuple(result)

print (output_tuple)


#davaleba 6

set1 = {1, 2}
set2 = {'a', 'b'}

output_set = {(x, y) for x in set1 for y in set2}

print("output:", output_set)