numlist=[]
while True:
    inp=input("enter a number:")
    if inp=="done":break
    value=float(inp)
    numlist.append(value)
avg=sum(numlist)/len(numlist)    
print("average:",avg)
