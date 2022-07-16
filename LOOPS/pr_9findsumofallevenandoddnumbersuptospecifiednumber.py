num=int(input("enter the number:"))
count=1
sum_even=sum_odd=0
while count<=num:
    if (count%2)==0:
        sum_even+=count
    else:
        sum_odd+=count    
    count+=1    
print("sum of all even number upto",num,"is:",sum_even)    
print("sum of all odd number upto",num,"is:",sum_odd)    
