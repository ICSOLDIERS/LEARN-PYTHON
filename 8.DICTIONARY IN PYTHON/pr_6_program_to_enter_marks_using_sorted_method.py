rec=dict()
num=int(input("enter number of students:"))
i=1
while i<=num:
    name=input("enter the name:")
    per=int(input("enter the percentage of student:"))
    rec[name]=per
    i+=1
    ls=rec.keys()
print("anme of the student","\t","marks%")    
for i in sorted(ls,key=rec.get):
    print("\t",i,"\t\t",rec[i])


