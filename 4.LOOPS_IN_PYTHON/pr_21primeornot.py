num=int(input("enter the number:"))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print("this is not a prime number")
            break
    else:
        print("this is a prime number")
else:
    print("this is not a prime number")            
