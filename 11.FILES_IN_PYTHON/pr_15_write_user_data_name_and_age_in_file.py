ch="y"
f=open("python5.txt","a")
while ch=="y" or ch=="Y":
    name=input("enter your name:")
    age=int(input('enter your age:'))
    f.write(name)
    f.write("\n")
    f.write(str(age))
    f.write("\n")
    print("data saved successfully!")
    ch=input("do you want to add more records (y/n):")
f.close()    

