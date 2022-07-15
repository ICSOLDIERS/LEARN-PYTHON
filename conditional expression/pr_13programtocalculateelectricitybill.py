units=int(input("enter the total unit consumed:"))
if units>500:
    ammount=units*9.25
    surcharge=80
elif units>300:
    ammount=units*7.25    
    surcharge=70
elif units>200:
    ammount=units*5.25  
    surcharge=30
else:
    ammount=units*2.25    
    surcharge=20
billtotal=ammount+surcharge    
print("your total bill is = %.2f"%billtotal)       