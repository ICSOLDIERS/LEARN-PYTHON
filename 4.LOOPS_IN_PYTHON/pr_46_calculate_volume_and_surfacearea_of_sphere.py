from secrets import choice


radius=float(input("enter the radis of sphere: "))
print("1: calculate surface_area of sphere")
print("2: calculate volume of sphere")
choice=int(input("enter your choice(1 or 2) :"))
if choice==1:
    surface_area=4*3.14*radius*radius
    print("surface area of sphere is :",surface_area)
else:
    volume_of_sphere=(4/3*(3.14*radius*radius*radius))    
    print("volume of sphere is :",volume_of_sphere)