# lst1 = [1,2,3,4,5]
# print(type(lst1))
# print(len(lst1))

# lst1[0]=12
# print(lst1) 

# lst1.append(15)
# print(lst1)

# lst1.reverse()
# print(lst1)

# lst1.sort()
# print(lst1)

# lst1.insert(2,"Hellow")
# print(lst1)

# lst1.pop()
# print(lst1)

# lst1.remove(2)
# print(lst1)

# lst = []
# intVal1 = int(input("Enter list length  : "))
# for i in range(1,intVal1+1):
#    lst.append(i) 

# print(lst) 

def table():
       a=1
       num=int(input("Enter any number: "))
       while(a<=10):
            print(f"{a} * {num} : ",a*num)
            a+=1

def find_square():
          num1=int(input("Enter start range number: "))
          num2=int(input("Enter end range number: "))
          while(num1<=num2):
                print() 
                print(f"{num1} * {num1} : ",num1*num1)
                num1+=1

def find_qube():
          num1=int(input("Enter start range number: "))
          num2=int(input("Enter end range number: "))
          while(num1<=num2):
            print()
            print(f"{num1} * {num1} * {num1} : ",num1*num1*num1)
            num1+=1

def prime():
          num1=int(input("Enter start range number: "))
          for i in range(1,num1+1):
                 if(num1%i==0):
                        print(num1)

choice = 0
while choice!=4:
      print("1 Table")
      print("2 find Square")
      print("3 find qube")
      print("4 find prime")
      print("5 Exit Program")
      choice = int(input("Enter number: "))

      if(choice==1):
            table()

      elif(choice==2):
           find_square()

      elif(choice==3):
           find_qube()    

      elif(choice>=4):
            prime()

      elif(choice>=5):
            break