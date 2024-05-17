# for j in range(4):    
#     for i in range(5):
#         print("*",end=" ")
#     print()

for j in range(4):    
    for i in range(j+1):
        print("*",end=" ")
    print()

for j in range(4,0,-1):    
    for i in range(j):
        print("*",end=" ")
    print()


for j in range(4):    
    for i in range(4-j):
        print("*",end=" ")
    print()