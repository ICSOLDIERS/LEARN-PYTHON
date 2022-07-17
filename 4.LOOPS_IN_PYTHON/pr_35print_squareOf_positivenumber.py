while True:
    num=int(input("enter  the integer for square or zero for exit:"))
    if num<0:
        continue
    if num==0:
        break
    if num>0:
        print("square of integer is :",num**2)
print("GOOD BYE!")        