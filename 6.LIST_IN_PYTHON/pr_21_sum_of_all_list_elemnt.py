list=[]
number=int(input("enter total number of elements in list:"))
for i in  range(1,number+1):
    value=int(input("enter element:"))
    list.append(value)
    print(list)
sum=0
for item in list:
    sum+=item    
print("sum of all elements in list is:",sum)    