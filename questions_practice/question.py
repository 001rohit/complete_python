
#1 take  name , age, address, contact ,input from user and make  dictionary of it and print the dictionary 

name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")
contact = int(input("Enter your contanct number: "))

myDict = {
   "name":name,
   "age":age,
   "address":address,
   "contact": contact,
}

print(myDict)

#2 
arr1 = [2,14,6,80]
arr2 = [1,31,5,17]
ans = []
for i in range(0,len(arr1)):
    ans.append(arr1[i])
    ans.append(arr2[i])

print(ans)

arr1.append(arr2)  
print(arr1)


#3 take  input of 3 number of list and print the table of each number

# for i in arr1,arr2:
#     arr1.append(arr2)  
#     print(i) 

# for i in arr1:
#     print(i)

list = []
for i in range(3):
            input2 = int(input("Enter the number: "))
            list.append(input2)
            
print(list)
print("Print table in list ")
for i in list:
        a = 1
        while(a<=10):
                    print(i,'*',a,"=",a*i)
                    print( )
                    a=a+1

#4 take 3 number input and print the sum of number

res = []
for i in range(3):
       value = int(input("Enter any number: "))
       res.append(value)
    
print(res)
sum = sum(res)
print(sum)    

#5 Take a number input and check the number is odd and Even

check = int(input("Enter any number: "))
if(check%2==0):
    print(f"{check} is an Even number")
else:
    print(f"{check} is an Odd number")

a = 10
b =21
c = 15

#6 Take 3 number  input and print the largest number among them

if(a>b and a>c):
    print(f"{a} is a greates number")
elif(b>a and b>c):
    print(f"{b} is a greates number")
elif(c>a and c>b):
    print(f"{c} is a greates number")
elif(a==b and b==c and a==c):
    print("all numbers are equall")



