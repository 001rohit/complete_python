
# for loop
# for var_name in range (starting ,ending+1,step):
# code to execute

# print number 1 to 10 
# for i in range (1,11):
#       print(i)

# # print number 1 to -100
# for i in range (1,-101,-1):
#       print(i)


# for i in range (1,11):
#       print(i)


# while loop
# x= 0
# input1 = int(input("Enter the any number: "))
# while(x>=-10):
#         print(x)
#         x= x-1

#2 take a number inpute from the user and print 0 to that number
# x=0
# input2= int(input("Enter any number: "))
# while(x<input2):
#         x = x+1
      
#1 take a number from the user and print  the table from the input number
# method .1 
# input3 = int(input("Enter the any number: "))
# for i  in range(1,11 ):
#         print(f" {input3} * {i} = ",input3*i)   

#method .2
# num =1
# while(num>0):
#                 num =int(input("Enter the any number: "))
#                 if(num<=0):
#                           break
#                 count = 1
#                 print("Here is your Table !!!")
#                 while count<=10:
#                         num = num *1
#                         print(num,'x',count,'=',num*count)
#                         count +=1
      

#2 w.r.p which take 10 number input and print the sum of 10 number
# sum = 0
# for  i in range(1,11,1):
#         input1 = int(input(f"Enter the value of number { i }: "))
#         sum = sum+input1
# print("sum of 10 number is: ",sum)      


#1 w.r.p take a string input and check whether it containers all the 26 characters or not

input1 = input("Enter any paragraph: ")
character = ['a','A','b','B','c','C','d','D','e','E','f','F','g','H','i','I','j','k','K','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','Y','z','Z']

if input1 in character:
        print(input1," It is a 26 character of alphabate for in this paragraph")
else:
        print(input1," It is not a 26 character of alphabate for in this paragraph")