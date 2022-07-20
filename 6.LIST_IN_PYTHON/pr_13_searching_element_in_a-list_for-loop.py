list=[14,12,18,19,13,17]
print("the list is :",list)
x=int(input("enter the number to find:"))
found=False
for i in range(len(list)):
    if list[i]==x:
        found=True
        print("%d found at %d position"%(x,i))
        break
if found==False:
    print("%d is not in list"%x)    