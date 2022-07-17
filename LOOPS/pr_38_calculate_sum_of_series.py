num=int(input("enter the number:"))
n=int(input("enter the limit:"))
sum=0
for i in range(1,n+1):
    r=num*i
    sum+=r
    print(r,'+',end=" ")
    print("sum of series is:", sum)

