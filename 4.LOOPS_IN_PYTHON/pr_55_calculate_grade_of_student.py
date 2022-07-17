sub1=int(input("enter the first subject marks: "))
sub2=int(input("enter the second subject marks: "))
sub3=int(input("enter the third subject marks: "))
sub4=int(input("enter the fourth subject marks: "))
sub5=int(input("enter the fifth subject marks:"))
avg=(sub1+sub2+sub3+sub4+sub5)/5
if avg>=90:
    print("Grade: A")
elif avg>=80 and avg<90:
    print("Grade: B")    
elif avg>=70 and avg<80:
    print("Grade: C")
elif avg>=60 and avg<70:
    print("Grade: D")
else:
    print("Grade: F")    