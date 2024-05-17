import math
# Sum function 
def sum():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sum1 = num1+num2
    print(f"{num1}+{num2} = {sum1}")

# Substract function 
def subt():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sub1 = num1-num2
    print(f"{num1}-{num2} = {sub1}")

# Multiplication function 
def multi():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    multi1 = num1*num2
    print(f"{num1}*{num2} = {multi1}")

#Devision Function
def devi():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    devi1 = num1/num2
    print(f"{num1}/{num2} = {devi1}")

#Mode Function
def mode():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    mode = num1%num2
    print(f"{num1}/{num2} = {mode}")

#Square Function
def square():
    num1 = int(input("Enter any number: "))
    square = num1*num1
    print(f"{num1}*{num1} = {square}")

#Qube Function
def qube():
    num1 = int(input("Enter any number: "))
    qube = num1*num1*num1
    print(f"{num1}*{num1}*{num1} = {qube}")

def Power():
    num1 = int(input("Enter any number: "))
    num2 = int(input("Enter any number: "))
    print(f"{num1}*{num1}*{num1} = {math.pow(num1,num2)}")


#Check odd and even number
def Check_Num():
    num1 = int(input("Enter any number: "))
    if(num1<0):
        print(f"{num1} is negative number")
    elif(num1%2==0):
        print(f"{num1} is a Even number")
    else:
        print(f"{num1} is a Odd number")

#Check Prime Function
def Check_Prime():
    num1 = int(input("Enter any number: "))
    count = 0
    for i in range(1,num1+1):
        if(num1%i==0):
             count += 1
    if(count==2):
        print(f"{num1} is prime number")
    else:
        print(f"{num1} is not prime number")

#Factorial Function
def Find_Factorial():
    num = int(input("Enter any number: "))
    fact = 1
    for i in range(2,num+1):
        fact*=i
    print(f"{num} number is factorial : {fact} ")     
    
#Parcentat function
def parcent():
    num1 = int(input("Enter number : "))
    num2 = int(input("Enter number (1-100): "))
    percent = num1*num2/100
    print(f"{num1} percent of {num2} : {percent} ")  
    
def calc_LCM():
    num1 = int(input("Enter any number: "))
    num2 = int(input("Enter any number: "))
    if(num1>num2):
        small = num2
    else:
        small=num1
    for i in range(1,small+1):
          if(num1%i==0) and (num2%i==0):
              hcf=i
    lcm = num1*num2/hcf
    print(lcm)

#Loop 
data=0
while data!=13:
    print("\n\n1 Add")
    print("2 Substraction") 
    print("3 Multiplication")
    print("4 Devision")
    print("5 Mod")
    print("6 Square")
    print("7 Qube")
    print("8 Power")
    print("9 Check_Your_Number")
    print("10 Check_prime")
    print("11 Factorial")
    print("12 Percentage")
    print("13 Find LCM")
    print("14 Close Program")
    

    data = int(input("Enter your choice: "))

    if data ==6:
        square()

    elif data ==7:
        qube()

    elif data ==9:
        Check_Num()

    elif data ==10:
        Check_Prime()
    
    elif data ==11:
        Find_Factorial()

    elif(data==1):
            sum()

    elif(data==2):
            subt()

    elif(data==3):
            multi()

    elif(data==4):
            devi()

    elif(data==5):
        mode()

    elif(data==8):
            Power()

    elif(data==12):
            parcent()

    elif(data==13):
            calc_LCM()

    elif(data>=14):
            break

print("Over this Program")
    
