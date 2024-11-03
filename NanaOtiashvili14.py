# class BankAccount:
#     def __init__(self, account_number, account_holder, balance=0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"{amount} deposit money")
#         else:
#             print("error:The amount must be positive")

#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print(f"{amount} withdraw money")
#             else:
#                 print("error: not enough money")
#         else:
#             print("error:The amount must be positive.")

#     def __str__(self):
#         return f"BankAccount(account_number={self.account_number}, account_holder={self.account_holder}, balance={self.balance})"


# account1 = BankAccount(account_number="111111", account_holder="anaana")
# account2 = BankAccount(account_number="222222", account_holder="sabasaba", balance=100)

# account1.deposit(200)
# account1.withdraw(100)

# account2.deposit(300)
# account2.withdraw(100)  
# account2.withdraw(500)

# print(account1)
# print(account2)



class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} append in the course: {course}.")
        else:
            print(f"{self.name} is already in the course: {course}.")

    def show_info(self):
        return f"student: {self.name}, ID: {self.student_id}"

    def show_courses(self):
        if self.courses:
            print(f"{self.name} Registered for the following courses: {', '.join(self.courses)}")
        else:
            print(f"{self.name}Not registered for courses.")

student1 = Student(name="Ana", student_id="11111")
student2 = Student(name="Saba", student_id="22222")

student1.enroll("graphic design")
student1.enroll("architecture")
student2.enroll("political science")
student2.enroll("economy")

print(student1.show_info())
student1.show_courses()

print(student2.show_info())
student2.show_courses()
