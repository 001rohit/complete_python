# Take input of 10 number in an list and sort descending order
# list = []
# for i in range (10):
#      input1 = int(input("Enter the number: "))
#      list.append(input1)
    
# list.sort(key = None,reverse=True)
# print(list)
     

# take 5 number input in an tuple by user and perform the following operation
#1 change the value of inpute 2 of tuple (using index)
#2 sort the tuple in ascending order and print tuple
#3 delete the 2 last element of tuble

list1 = []
for i in range (5):
        value = int(input("Enter for any number: "))
        list1.append(value)  

print("To the list value of elements")
print(list1)

#1 change the value of inpute 2 of tuple (using index)
print("change the value index  2 in tuple")
list1[2] = 100
print(tuple(list1))

#2 sort the tuple in ascending order and print tuple
print("tuple in sort form")
list1.sort()
print(tuple(list1))

#3 delete the 2 last element of tuble
print("delete the value second last index  2 to tuple")

list1.pop(-2)
print(tuple(list1))

# Take a number input and check a number is prime or not ?
print("to check the prime number")
res = 0
num1 = int(input("Enter any number: "))
if(num1==0 and num1==1):
      res=1
for i in range(2,num1):
      if(num1%i==0):
            res=1
if res==1:
      print(f"{num1} Number is not prime")
else:
      print(f"{num1} number is prime")