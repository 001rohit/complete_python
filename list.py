
list = [3,4,5,6,2]
print(list)

# to add the element in the list 
list.append(24)
print(list)

# to remove the element in the list
list.pop()
print(list)

# to sort the element in the list
list.sort()
print(list)

# to add all the number in list of array
sum1 = sum(list)
print(sum1)

print(type(list))

print(len(list))

print(list[0])
print(list[1])

print(list[1:3])

list1 = []
for i in range(5):
        addValue = int(input("Enter Any number: "))
        list1.append(addValue)

print(list1)

sum = 0
for i in range (0,len(list1)):
        sum = sum+list1[i]

print("Total number of sum is : ",sum)