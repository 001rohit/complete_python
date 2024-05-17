#1 write a function that tkaes input a list and print the sum of list number
def sumList(num):
    sum = 0
    for i in range(0,len(num)):
          sum = sum+lst[i]
    print(sum)

lst = [1,2,3,4,5]
sumList(lst)
          
#2 wirte a function that take a number and check the number is  even or not          
def Check_num(num):
     if(num%2==0):
        print(f"{num} is a Even number")
     else:
           print("This is Odd number")
           
Check_num(24)

#3 write a function that take a number and tell the number is prime or not
def check_prime(num):
     count = 0
     for i in range(1,num+1):
          if(num%i==0):
            count+=1
     if(count==2):
       print("The give number is prime number")
     else:
         print("give number is not prime number")

num1 = int(input("Enter any number: "))
check_prime(num1)  

# find the largest number in list

def findLargest(num):
    largest = num[0]
    for i in range(1,len(num)):
        if(num[i]>largest):
            largest = num[i]

    return largest 

lst1 = [12,33,54,96,56,78]
res = findLargest(lst1)
print(res)   