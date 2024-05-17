# list in python 

# w.a.p to take input  5  a number and  print  the of list number  

# input = int(input("Enter the value: "))

inputs = []

for i in range(5):
    inp = int(input("Enter the value of Number: "))
    inputs.append(inp)

print("Elements of List:  ",inputs)

Sum = 0

for i in range(0,len(inputs)):
    Sum = Sum+inputs[i]
print("The Sum number of sum in list : ",Sum)




# input1 = int(input("Enter the value of number: "))
# input2 = int(input("Enter the value of number: "))
# input3 = int(input("Enter the value of number: "))
# input4 = int(input("Enter the value of number: "))
# input5 = int(input("Enter the value of number: "))
# lst = []

# lst.append(input1)
# lst.append(input1)
# lst.append(input2)
# lst.append(input3)
# lst.append(input4)
# lst.append(input5)
# print(lst)

# for i in range(0,len(lst)+1):
#     print(i)

# total = 0
# for i in  range (0,len(lst)):
#     total = total+lst[i]

# print("sum of all elements in given list, ",total)

# print("hellow")

# inputs = []
# for i in range(5):
#     value = int(input("Enter the number: "))
#     inputs.append(value)
# # print(inputs)
#     total = 0
# for i in range(0,len(inputs)):
#     total = total+inputs[i]
# print(total)
# total = sum(inputs)
# print(total)