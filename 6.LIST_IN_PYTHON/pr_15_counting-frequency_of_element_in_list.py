from xml.dom.minidom import Element


list=[]
print("enter list of five integer:")
for i in range(5):
    print("enter integer:",i)
    usrinput=int(input())
    list.append(usrinput)
print("the list is :",list)    
lenght=len(list)
element=int(input('enter the element:'))
c=0
for i in range(0,lenght-1):
    if element==list[i]:
        c+=1
if c==0:
    print(element,"not found in given list")        
else:
    print(element,"has frequency as",c,"in given list")    

