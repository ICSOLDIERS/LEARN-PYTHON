'''
*
**
***
****
*****           '''

num=int(input("enter the number to form pyramid:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()   