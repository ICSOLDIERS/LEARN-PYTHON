principal=int(input("enter the principal ammount: "))
rate=float(input("enter the rate of interest: "))
time=int(input("enter the time: "))
for i in range(1,time+1):
    interest=(principal*rate)/100
    principal=principal+interest
    print("after",i,"year","interest= ",interest,"ammount= ",principal)

