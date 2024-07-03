LG_in_kwara = ["ilorin west", "ekiti", "oke-ero", "ifelodun","barutee","asa", "ilorin South", "Kaima"]

#Find Lg in the even position

length = len(LG_in_kwara) # This is called a function
# def double(x):
#     print (x * 2)
# for i in range((5)):
#     print(LG_in_kwara[i])

# for i in range (length):
#     print(LG_in_kwara[i])
#     print(LG_in_kwara[1:9:2])

# for i in range (1,length,2):
#     print(LG_in_kwara[i])

for i in range (length):
    if i % 2 == 1:
        print(LG_in_kwara[i])

#Or this method
# for i in range (length):
#     if (i+1) % 2 == 0:
#         print(LG_in_kwara[i])

# for i in range (length):
#     if (i+1) % 2 == 1:
#         print(LG_in_kwara[i])

# for i in range (length):
#     if i % 2 == 0:
#        print(LG_in_kwara[i]) 

#print all the LGA that start with vowels letter

# vowels = "aeiou"
# vowelsArray = [a, e, i, o, u]

# for char in vowels:
#     print(char)

# for i in range(length):
#     if LG_in_kwara[i][0] in vowels:
#         print(LG_in_kwara[i])   

# for lg in LG_in_kwara:
#     if lg[0] in vowels:
#         print(lg) 

# double(7)
# double(3)
# double(15)

# for i in range (length):
#     LG_in_kwara[i] =  LG_in_kwara[i]  + ' state'
#     print(LG_in_kwara[i])
  
# print(LG_in_kwara)

# for i in range (length):
#     LG_in_kwara[i] =  LG_in_kwara[i]  + ' LG'
#     print(LG_in_kwara[i])
  
