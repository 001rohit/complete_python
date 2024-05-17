# import datetime
# import calendar
# now = datetime.datetime.now()
# print(now.strftime("%y-%m-%d %H : %M:%S"))
# y=int(input("Input the year: "))
# m=int(input("Input the month: "))

# print(calendar.month(y,m))

# def sum_thrice(x,y,z):
#     sum = x+y+z

#     if (x==y==z):
#         sum = sum*3

#     return sum

# print(sum_thrice(1,1,3))
# print(sum_thrice(1,1,1))

# def sum_thrice(x,y,z):
#     sum = x+y+z

#     if (x==y==z):
#         sum = sum/3

#     return sum

# print(sum_thrice(1,1,3))
# print(sum_thrice(50,50,50))

# count method

# lst = [1,2,3,4,5,4,4,4,4,4]
# count = 0 
# for num in lst:
#        if(num==3):
#            count+=1
# print(count)

# def is_vowel(char):
#     all_vowels = 'aeiou'

#     return char in all_vowels

# print(is_vowel('o'))

# match

# def is_group_memebr(lst1,num):
#    for value in lst1:
#       if(num==value):
#         return True
    
#    return False

# print(is_group_memebr([1,2,3,4,5,6,121,34,5,334,7,8],121))
# num=5
# lst1 = [1,2,3,4,5,6,7]

# def  histrogram(items):
#       for n in items:
#             output = ''
#             times = n

#             while times>0:
#                   output+="*"
#                   times-=1
#             print(output)

# histrogram([4,5,6,7])

# lst = [24,26,1,2,3,4,5,6]
# for i in lst:
#     if(i%2==0):
#         if(i==24 or i==2 or i==4):
#             continue
#         print(i)