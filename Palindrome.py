#3 write a program to take input a number to check number palindrome
num=-2
while (num!=-1):
    num = int(input("Enter The number: "))
    if (num==-1):
         break
    temp = num
    reverse = 0

    while num !=0:
        remainder = num%10
        reverse = reverse * 10 + remainder
        num = num//10
    print(reverse)
    if(reverse ==temp):
          print("This is a palindrom number")
    else:
        print("This is not a palindrome number")
     