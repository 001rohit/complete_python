lst=[]
input1 = int(input("Enter any number: "))
for i in range(1,input1+1):
    val = int(input("Enter value: "))
    if(val%2==0):
             lst.append(val)

print(lst)