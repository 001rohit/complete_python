import time
for i in range(0,100+1):
    print(i)

intVal = int(input("spacified size in loop: "))
for i in range(0,intVal+1):
    print(i)

intVal = int(input("spacified size in loop: "))
for i in range(1,intVal+1):
   if(i%2==0):
      if(i!=16 and i!=20):
          print(i)

intVal = int(input("spacified size in loop: "))
for i in range(1,intVal+1):
    time.sleep(1)
    if(i%2!=0):
        print("This is odd number",i)
    elif(i%2==0):
      print("This is even number",i)

lst = [1,2,3,4,5,6]
for i in lst:
    print(i)

lst = [1,2,3,4,5,6]
for i in range(0,len(lst)):
    print(i,lst[i])

lst = [1,2,3,4,5,6]
for i in range(0,len(lst)):
    if(lst[i]%2!=0):
        print(lst[i])


lst = []
intVal1 = int(input("Enter the size: "))
for i in range(1,intVal1+1):
   val = int(input("Enter the number: "))
   lst.append(val)
print(lst)

removeVal = int(input("Enter the value: "))
remove = lst.remove(removeVal)
print(lst)

# insert Value in list
indexVal = int(input("Enter index value: "))
Value = int(input("Enter  value: "))
InsertVal = lst.insert(indexVal,Value)
print(lst)

# remove value for lst index in list
lst.pop()
print(lst)

# count the value in list
countVal = int(input("Enter The value of any one element to the list: "))
countValOf = lst.count(countVal)
print("Reapet same element in list ",countValOf,"times")

elementVal = int(input("Enter any one element to the list: "))
elementValue =lst.index(elementVal)
print("Index value is: ",elementValue)

mydict = {
   "name":"Rohit",
   "gender":"male",
   "age":26,
   "address":"Kolar Road"
}
for i in mydict:
   print(i,":",mydict[i])

for key,value in mydict.items():
   print(key,":",value)

# delete any value with help to key
del mydict["address"]
print(mydict)

# new key add
mydict["hobby"] = "traveling"
print(mydict)
 
# change value with help to key
mydict["hobby"] = "reading"
print(mydict)

