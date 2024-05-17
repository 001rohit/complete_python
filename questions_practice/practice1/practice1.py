# find prime number
# num=23
# count = 0
# for i in range(1,num+1):
#     if(num%i==0):
#          count+=1
# if(count==2):
#         print("Given number is prime")
# else:
#         print("Give number is not prime")

# lst = [1,2,3,4,5,6,7,8,9,10]
# lst1=[]
# for i in range(0,len(lst)):
#       if(lst[i]%2==0):
#             lst1.append(lst[i])
# print(lst1)
        
# lst2 = []
# for i in range(5):
#     input1 = int(input("Enter any number: "))
#     lst2.append(input1)

# print(lst2)
# sum = 0
# for i in lst2:
#     sum+=i
# print(sum)

# fact = 1
# for i in lst2:
#     fact*=i
# print(fact)

# find max number in lst
# numlst = [1,2,3,4,5,6,7,8]
# max = numlst[0]
# for i in range(0,len(numlst)):
#     if(numlst[i]>max):
#         max=numlst[i]

# print(max)

def find_devisible_num(num):
        lst1 = []
        lst2=[]
        for i in range(1,num+1):
           if(i%3==0 and i%5!=0):
                lst1.append(i)
           if(i%5==0 and i%3!=0):
               lst2.append(i)
        
        print(lst1)
        print(lst2)

numlst1 = 100
find_devisible_num(numlst1)
