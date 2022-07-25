print("enter 'x' for exit." )
filename=input("enter the filename with extension to read:")
if filename=="x":
    exit()
else:
    r=open(filename,"r")    
    print("\nthe file",filename,"opened successfully!")
    print("the file",filename,"contains:\n")
    print("*"*50)
    print(r.read())
    r.close()
    print("*"*50)


