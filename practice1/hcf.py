def calcu_lcm(x,y):
    if(x>y):
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if(x%i==0)and(y%i==0):
            hcf=i
    
    lcm=x*y/hcf
    return lcm

print(calcu_lcm(20,24))

