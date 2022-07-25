line_number=3
filename=input("enter the filename to read:")
myfile=open(filename,"r")
currentline=1
for line in myfile:
    if currentline==line_number:
        print(line)
        break
    currentline+=1
