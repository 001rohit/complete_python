# Write a Python program that concatenates all elements in a list into a string and returns it.
result=''
lst=[1,4,5,6]
for element in lst:
    result +=str(element)

print(result)