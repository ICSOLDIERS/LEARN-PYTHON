radius=float(input("enter the radius of a circle:"))
print("1: calculate area of a circle" )
print("2: calculate perimeter of circle")
choice=int(input("enter  your choice(1 or 2) :"))
if (choice==1):
    area_of_circle=3.14*radius*radius
    print("area of circle is :",area_of_circle)
else:
    perimeter_of_circle=2*3.14*radius    
    print("perimeter of circle is :",perimeter_of_circle)