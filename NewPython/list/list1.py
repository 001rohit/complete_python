n = 3
lst1 = []
lst2 = []
lst3 = []
for i in range(0,3+1):
    inpt1 = input("Enter you favorit movie: ")
    lst1.append(inpt1)

for i in range(0,3+1):
    inpt1 = input("Enter you favorit country: ")
    lst2.append(inpt1)

for i in range(0,3+1):
    inpt1 = input("Enter you favorit park ")
    lst3.append(inpt1)

manList = [lst1,lst2,lst3]
print(manList)
print(manList[0])