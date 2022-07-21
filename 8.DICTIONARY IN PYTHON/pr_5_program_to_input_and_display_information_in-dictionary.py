rec=dict()
num=int(input("enter number of students:"))
i=1
while i<=num:
    name=input("enter the name:")
    per=int(input("enter the percentage of student:"))
    rec[name]=per
    i+=1
print("anme of the student","\t","marks%")    
for i in rec:
    print("\t",i,"\t\t",rec[i])


