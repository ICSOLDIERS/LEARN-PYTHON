total=0
count=0
while True:
    inp=input("enter a number: ")
    if inp=="done" :break
    value=float(inp)
    total+=value
    count+=1
avg=total/count    
print("average:",avg)
