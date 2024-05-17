# print the largest number from a list of number
lst1 = [32,84,97,86,45,103,997]
largest = lst1[0]
for i in range(1,len(lst1)):
        if(lst1[i]>largest):
             largest = lst1[i]
print(largest)

# print the smallest number from a list of number
minValue = lst1[0]
for i in  range(1,len(lst1)):
       if(lst1[i]==minValue):
              minValue=lst1[i]

print(minValue)
 