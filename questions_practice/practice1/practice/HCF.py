def calc_hcf(x,y):
    if(x>y):
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if(x%i==0 and y%i==0):
            hcf=1

    return hcf
num1 = int(input("Eneter first number: "))
num2 = int(input("Eneter second number: "))
calc_hcf_res = calc_hcf(num1,num2)
print(calc_hcf_res)