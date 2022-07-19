str=input("enter the string:")
count=0
for i in str:
    if i.isspace() == False:
        count+=1
print("total  number of charecters is:",count)        
