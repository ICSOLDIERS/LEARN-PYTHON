list=[]
number=int(input("enter the number of elements in the list:"))
for i in range(1,number+1):
    value=int(input("enter element:"))
    list.append(value)
    list.sort()
print("sorted list is :",list)    
print("mid value is:",list[int(len(list)/2)])