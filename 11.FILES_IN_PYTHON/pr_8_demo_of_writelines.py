colors=["red\n","blue\n","green\n","yellow"]
str=""" this is the first line
this is the second line
this is the thirs line"""
myfile=open("python2.txt","w")
myfile.writelines(str)
myfile.writelines(colors)
myfile.close()