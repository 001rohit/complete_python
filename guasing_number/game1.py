print("Welcome to my Guessing number game")
import random
import time
num = round(random.random()*100)

guess = 0
count = 0

while(guess != num):
    guess = int(input("Enter Your Number : "))
    if(guess>num):
        print("Your guess is higher")
    elif(guess<num):
        print("Your guess is lower")
    
    count += 1

print(f"You guessed it right in {count} Attempts")