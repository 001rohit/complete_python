# what is a difference between list,set,tuple
# list is an array to all value are store in one variable
#  multiple values are store to the difference index  in a list (values like number,string)   
lst = [2,3,4,5,6,"Hellow"]
print(lst)

# set
# set is a function  to decalare on one time and use to multiple time , apply different number 
def sum_num(num1,num2):
          return num1+num2

a = 20
b = 25
sum = sum_num(a,b)
print("Sum of Two number is : ",sum)

a1=35
b1 =45
sum1 = sum_num(a1,b1)
print("Sum of Two number is : ",sum1)

# Tuple 
# Tuple is a 
tpl=(1,2,3,4,5,6)
print(tpl) 
# find index
print(tpl.index(1))
tpl=(1,2,3,4,5,6,3,4,2)
#count method
print(tpl.count(3))

tpl1 = ("Rohit",)*6
print(tpl1)

