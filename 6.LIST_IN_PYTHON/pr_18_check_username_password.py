database=['ajay',1234],['Suman','2345'],['Abhishek','3456'],['Vivek','4444']
username=input("enter username:")
password=input("enter password:")
if [username,password] in database:
    print("Access granted")
else:
    print("Access denied!")    