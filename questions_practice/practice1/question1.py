# list
lst = [1,2,3,4,5,"Hellow",True]
print(lst)
print(len(lst))

# tuple
tpl = (1,2,3,4,5,"Welcome",True)
print(tpl)
for i in tpl:
    print(i)
# count
print(tpl.count(2))
#find index
print(tpl.index("Welcome"))
# remove
print(tpl)
listConvert = list(tpl)
print(listConvert)
lastElement = listConvert.pop(-1)
listConvert.append("Rohit")
print(listConvert)
print(lastElement)

tplConvert = tuple(listConvert)
print(tplConvert)

# set

def find_largest(num):
    larg = num[0]
    for i in range( 0,len(num)):
             if(num[i]>larg):
                   larg = num[i]
    print(larg)
lst = [2,3,4,5,6,7]
find_largest(lst)


def find_smallest(num):
    larg = num[0]
    for i in range( 0,len(num)):
             if(num[i]==larg):
                   larg = num[i]
    print(larg)
lst2 = [2,3,4,5,6,7]
find_smallest(lst2)


# loop:- # Take a list of 10 item input and print the list using loop
lst1 =[] 
input1 = int(input("Enter any number: "))
for i in range(0,input1):
      inputVal = int(input("Enter any number: "))
      lst1.append(inputVal)
print(lst1)       

# simple reverse loop 
for i in range(10,0-1,-1):
      print(i)

a = 10
while(a>0):
      print(a)
      a-=1

# a = 0
# while(a<=10):
#       print(a)
#       a+=1


lst = []
val = int(input("Enter any number: "))
sum1 = 0
for i in range(1,val+1):
      lst.append(i)
      
print(lst)
for i in lst:
      sum1=sum1+i
print(sum1)

# find Factorial
multi=1
for i in lst:
      multi*=i
print(multi)







