num=25 
if(num<=1):
    print("Give number is prime")
else:

    if(num%2==0):
        print("Give number is not prime")
    else:
        print("Give number is prime")

    
# def check_prime(num):
#      count = 0
#      for i in range(1,num+1):
#           if(num%i==0):
#             count+=1
#      if(count==2):
#        print("The give number is prime number")
#      else:
#          print("give number is not prime number")

# num1 = int(input("Enter any number: "))
# check_prime(num1)  

# num = int(input("Enter the number"))
# fact = 1
# for i in range(2,num+1):
#     fact*=i
# print(fact)