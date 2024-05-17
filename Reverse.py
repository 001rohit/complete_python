#2 write a program to reverse a  number 

num = 2345
temp = num
reverse = 0

while num !=0:
    remainder = num%10
    reverse = reverse * 10 + remainder
    num = num//10
print(reverse)
     