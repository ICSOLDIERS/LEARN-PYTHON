str=input("enter the string:")
alphabets=digits=special=0
for i in range(len(str)):
    if str[i].isalpha():
        alphabets+=1
    elif str[i].isdigit():
        digits+=1    
    else:
        special+=1    
print("\n total number of alphabet are:",alphabets)
print("\n total number of digits are:",digits)
print("\n total number of speacial charecters are:",special)

