list=[2,3,3,5,4,4,2,2]
print("original list:",list)
my_set=set(list)
d=dict.fromkeys(my_set,0)
# print ("dictionary with 0 values:")
print(d)
for n in list:
    d[n]+=1
print("element: frequency")
print(d)