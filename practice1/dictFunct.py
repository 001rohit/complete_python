name = ""
Email=""
mobile=0
Address = ""
myDict={
"Enter your Name":name,
"Enter your Email":Email,
"Enter your mobile":mobile,
"Enter your Address":Address,
}
def myProg():
    name = input("Enter your name: ")
    Email = input("Enter your Email: ")
    mobile = int(input("Enter your mobile: "))
    Address = input("Enter your Address: ")
    myDict["Enter your Name"]=name
    myDict["Enter your Email"]=Email
    myDict["Enter your mobile"]=mobile
    myDict["Enter your Address"]=Address

def printdict():
          if(len(myDict)>0):
              print()
              for keys,values in myDict.items():
                 print(keys,":",values)
                 print()
          else:
               print("Dictionary is empty")

def delate_data():
    # name = input("Enter your new name: ")
    # Email = input("Enter your new  Email: ")
    # mobile = int(input("Enter your new mobile: "))
    # Address = input("Enter your new Address: ")
  if(len(myDict)>0):
      del  myDict["Enter your Name"]
      del  myDict["Enter your Email"]
      del  myDict["Enter your mobile"]
      del  myDict["Enter your Address"]
  else:
       print("Dictionary is already empty")
    
# myProg()
# printdict()
choice = 0
while choice!=4:
        print("\n\n1 Enter Your New data")
        print("2 print data")
        print("3 delate data ")

        choice = int(input("Enter your choice: "))
        if(choice==1):
          myProg()
        elif(choice==2):
             printdict()
        elif(choice==3):
             delate_data()
        elif(choice==4):
              break
        