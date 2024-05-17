# code reusablity
# eassy to debuge
# principle - dry(Do not repeat youself

# def find_devision(num):
#     lst1 = []
#     for i in range(1,num+1):
#         if(num%i==0):
#           lst1.append(i)
#     print(f"The divisor of {num} are {lst1}")
    
# num = 20
# find_devision(num)

# num = 25
# find_devision(num)

# num = 36
# find_devision(num)

def find_devision():
    num = int(input("Enter any number: "))
    lst1 = []
    for i in range(1,num+1):
        if(num%i==0):
          lst1.append(i)
    print(f"The divisor of {num} are {lst1}")
    
for i in range(10):
    find_devision()

# data = ""
# while data!="Stop":
#     data = input("Enter your choice: ")
#     if(data=="Stop"):
#         break
#     else:
#         find_devision()
