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
7
def calc_lcm():
         num1 = int(input("Enter first number: "))
         num2 = int(input("Enter second number: "))
         if(num1>num2):
             small = num1
         else:
             small = num2
         for i in range(1,small+1):
             if(num1%i==0)and(num2%i==0):
                 hcf=i

         lcm = num1*num2/hcf
         print(f"{num1} and {num2}: {lcm}")
         

data=0
while data!=6:
    print("\n\n1 Add")
    print("2 Substraction") 
    print("3 Multiplication")
    print("4 Devision")
    print("5 LCM")
    print("6 Exit\n\n")
    data = int(input("Enter your choice: "))

    if(data==1):
        print("\n\tAddition\n")
        sum()

    elif(data==2):
        print("\n\tSubstraction\n")
        subt()

    elif(data==3):
        print("\n\tMultiplication\n")
        multi()

    elif(data==4):
        print("\n\tDevision\n")
        devi()
    
    elif(data==5):
        calc_lcm()

    elif(data>=6):
        break

print("Over this Program")
