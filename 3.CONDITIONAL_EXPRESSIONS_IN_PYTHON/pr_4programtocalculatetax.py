name=input("enter the name:" )
salary=float(input("enter the salary :"))
if salary>5000:
    tax=0.10*salary
    netsalary=salary-tax
    print("the net salary of",name,"is:",netsalary)
else:
    netsalary=salary    
    print("no taxable ammount")
    print("the total salary of",name,"is:",netsalary)