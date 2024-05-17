#Add item in list
lst1=[]
def Append():
    num=int(input("Enter any one number: "))
    for i in range(1,num+1):
       input1 = int(input("Enter number: "))
       lst1.append(input1)
    
#Print the list    
def Print1():
     print(lst1)

#remove the item in list
def Pop():
        lst1.pop(-1)

#insert item in list
def insert():
     index = int(input("Enter number: "))
     data = int(input("Enter data: "))
     lst1.insert(index,data)

#remove any item in list
def remove():
     index = int(input("Enter any index number: "))
     if(len(lst1)>0):
         lst1.pop(index)

 # Clear all item in list           
def Clear():
     lst1.clear()

#check the size of list
def listSize():
     print(len(lst1))

#check list  empty or not 
def Check_list():
     if(len(lst1)==0):
        print("List is Empty")
     else:
         print("List is not Empty")

def reverse():
     lst1.sort(key=None,reverse=True)
     print(lst1)

# Append()
# Pop(lst1)
# insert(lst1)
# remove(lst1)
# Print1(lst1)
# Clear(lst1)
# Print1(lst1)
# listSize(lst1)
# Check_list(lst1)   
# reverse(lst1)

choice=0
while choice!=10:
     print("1 Add item in list")
     print("2 Print the list")
     print("3 Remove the item in list for last element")
     print("4 Remove any item in list")
     print("5 Check the size of list")
     print("6  Clear all item in list ")
     print("7 check item in list empty or not")
     print("8 Insert data at give index")
     print("9 Print list to Reverse ")
     print("10 Exit program")
    #  lst1=[]
     
     choice = int(input("Enter your choice: "))
     if(choice==1):
          Append()
     elif(choice==2):
        Print1()
     elif(choice==3):
        Pop()
     elif(choice==4):
        remove()
     elif(choice==5):
        listSize()
     elif(choice==6):
        Clear()
     elif(choice==7):
        Check_list()
     elif(choice==8):
        insert()
     elif(choice==9):
         reverse()
     elif(choice >=10):
         break
     
print("Over your program")