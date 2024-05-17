import random
import time
num = round(random.random()*100)
# x = time.sleep(1)
# print(x)

gauss =0
count = 0
while(gauss!=num):
   gauss=int(input("Enter the number: "))
   if(gauss>num):
      print("Your gauss is high")
   elif(gauss<num):
      print("your gauss is low")
      count+=1

print(f"You are guass number is right,You {count} time to attempt ")


   