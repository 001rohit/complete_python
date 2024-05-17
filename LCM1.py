# def LCM(num1,num2):
#             if(num1>num2):
#                   hcf = num1
#             else:
#                   hcf=num2
#             if(hcf%num1==0) and (hcf%num2==0):
#                      lcm = num1*num2/hcf  
#                      print(lcm)

# LCM(12,13)

# num1 = 12
# num2=14
# LCM(num1,num2)

# def LCM(num1,num2):
#     if(num1>num2):
#         greater=num2
#     else:
#         greater=num2
#     while(True): 
#        if(greater%num1==0) and (greater%num2==0):
#         lcm=greater
#         break
#        greater+=1
#     return lcm

# num1 = 12
# num2 = 13
# res =LCM(num1,num2)
# print(res)

def calc_LCM():
    intVal1 = int(input("Enter first number: "))
    intVal2 = int(input("Enter second number: "))

    if(intVal1>intVal2):
         small=intVal2

    else:
           small=intVal1

    for i in range(1,small+1):
           if(intVal1%i==0) and (intVal2%i==0):
                 hcf=i
                
    lcm = intVal1 * intVal2/hcf
    print(lcm)


choice = 0
while choice!=2:
      print("Find lcm")
      choice = int(input("Enter your choice: "))

      if(choice==1):
            calc_LCM()

      elif(choice==2):
            break


