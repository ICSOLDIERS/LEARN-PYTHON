side1=float(input("enter the first side of triangle:"))         #6
side2=float(input("enter the second side of triangle:"))        #4
side3=float(input("enter the third  side of triangle:"))        #4
s=(side1+side2+side3)/2
area=(s*(s-side1)*(s-side2)*(s-side3))**0.5
print("area of triangle is :", area)       #7.937253933193772