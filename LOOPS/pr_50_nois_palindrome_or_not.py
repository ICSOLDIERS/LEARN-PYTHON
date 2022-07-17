# check the entered number is palindrome or not
num=int(input("enter the number:"))
temp=num
rev_num=0
while temp>0:
    rev_num=rev_num*10 +(temp%10)
    temp//=10
if num == rev_num:
    print("this is a palindrome number")    
else:
    print("this is not a palindrome number")    