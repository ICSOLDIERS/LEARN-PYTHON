print("1: calculate area of square:")
print("2: calculate area of rectangle:")
choice=int(input("enter your choice 1 or 2:"))
if choice==1:
    side=float(input("enter the side of square:"))
    area_square=side*side
    print("area of square is:",area_square)
else:
    lenght=float(input("enter the leght of rectangle:"))    
    breadth=float(input("enter the breadth of rectangle:"))
    area_rectangle=lenght*breadth
    print("area of rectangle is :", area_rectangle)