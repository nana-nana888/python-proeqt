sentence = input("write sentense: ")

filled_dict = {}
for word in sentence.lower().split():
    filled_dict[word] = filled_dict.get(word, 0) + 1

print(filled_dict)


# davaleba 2

# filled_dict = {
#     '+': lambda x, y: x + y,
#     '-': lambda x, y: x - y,
#     '*': lambda x, y: x * y,
#     '/': lambda x, y: x / y if y != 0 else "Cannot divide by zero"
# }


# num1 = float(input("first number:"))
# num2 = float(input("Second number: "))
# operator = input("choose operator (+, -, *, /): ")


# if operator in filled_dict:
#     result = filled_dict[operator](num1, num2)
#     print(f"result: {result}")
# else:
#     print("Unacceptable operator!")

number1 = int(input('please input a number'))
number2 = int(input('please input a number'))
operator = input ('Please input math operator')

operators_dict = {
    '+': number1 + number2,
    '-': number1 - number2,
    '*': number1 * number2,
    '/': number1 / number2

    }

print (operators_dict.get(operator, 'please enter operators (+,-,*,/)'))


#davaleba 3
# squares = {num: num**2 for num in range(1, 11)}
# print(squares)

lst = [x for x in range(1, 11)]
dct = {x: x**2 for x in range(1, 11)}
print(dct)



#davaleba 4
departments = {
    "HR": [
        {"name": "Ana", "surname": "Smith", "age": 30, "salary": 4000},
        {"name": "John", "surname": "Doe", "age": 25, "salary": 5200}
    ],
    "IT": [
        {"name": "Alice", "surname": "Johnson", "age": 28, "salary": 5800},
        {"name": "Bob", "surname": "Brown", "age": 35, "salary": 5900},
        {"name": "Sally", "surname": "Harington", "age": 25, "salary": 6900}
    ],
    "Marketing": [
        {"name": "Emma", "surname": "Davis", "age": 40, "salary": 4000},
        {"name": "Liam", "surname": "Wilson", "age": 29, "salary": 4500}
    ]
    
              }

# average_salaries = {dept: sum(emp['salary'] for emp in employees) / len(employees) 
#                     for dept, employees in departments.items()}


# for dept, avg_salary in average_salaries.items():
#     print(f"{dept} Average salary of the department: {avg_salary}")

# ან ასე

average_salaries = {}

for departament, employees in departments.items():
    total_salary = sum(employee['salary'] for employee in employees)
    employees_count = len(employees)
    average_salary = total_salary / employees_count
    average_salaries[departament] = average_salary

print(average_salaries)

