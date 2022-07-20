x=[[17,72],[43,14],[45,65]]
trans=[[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        trans[j][i]=x[i][j]
for k in trans:
    print(k)        
    