# def check_prime():
#     num = int(input("Enter any number: "))
#     count=0
#     for i in range(1,num+1):
#         if(num%i==0):
#             count+=1
#     if(count==2):
#         print("Give number is prime")
#     else:
#         print("Give number is not prime")

# for i in range(5):
#     check_prime()

def  check__multiple(num):
    lst2 = []
    lst3=[]
    for i in range(1,num+1):
         if(i%3==0 and i%5!=0):
            lst2.append(i)
         elif(i%5==0 and i%3!=0):
            lst3.append(i)
    print(lst2)
    print(lst3)
# check__multiple(30)
check__multiple(100)

# def sum_lst(num):
#     sum1=0
#     for i in num:
#           sum1+=i
#     print(sum1)    
# lst1 = [1,2,3,4,5,6,7,8,9,10]
# sum_lst(lst1)
    