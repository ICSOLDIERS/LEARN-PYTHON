line=input("enter the line:")
lower=upper=digit=0
for i in line:
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1        
    elif i.isdigit():
        digit+=1    
    else:
        pass    
print("total loweercase letters are:",lower)    
print("total uppercase letters are:",upper)    
print("total digits letters are:",digit)    
