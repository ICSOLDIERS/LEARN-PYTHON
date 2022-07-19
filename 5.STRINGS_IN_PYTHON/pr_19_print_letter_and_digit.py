s=input("enter the string:")
d=l=0
for c in s:
    if c.isdigit():
        d+=1
    elif c.isalpha():
        l+=1
    else:
        pass    
print("no of letters is:",l)    
print("no of digit is :",d)
