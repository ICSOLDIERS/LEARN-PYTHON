import scipy as sp


item=input("enter the item name:")
sp_cost=float(input("enter the selling price of item:"))
gst_rate=float(input("enter the gst rate:"))
cgst=sp_cost*((gst_rate/2)/100)
sgst=cgst
amt=sp_cost+cgst+sgst
print("cgst (@",(gst_rate/2),"%): ",(cgst))
print("sgst (@",(gst_rate/2),"%): ",(sgst))
print("total ammount payable:",amt)

