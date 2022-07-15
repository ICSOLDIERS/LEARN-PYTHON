name=input("enter  your name:")
salary=eval(input("enter your salary"))
if salary<=500000:
    taxamt=0.05*salary
elif salary<=600000:
    taxamt=0.7*salary
elif salary<=700000:
    taxamt=0.8*salary    
else:
    taxamt=0.10*salary    
print("name:",name,"salary:",salary,"taotal tax:",taxamt)    

