1# W.A.P to take a input any alphabate and find vowel or consonant in this program 
array1 = ['a','e','i','o','u','A','E','I','O','U']
array2 = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','I','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
                  
input1 = input("Enter any character of alphabetic : ")

if input1 in array1:
     print("It is a vowel")
elif input1 in array2:
     print("It is  a consonant")
else:
     print("Please Enter valid charecter in alphabate")