name=""
bankName=""
Accoun_Type=""
Bank_branch=""
Account_No=0
mobile_No=0
Email_id=""
useDict={
    "Name of customer":name,
    "Name of Bank ": bankName,
    "Account Type":Accoun_Type,
    "Branch of Bank":Bank_branch,
    "Account No.": Account_No,
    "Mobile No.":mobile_No,
    "Email address":Email_id
}
def Open_Account():
    useDict["Name of customer"]=input("Enter your name: ")
    useDict["Name of Bank"]=input("Enter you Bank Name: ")
    useDict["Account Type"]=input("Enter you Account type: ")
    useDict["Branch of Bank"]=input("Enter your branch address: ")
    useDict["Account No."]=int(input("Enter your Account Number: "))
    useDict["Mobile No."] = int(input("Enter you mobile Number: "))
    useDict["Email address"]=input("Enter your Email address: ")

def PrintUseDatail():
     for keys , values in useDict.items():
        print(keys," : ",values)

Open_Account()
PrintUseDatail()








# useDict[name]=input("Enter your name: ")
# useDict[bankName]=input("Enter you Bank Name: ")
# useDict[Accoun_Type]=input("Enter you Account type: ")
# useDict[Bank_branch]=input("Enter your branch address: ")
# useDict[Account_No]=int("Enter your Account Number: ")
# useDict[mobile_No] = int("Enter you mobile Number: ")
# useDict[Email_id]=input("Enter your Email address: ")
# for keys , values in useDict.items():
#     print(keys,values)