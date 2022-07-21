compscience=dict()
num=int(input("enter the number of student opted for python language:"))
i=1
while i<=num:
    name=input("enter the name:")
    grade=int(input("enter the grade:"))
    compscience[name]=grade
    i+=1
print("Computer science","\t","Name of student","\t","Grade")    
for i in compscience:
    print("python","\t\t\t",i,"\t\t\t",compscience[i])

