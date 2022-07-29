def power(x,n):
    result=1
    for i in range(n):
        result*=x
    return result    
a=int(input("enter the number:"))    
b=int(input("raise to the power:"))
pw=power(a,b)
print(a,"raise to the power",b,"is:",pw)