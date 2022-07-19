a=input("enter the sstring:")
a=a.split()
lar=a[0]
max_len=len(a[0])
for i in a:
    if len(i)>max_len:
        max_len=len(i)
        lar=i
print(lar)        