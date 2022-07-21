compscience=dict()
print(type(compscience))
num=int(input("enter the number of student opted for python language:"))
i=1
while i<=num:
    name=input("enter the name:")
    grade=int(input("enter the grade:"))
    compscience[name]=grade
    i+=1
    ls=compscience.keys()
print("Computer science","\t","Name of student","\t","Grade")    
for i in sorted(ls,key=None,reverse=False):
    print("python","\t\t\t",i,"\t\t\t",compscience[i])

