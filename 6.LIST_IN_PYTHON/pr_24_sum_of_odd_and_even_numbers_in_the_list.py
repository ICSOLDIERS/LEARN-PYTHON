list=[]
sum_odd=0
sum_even=0
number=int(input("enter the number of elements in the list:"))
for i in range(1,number+1):
    value=int(input("enter elements:"))
    list.append(value)
for j in range(number):
    if list[j]%2==0:
        sum_even=sum_even+list[j]
    else:
        sum_odd=sum_odd+list[j]        
print("\n the sum of all even number in the list is :",sum_even)        
print("\n the sum of all odd number in the list is :",sum_odd)        

