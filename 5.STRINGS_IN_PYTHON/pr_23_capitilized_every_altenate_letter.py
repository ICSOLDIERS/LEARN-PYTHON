str=input("enter the string:")
lenght=len(str)
str2=""
for i in range(0,lenght):
    if i%2==0:
        str2+=str[i]
    else:
        str2+=str[i].upper()    
print(str2)        