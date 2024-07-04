# class BankAccount:
#     def __init__(self, account_name, account_number, initial_balance=0):
#         self.account_number = account_number
#         self.account_name = account_name
#         self.initial_balance = initial_balance


#     def describe(self):
#         print(self.account_name, self.account_name, self.initial_balance)

#     def deposit(self,amount):
#         self.initial_balance = self.initial_balance + amount #or self.balance +=amount is the same
#         print(f"deposit successful of {amount}, your new balance is {self.initial_balance}")

#     def Withdraw(self, amount):
#         self.intial_balance -= amount
#         print(f"successful withdraw of {amount}, your new balance is {self.initial_balance}")

#     def withdraw(self, amount):
#         self.initial_balance+= amount
#         if amount <=0:
#             print("insufficent fund")
        # return


    # def _str_(self):
    #     return str("An object of class Bankaccount")
    # def _str_(self):
    #     return str(f"this is an object of class BankAccount, with name: {self.name}")


# account1 = BankAccount("Alayo", 53212)
# account2 = BankAccount("Joy", 2356879, 2000) 

# account2.deposit(50000000)
# account1.Withdraw(300000)

# account1.describe()
# account1.deposit(500)
# account1.name = "dammy"
# account1.describe()
# account2.describe()

# account1.describe()
# account2.describe()

# print(account1)
# print(account2)

class Person():
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def Dperson(self):
        print(f"This is {self.name}, {self.age}year old, with an height of {self.height}cm")

class Student(Person):
    def students(self,Department):
        self.Department = Department 
        print(f"The student name is {self.name} {self.age},year old, with an height of {self.height}cm, and in {self.Department}")

class Lecturer (Person):
    def lecturer(self, State): 
        self.State = State
        print(f"The lectuer name is {self.name} {self.age},year old, with an height of {self.height} from, {self.State}.")

Person1 = Person ("Alayo", 72, 50,)
Person2 = Student ("Adijat", 63, 65) #YOu can't add your new variable here, you can add new decleared   whenever you want to call out.
Person3 = Lecturer("Prof Atanda", 92, 65)

Person1.Dperson() 
Person2.students("BCH") #Whenever you want to call or print always use your class variable name not the class name.
Person3.lecturer("Oyo")





