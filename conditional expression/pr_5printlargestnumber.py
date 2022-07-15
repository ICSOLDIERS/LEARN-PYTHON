num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
max=num1
if num2>num1:
    max=num2
if num3>max:
    max=num3    
print("the gretest number is:",max)    