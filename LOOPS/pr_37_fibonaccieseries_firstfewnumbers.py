number=int(input("enter the number upto you want fibonacci series:"))
num1=0;num2=1
print(num1,end=" ")
print(num2,end=" ")
for i in range(1,number):
    num3=num1+num2
    print(num3,end=" ")
    num1,num2=num2,num3
