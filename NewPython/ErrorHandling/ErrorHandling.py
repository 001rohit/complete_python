# exception  = events detected during excution that interrupt the flow of a prgoram

try:
    numerator = int(input("Enter first number: "))
    denomenator = int(input("Enter second number: "))

    result = numerator/denomenator

except ZeroDivisionError as e :
    print(e)
    print("you can not divide by zero")

except ValueError as e:
    print(e)
    print("Enter only number plz")

except Exception as e:
    print(e)
    print("something went wrong :(")

else:
    print(result)

print("You program is working")

     