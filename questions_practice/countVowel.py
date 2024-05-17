# str = input("Enter string as you wish: ")
# vowels = 0
# consonent = 0
# for i in str:
#     if(i=='a'or i=='e' or i =='i' or i=='o' or i=='u'):
#         vowels +=1
#     elif i !=' ':
#        consonent+=1   

# print("The number of vowels: ",vowels)
# print("The number of consonent: ",consonent)

str = ' rohit kumre'
vol = 'aeiou'
vol1 =0
const=0
for i in vol:
    for j in str:
        if(i==j):
            vol1+=1

print(vol1)