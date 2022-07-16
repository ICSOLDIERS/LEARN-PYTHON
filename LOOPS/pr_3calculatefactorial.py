from math import factorial


factorial=1
number=int(input("enter the number:"))
while number>1:
    factorial*=number
    number-=1
print("factorial of",number,"is:",factorial)    