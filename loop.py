# for i in range (1,11):
#     if i==4:
#         break
#     else:
#         print(i)

# sum = 0
# for i in range (1,51):
#     if i%2==0:
#         sum+=i

# print("Ths sum of all the even number : ",sum)  

# for i in range (1,20):
#     print(i,i*i)

# w.a.p to find sum of first 10 odd number using while loop

# value = int(input("Enter the value of number: "))
# sum = 0 
# n = 0
# while n<=value:
#     if n%2!=0:
#             sum+=n  
#     n+=1
       
# print("The Sum of odd number: ",sum)

# for i in range (1,101):
#     if(i%8==0 and i%12==0):
#         print(i)

# while True:
#         name = input("Enter custormer's name: ")
#         total = 0
#         while True:
#                     print("Enter the amount and quantity")
#                     amount= float(input("enter amount: "))
#                     quantity = float(input("enter quantity: "))
#                     total +=amount*quantity
#                     repeat = input("do you want to add more items? (yes/no):  ")
#                     if (repeat =='no' or repeat=='No'):
#                                 break
                    
#         print("-"*40)  
#         print("Name: ",name)
#         print("Amount to be paid: ",total)
#         print("-"*40)
#         print("*********Happy Shopping************")

#         repeat1 = input("do you want to go to next customer? (yes/no): ")
#         if repeat1 =="no" or repeat1=="No":
#                         break
# print(" *Rohit_Kumre_ji* "*20)

           
a = "why fit in , when you are born to stand Out!"
# b = len(a)
# print(a.count("O"))

# b = a.upper()
# print(b)

# print(a.find("in"))
# print(a)
# print(a.title())

# for i in range (1,6):
    # for j in range (1, i+1):
        # print(j,end=" ")
        # print(i,end=" ")
       
        # print("*",end=" ")
    # print( )

for i in range (1,6):
    for j in range (6,i,-1):
        print(i,end=" ")
    print( )
                                   

