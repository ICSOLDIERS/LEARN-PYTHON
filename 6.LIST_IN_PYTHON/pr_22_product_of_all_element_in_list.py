from math import prod
from numpy import product


list=[]
number=int(input("enter the number of elements in the list:"))
for i in range(1,number+1):
    value=int(input("enter element:"))
    list.append(value)
    print(list)
product=1
for item in list:
    product*=item    
print("the product of all elemnt in the list is :",product)    
