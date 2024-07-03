# class
# my_list = [2,'good' ]
# our_list = [ 2, 4, 8]
# var = 4.2
# word = 'good'

# print(type(our_list))

# print(type(my_list))
# my_list.append('new')
# print(my_list)
# print(type(var))
# print(type(word))
# print(type({}))

class Car:
    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model= model
        # print('new instance of  car created')
    def describe(self):
        print(f'this is a {self.color} {self.make} {self.model}')



car1 = Car('blue', 'toyta', 'camry')
car2 = Car('white', 'honda', 'accord')
vehicle3 = Car('grey', 'lexus', 'jeep')

car1.describe()
# vehicle3.describe()
# print(vehicle3.color)
# car2.describe()
# car1.color = 'green'
# car1.describe()
# car1.make = 'venza'
# car1.describe()

# class Animal():
#     def __init__(self, age, weight, height, colour ):
#         self.age = age
#         self.weight = weight
#         self.height = height
#         self.color = colour

#     def describe(self):
#         print(f'this is a {self.age}yrs old {self.color} {self.weight} animal, with a height of {self.height}')


# class Mammal(Animal):

#    def describeMammal(self):
#         print(f'this is a {self.age}yrs old {self.color} {self.weight} mammal')

# cat1 = Mammal(3, '4kg', '15cm', 'blue')
# cat1.describe()
# cat1.describeMammal()


# a1 = Animal(5, '2kg', '15cm', 'black')
# a1.describe()
# a1.describeMammal()


# print(a1.weight)
# a1.weight = '7kg'
# a1.describe()