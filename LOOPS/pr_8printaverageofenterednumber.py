counter=0
total=0
number=0
while number>=0:
    number=int(input("enter the positive number or a negative number to exit:"))
    total+=number
    counter+=1
avg=total/counter
print("the average of numbers is:",avg)
