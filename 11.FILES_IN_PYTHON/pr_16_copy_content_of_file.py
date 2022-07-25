inp=open("python5.txt","r")
outp=open("python6.txt","w")
for line in inp:
    outp.write(line)     
print("1 file copied!")    
# now close the file
inp.close()
outp.close()