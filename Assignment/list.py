lst = []

def find_small(num):
    small = num[0]
    for i in range(1,len(num)):
        if(num[i]==small):
            small = num[i]
    print(small)

def find_largest(num):
    largest = num[0]
    for i in range(1,len(num)):
        if(num[i]>largest):
            largest = num[i]
    print(largest)
         
def remove_lastElement(num):
       if(len(num)>0):
            num.pop()
            print(num)

def Add_Element(num):
    for i in range(1,len(num)+1):
        input1 = int(input("Enter any number: "))
        lst.append(input1)
    print(lst)

lst1 = [1,2,3,4,5,6,7,8,9]
# Add_Element(lst1)
# find_small(lst1)
# find_largest(lst1)
remove_lastElement(lst1)