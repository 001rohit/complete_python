# print("hellow python")

# value = input("Enter the any single alphabetic letter:- ")
# valu1 = ['a','e','i','o','u','A','E','I','O','U']

# if value in valu1:
#     print(value,",It is a vowel")

# elif (value=='A' or value=='E' or value=='I' or value=='O' or value=='U' ):
#     print(value,"It is a vowel")
# else:
#     print(value,",It is a consonent")
    
# input1 = input("Enter the any number:-")
#2 palindrome
#3 rever number
num = -1
while(num != -1):
    num = int(input("Please Enter any number  :  "))
    if(num==-1):
        break
    temp = num
    reverse = 0
    while num != 0 :
        rem = num % 10
        reverse =  reverse * 10  + rem
        num = num // 10    
    
    print(reverse)
    if(reverse==temp):
        print("The number is palindrome")
    else: 
        print("The number is not palindrome")   