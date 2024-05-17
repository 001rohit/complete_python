# program - 1 
age = int(input("Enter your age: "))
if(age>=18):
    print("Yes you can vote")
else:
    print("You are minor")

# program - 2

day = input("Enter any  day: ")
if(day == "Monday"):
    print("1: You Enter  day : ",day)
elif(day=="Tuesday"):
    print("2: You Enter  day : ",day)
elif(day=="Wednasday"):
    print("3: You Enter  day : ",day)
elif(day=="Thursday"):
    print("4: You Enter  day : ",day)
elif(day=="Friday"):
    print("5: You Enter  day : ",day)
elif(day=="Saturday"):
    print("6: You Enter  day : ",day)
elif(day=="Sunday"):
    print("7:You Enter  day : ",day)
else:
    print(f"{day},Is not a valid day")

# program - 3
num = int(input("Please Select the number(1-7): "))
if(num==1):
    print(f" You select the number is {num} ,and the day is Monday")
elif(num==2):
    print(f" You select the number is {num} and the day is Tuesday")
elif(num==3):
    print(f"3: You select the number is {num} and the day is Wednasday")
elif(num==4):
    print(f"4: You select the number is {num} and the day is Thursday")
elif(num==5):
    print(f"5: You select the number is {num} and the day is Friday")
elif(num==6):
    print(f"6: You select the number is {num} and the day is Saturday")
elif(num==7):
    print(f"7:You select the number is  {num}and the day is Sunday")
else:
    print(f"{num},Is not a valid number")

# program - 4
num1 = int(input("Please Enter the number: "))
if(num1<=0):
    print(f"{num1} is not a valid number")
elif(num1%2==0):
    print(f"{num1} is Even number")
else:
    print(f"{num1} is  Odd number")

# w.a.p to accept the cost price of a bike and display the road tax to ba paid according to the following criteria:
tax = 0
principle = int(input("Enter the price of bike "))
if(principle>100000):
      tax = principle*15/100
elif(principle>50000):
      tax = principle*10/100
else:
      tax = principle*5/100

print(f"Only Tax to be paid for bike : {tax}")
print(f"The bike price with include tax: {principle+tax}")

# w.a.p to accept a number from 1 to 12 and display name of the month 

month = int(input("Enter the number (1 to 12): "))
if(month==1):
      print("January")
elif(month==2):
    print("Febrary")
elif(month==3):
    print("March")
elif(month==4):
    print("April")
elif(month==5):
    print("May")
elif(month==6):
    print("Jun")
elif(month==7):
    print("July")
elif(month==8):
    print("August")
elif(month==9):
    print("September")
elif(month==10):
    print("Octomber")
elif(month==11):
    print("November")
elif(month==12):
    print("December")
else:
     print("Please Enter valid number")

# Accept any city fromm the user and display monument of that city

city = input("Enter the name of State: ")
if(city=="Delhi"):
    print("Red For")
elif(city=="Agra"):
    print("Taj Mahal")
elif(city=="Jaipur"):
    print("Jal Mahal")
else:
    print("Not valid available State  :")

# w.a.p to find the lowest number out of two number excepted from user.
num1 = int(input("Enter the First number: "))
num2 = int(input("Enter the Second number: "))
if(num1>num2):
    print(f"{num2} is smaller number")
elif(num2>num1):
    print(f"{num1} is smaller number")
elif(num1==num2):
    print("Both number are equal")


# w.a.p to find the largest number out of two number excepted from user.
num1 = int(input("Enter the First number: "))
num2 = int(input("Enter the Second number: "))
if(num1>num2):
    print(f"{num1} is greater")
elif(num2>num1):
    print(f"{num2} is greater")
elif(num1==num2):
    print("Both number are equal")

# w.a.p to check whether a number (accepted from user) is positive or negative
num = int(input("Enter the number: "))
if(num>=0):
       print("This is a positive number")
else:
       print("This is a negative number")

# w.a.p to whether a number (accepted from user) is divisible by 2 and 3 both

num2 = int(input("Enter first number: "))
if(num2%2==0 and num2%3==0):
    print(f"{num2} is divisible by 2 and 3 both")
elif(num2%2==0 ):
    print(f"{num2} is divisible by 2 ")
elif(num2%3==0):
    print(f"{num2} is divisible by 3")
else:
    print(f"{num2} is not divisible by both")

# W.A.P to find the largest number out of three numbers excepted from user

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

if(n1>n2 and n1>n3):
    print(f"{n1} is greater number")
elif(n2>n3 and n2>n1):
    print(f"{n2} is greater number")
elif(n3>n1 and n3>n1):
    print(f"{n3} is greater number")
elif(n1==n2 and n2==n3 and n1==n3):
    print("All numbers are equals")


# Accept the age of 4 people and display the youngest one

store1 = []
for i in range(10):
      inputValue = int(input("Enter the ages of  peoplse: "))
      store1.append(inputValue)

print(store1)
minValue = min(store1)
print(f"{minValue} is a yongest person")
maxValue = max(store1)
print(f"{maxValue} is a oldest person")


# w.a.p to check whether a number is prime or not.

res = 0
num1 = int(input("Enter any number: "))
if(num1==0 and num1==1):
      res=1
for i in range(2,num1):
      if(num1%i==0):
            res=1
if res==1:
      print(f"{num1} Number is not prime")
else:
      print(f"{num1} number is prime")

# w.a.p to take inputs following from the user and calculate the percentage of class attended:

totalWorkingday = int(input("Total number of working days: "))
Student = int(input("Total number of days for absent: "))
per = (totalWorkingday-Student)/totalWorkingday*100
print("your attendece is: ",per)
if(per<75):
      print("You can not eligible for exams")
else:
     print("you are eligible for writing exam")

# w.a.p  company decided to give bonus to employee according to following 
servi = int(input("Enter the time period of service: "))
sal = int(input("Enter your salary: "))
res=0
if(servi>10):
    res = sal*10/100
elif(servi>=6 and servi<=10):
    res = sal*8/100
elif(servi<6):
     res = sal*5/100

print("Bonus is:  ",res)
print("Total Gross sallary is:  ",res+sal)

product1 = int(input("Enter The prodcut price: "))

rs = 0
if(product1>10000):
    res = product1*20/100
elif(product1>7000 and product1<=10000):
    res = product1*15/100
elif(product1<=7000):
    res = product1*10/100

# print(f"The product price is {product1} and  The discount is {res} ,and Net amount value is {product1-res}")

# method -1
sign = input("Enter any sign (+,-,*,/): ")
res1 = 0
if(sign=="+"):
      firstvalu = int(input("Enter the first num : "))
      secondvalu = int(input("Enter the second num : "))
      res1 = firstvalu+secondvalu
elif(sign=="-"):
      firstvalu = int(input("Enter the first num : "))
      secondvalu = int(input("Enter the second num : "))
      res1 = firstvalu-secondvalu
elif(sign=="*"):
      firstvalu = int(input("Enter the first num : "))
      secondvalu = int(input("Enter the second num : "))
      res1 = firstvalu*secondvalu
elif(sign=="/"):
      firstvalu = int(input("Enter the first num : "))
      secondvalu = int(input("Enter the second num : "))
      res1 = firstvalu/secondvalu
 
print("Your Answer is: ",res1)

# method -2
sign = input("Enter any sign (+,-,*,/): ")
firstvalu = int(input("Enter the first num : "))
secondvalu = int(input("Enter the second num : "))
if(sign=="+"):
         print(f"{firstvalu+secondvalu}")
elif(sign=="-"):
      print(f"{firstvalu-secondvalu}")
elif(sign=="*"):
      print(f"{firstvalu*secondvalu}")
elif(sign=="/"):
      print(f"{firstvalu/secondvalu}")

#w.a.p to check your electricity bill
ut = int(input("Enter number of units: "))
amount = 0
if(ut<=100):
    amount = 0
elif(ut>100 and ut<=300):
    amount = (ut-100)*2
else:
    amount = 400+(ut-300)*5

print("Total amount to pay is ",amount)

# w.a.p Accept the number of days from the user and calculate the charge for library according to following:

day = int(input("Enter the number of day: "))
res = 0
if(day<=5 and day>0):
    print("You pay the amount with late fee: ",day*2)
#     res = day*2
elif(day>=6 and day<=10):
    print("You pay the amount with late fee: ",day*3)
elif(day>=11 and day<=15):
        print("You pay the amount with late fee: ",day*4)
#     res = day*4
elif(day>15):
        print("You pay the amount with late fee: ",day*5)
#     res = day*5
else:
    print("Enter the valid day")

print("Your pay with late fee: ",res)

# w.a.p accept the killometers covered and calculate the bill according to the following  
# first 10km ->  Rs. 11/km
# next 90km -> Rs. 10/km
# After that -> Rs. 9/km

speed = int(input("Enter the spead: "))
if(speed<=10):
    print("cost of speed ",speed*11)
elif(speed>10 and speed<=100):
    print("cost of speed value: ",speed*10)
elif(speed>100 ):
    print("cost of speed value: ",speed*9)

for i in (2,3,4,5):
    print(i)
for i in range(5):
    print(i)

name = input("Enter you name: ")
print(name.upper())