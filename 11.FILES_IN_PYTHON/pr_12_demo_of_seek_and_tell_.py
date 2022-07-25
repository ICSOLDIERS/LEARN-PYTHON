text=["\ndifferent ","color","name"]
myfile=open("python3.txt",mode="a+")
myfile.writelines(text)
print("position of the file cursor:",myfile.tell())
myfile.seek(20)
for line in myfile:
    print(line)