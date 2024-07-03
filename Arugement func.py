#Write a function that add it argument to the end of a list This is wrong.
# def Item_add(Goods, Item): THis is not correct, you'll have to assign my_items as a list. i.e () to []
#     list.append(Item)
#     return(Goods)

# my_items=("Car", "Phone" , "Perfume")
# Addition = "cash"
# New_Addition = Item_add(my_items, Addition)
# print(New_Addition) 
# print()

# def Item_add(x, y): #The correct one 
#     x.append(y)
#     return(x)

# my_items=["Car", "Phone" , "Perfume"]
# Addition = ["cash"]
# New_Addition = Item_add(my_items, Addition)
# print(New_Addition) 
# print()

# print(my_items+Addition)


# def something(this):
#     another_thing = list()
#     another_thing.append(this)
#     return another_thing

# something_else = something('west')
# print(something_else)
# another = Item_add([2,3,5], 'new') #another Method
# print(another)
# for i in Item2:
#   Item1.append(i)

# print(Item1)

# #Wrtie a f (x) to change the first element of your list to ABC
# Name =["Khadija", "Amina", "KDJ"]

# goods = ["20000kg", "50kg", "40kg"]
# input = input.strip("kg")
# print()

#Not Modifying the content of the list
# goods = ["20000kg", "50kg", "40kg"]
# def add_weights (weights):
#     total = 0
#     for weight in weights:
#         strval = weight.strip("kg") #String vaule (strval)
#         numval = int(strval)
#         total = total + numval #or total += numval
#     return total

# ans = add_weights(goods)
# print (ans)
# print("average is:", ans/3)
# print(f"average is:, {ans/3}")

# number = [2, 4, 5, 6, 4,8]
# def add_num (number):
#     total = 0
#     for num in number:
#         total = total + num
#     return total
# ans = add_num(number)
# print(ans)  

# [2, 4, 5, 6, 4,8]
# def totalsum (values):
#     total = 0
#     for val in values:
#         total = total + val
#     return total

# print(ans)  

# number = [2, 4, 5, 6, 4,8]
# def add_num (number):
#     total = sum(number)
#     return total
# ans2 = add_num(number)
# print(ans2)
    


# number = [2, 4, 5, 6, 4,8]
# def Average (number):
#     avg = ans/len(number)    
#     return avg

# ans = Average(number)
# print(f"average is:, {ans}")

medecine = ['paracetamol','sabutamol','waetamol','normanitamol']

# def add_ex(drug):
#     new_medecine=[]
#     for i in drug:
#         if i[-2:] == 'ol':
#             new_medecine.append(i+'ex')
#     print(new_medecine)
# add_ex(medecine)

def add_ex(drug):
    # new_medecine=[]
    for i in drug:
       print (i[:-2] + "ex")
print(add_ex(medecine))
    
#     print(new_medecine)
# add_ex(medecine)

# for i in medecine:
#     new_medecine=[]
#     # print(i)
#     if i[-2:] == 'ol':

#         new_medecine.append(i+'ex')
#     print(new_medecine)

# print('paracetamol'[-2:])# : means everything
# print('paracetamol'[-2])