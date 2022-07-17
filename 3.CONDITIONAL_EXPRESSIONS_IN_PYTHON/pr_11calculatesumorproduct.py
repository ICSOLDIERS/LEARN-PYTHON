num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
print('1: calculate sum:')
print("2: calculate product: ")
choice=input("enter your choice(1 or 2): ")
if (choice =="1"):
    sum=num1+num2+num3
    print("the sum of",num1,',',num2,',',num3,"is:",sum)
else:
    product=num1*num2*num3    
    print("the product of",num1,',',num2,',',num3,"is:",product)

