# class BankAccount:
#     def __init__(self, account_name, account_number, initial_balance=0):
#         self.account_number = account_number
#         self.account_name = account_name
#         self.balance = initial_balance


#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         return self.balance

#     def withdraw(self, amount):
#         if amount > self.balance:
#             return print("Insufficient funds")
#         self.balance = self.balance - amount
#         return self.balance

#     def check_balance(self):
#         return self.balance


# acct1 = BankAccount("Khadija", 2134568790, 7500000 )
# acct2 = BankAccount("Adelayo", 6138568396, 5500000 )
# acct3 = BankAccount("Alayo", 2134594795, 3500000 )
# acct2.withdraw(100000)

# print(acct1.account_name,acct1.check_balance())
# print(acct2.account_name, acct2.check_balance())
# print(acct3.account_name, acct3.check_balance())


# print('====================================================')


# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

#     def display_details(self):
#         print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")


# class Student(Person):
#     def __init__(self, name, age, address, student_id, major):
#         super().__init__(name, age, address)
#         self.student_id = student_id
#         self.major = major

#     def display_details(self):
#         super().display_details()
#         print(f"Student ID: {self.student_id}, Course: {self.major}")


# class Lecturer(Person):
#     def __init__(self, name, age, address, employee_id, department):
#         super().__init__(name, age, address)
#         self.employee_id = employee_id
#         self.department = department

#     def display_details(self):
#         super().display_details()
#         print(f"Employee ID: {self.employee_id}, Department: {self.department}")


# student = Student("Labake", 20, "Tanke", "S12345", "Computer Science")
# student.display_details()

# lecturer = Lecturer("Romoke", 35, "Sango", "E12345", "Mathematics")
# lecturer.display_details()



    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return print("Insufficient funds")
        self.balance = self.balance - amount
        return self.balance

    def check_balance(self):
        return self.balance


acct1 = BankAccount("Khadija", 2134568790, 7500000 )
acct2 = BankAccount("Adelayo", 6138568396, 5500000 )
acct3 = BankAccount("Alayo", 2134594795, 3500000 )
acct2.withdraw(100000)

print(acct1.account_name,acct1.check_balance())
print(acct2.account_name, acct2.check_balance())
print(acct3.account_name, acct3.check_balance())


print('====================================================')


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")


class Student(Person):
    def __init__(self, name, age, address, student_id, major):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.major = major

    def display_details(self):
        super().display_details()
        print(f"Student ID: {self.student_id}, Course: {self.major}")


class Lecturer(Person):
    def __init__(self, name, age, address, employee_id, department):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Employee ID: {self.employee_id}, Department: {self.department}")


student = Student("Labake", 20, "Tanke", "S12345", "Computer Science")
student.display_details()

lecturer = Lecturer("Romoke", 35, "Sango", "E12345", "Mathematics")
lecturer.display_details()

