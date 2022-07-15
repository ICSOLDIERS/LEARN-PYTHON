x=y=0
x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
if (x>y):
    x,y=y,x     #interchange
    print("the largest number is :",y)
    print("the smallest number is :",x)
else:
    print("the largest number is:",y)    
    print("the smallest number is:",x)    
