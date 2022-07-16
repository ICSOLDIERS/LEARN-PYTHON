count_emp=0
while count_emp<3:
    hours=int(input("enter hours:"))
    rate=float(input("enter rater:"))
    pay=hours*rate
    print("pay is :",pay)
    count_emp+=1
print("all employees passed")    