details=dict()
num=int(input("enter the number of the students whose information you want to save:"))
i=1
while i<=num:
    name=input("enter the name of the student:")
    rno=int(input("ente the roll number of the student :"))
    details[name]=rno
    i+=1
name=input("enter the name of the student you wnat to delete :")    
del details[name]
ls=details.keys()
print("student information after deletion:")
print("Name of student","\t","R.No")
for i in ls:
    print("\t",i,"\t\t",details[i])