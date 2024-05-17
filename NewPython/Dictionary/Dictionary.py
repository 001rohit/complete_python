# dictionary  = a changeable , unordered collection of unique key:value pairs fast because they use hashinng, allow us to access a value quickly

capiltal  = {
    "USA":"Washington DC",
    "India":"New Delhi",
    "China":"Bejing",
    "Russia":"Mascow"
}
# print(capiltal["USA"])

# key = capiltal.keys()
# for i in key:
#     print(i)


# value = capiltal.values()
# for i in value:
#     print(i)
del capiltal["USA"] 
capiltal["Sir lanka"] = "colombo"
capiltal["Sir lanka"] = "Sri Jayawardenepura Kotte"
for k,v in capiltal.items():
    print(k,":",v)

