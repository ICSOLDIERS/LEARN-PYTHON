items=[2,8,9,12,17]
print("list of items is: ",items)
x=int(input("enter the number to find:"))
i=flag=0
while i<len(items):
    if items[i]==x:
        flag=1
        break
    i+=1
if flag==1:
    print(x,"found at position",i)    
else:
    print(x,"is not in list")    
