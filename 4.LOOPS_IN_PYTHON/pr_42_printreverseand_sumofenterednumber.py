sum=0
rev=0
number=int(input("enter the number:"))
while (number):
    digit=number%10
    sum+=digit
    rev=rev*10+digit
    number=number//10
print("reverse of number is :",rev)    
print("sum of digit of the number is :",sum)