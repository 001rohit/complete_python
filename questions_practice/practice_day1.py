#1 write a python program to sum alll the items in a list 
# list1 = []
# for i in range(5):
#     value1 = int(input("Enter the number: "))
#     list1.append(value1)

# print(list1)
# sum = 0
# for i in range(0,len(list1)):
#     sum = sum+list1[i]

# print(sum)

#2 write a python program to multiply all the items in a list
# multi = 1
# for i in range(0, len(list1)):
#     multi = multi*list1[i]

# print(multi)

#3 write a python program to get the largest number from a list 

# list1 = []
# for i in range(5):
#     value1 = int(input("Enter the number: "))
#     list1.append(value1)

# print(list1)

# max = list1[0]
# for i in list1:
#     if (i>max):
#         max = i

#3 write a python program to get the largest number from a list 
# min = list1[0]
# for i in list1:
#     if(i<=min):
#         min = i
    
# print(min)

# . Write a Python program to count the number of strings from a given list of strings. 
# The string length is 2 or more and the first and last characters are the same.
# list3 = ['abc','xyz','aba',1221]

# ctr = 0
# for word in list3:
#     if (len(word) >1 and word[0] == word[-1]):
#         ctr = ctr +1

# print(ctr)

# tuple = ([(2,5),(1,2),(4,4),(2,3),(2,1)])
# def last(n):
#     return n[-1]
# def sort_list_last(tuples):
#     return sorted(tuples , key=last)
# # sorted(tuple,key=last)
# print(sort_list_last([(2,5),(1,2),(4,4),(2,3),(2,1)]))

# Write a Python program to remove duplicates from a list.

# original_list = [2,3,4,5,6,7]
# copy_list = original_list.copy()
# print(copy_list)

# . Write a Python program to check if a list is empty or not
# checkList1 = []

# if not checkList1:
#     print("List is empty")
# else:
#     print("List full fill")

# Write a Python program to clone or copy a list

# l = [20,10,35,60]
# c = l.copy()
# i = list(l)

# print(l)
# print(c)
# print(i)

#  Write a Python program to find the list of words that are longer than n from a given list of words.
# n = []
# for i in range(3):
#     name = input("Enter your name: ")
#     n.append(name)

# for i in n:
#     print(i)
    
#  Write a Python function that takes two lists and returns True if they have at least one common member

# L1 = ["Rahul",1,2,3,4]
# L2 = ["Rohit",10,12,6,7]

# result = False
# for x in L1:
#     for y in L2:
#         if x ==y:
#             result =  True

# print(result)

# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# colorLIst = ["Red","Green","White","Black","Pink","Yellow"]
# print(colorLIst)

# delete method

# del colorLIst[0]
# del colorLIst[-1]
# del colorLIst[-1]

# pop method
# colorLIst.pop(0)
# colorLIst.pop(-1)
# colorLIst.pop(-1)

# print(colorLIst)

# Write a Python program to print the numbers of a specified list after removing even numbers from it.

# num = [7,8,120,25,44,20,27]
# num = [x for x in num if x % 2 !=0]
# print(num)
# numList = []
# for i in num:
#     if(i%2!=0):
#         numList.append(i)
# print(numList)

# Write a Python program to access the index of a list.
# list = []
# n= int(input("How many type to take input Enter any number: "))
# print( )
# for i in range(n):
#        value1 = int(input("Enter any number: "))
#        list.append(value1)
# list1 = []
# for i in range(len(list)):
#         list1.append(i)

# print(list1)    

# Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.

# res = []
# n= int(input("How many type to take input Enter any number: "))
# for i in range(n):
#            value1 = int(input("Enter any number: "))
#            res.append(value1)

# if(res)

# check a prime number 
 
# n1 = 31
# count = 0
# for i in range(1,n1+1):
#     if(n1%i==0):
#         count= count+1
# if(count ==2):
#     print("The give number is prime number")
# else:
#     print("give number is not prime number")

# name = "hi my name is Rohit kumre "
# print(name)
# print(name.index("R"))
# print(name.count("Rohit"))
# print(name[0])

# if (15>7):
#     print("True")
# else:
#     print("False")
