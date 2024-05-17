# print("hellow")

# def print_hellow():
#     print("hellow")

# print_hellow()

# def print_sum(a,b):
#     print(a+b)

# print_sum(5,10)


# arr= [1,2,3,4,5]
# arr.sort(reverse=True)
# print(arr)

# for list in arr:
#     print(list)

# def check(num):
#     if(num%2==0):
#         print("The number is Even number")
#     else:
#         print("The number is Odd number")

# val = int(input("Enter any Number: "))
# check(val)

# def calc(a,b):
#     if(a%2==0 and b%2==0):
#         print("Both number is a Even number")
#     else:
#         print("The number is a Odd number")
#     # print(a+b)
    # print(a-b)
# calc(2,12)

# def check_prime(num):
#     count = 0
#     for i in range(1,num+1):
#         if(num%i==0):
#             count+=1
#     if(count==2):
#         print("The given number is prime number ")
#     else:
#         print("The give Number is Not prime number")
# x = int(input("Enter any number: "))
# check_prime(x)

# res = 0
# num1 = int(input("Enter any number: "))
# if(num1==0 and num1==1):
#     res =1
# for i in range(2,num1):
#     if(num1%i==0):
#         res = 1
# if res==1:
#     print(f"{num1} Number is not prime Number")
# else:
#     print(f"{num1} Number is a prime Number")

# def largest_name(names):
#     max = names[0]
#     for i in range(1,len(names)):
#         if(len(names[i])>len(max)):
#             max = names[i]
#     return max

# names = ["Rajesh Kumar","Rajesh","Ramesh","Raj"]
# print("The largest Name is: ",largest_name(names))

# def table(num):
#     for i in range(1,11):
#         print(num,"*",i,"=",num*i)

# num = int(input("Enter any Number for print their Table: "))
# table(num)

# a = 10
# while(a>=1):
#     print(a)
#     a-=1

list1 = ["apple","graps",'banana']
# a = "hellow welcom"
# [print(x) for x in list1]
# [print(x) for x in a]
# newList = []
# for x in list1:
#     if "a" in x:
#         newList.append(x)

# print(newList) 

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# newlist1 = [ x for x in list1 if "a" in x]
# print(newlist1)

# list2 = [x for x in range(10)]
# print(list2)

# fruits = ["apple","banana"]
# newlist1 = ["$" for x in fruits]
# print(newlist1)

# fruits1 = ["banan","apple",]
# newlist2 = [x if x!= "apple" else "orange" for x in fruits1]
# print(newlist2)

# name = ["Rohit","Yogesh","Antim"]

# name[1] = "ankit"
# print(name)
# newList3 = [x if x!="Antim" else "Mayank" for x in name]
# print(newList3)

# age = 26
# txt = "my name is John, and I am {}"
# print(txt.format(age))

# num = []
# for i in range(5):
#     val = int(input("Enter any number: "))
#     num.append(val)

# num.sort(key=None,reverse=True)
# print(num)

# print(num)
# num.pop(-2)
# print(tuple(num))
# num[1]=102
# print(tuple(num))
# num.sort()
# print(tuple(num))

# print("To check the prime number")
# res = 0
# num1 = int(input("Enter any number to check prime: "))
# if(num1==0 and num1==1):
#     res = 1

# for i in range (2,num1):
#     if(num1%i==0):
#         res=1
# if res ==1:
#     print(f"{num1} Number is not a Prime")
# else:
#     print(f"{num1} Number is  a Prime")

# while loop

# input1 = int(input("Enter any number: "))
# x1 = 1
# while(x1<=10):
#     print(x1*input1)
#     x1= x1+1
# x =10
# while(x>=1):
#     print(x*input)
#     x=x-1

