# original dictionary
dict={"name":"Aman","class":"XII","year":2019}
print(dict)

# dictionary append with "streem"="science"
dict["stream"]="science"
print(dict)

# dictionary update with "stream"=commerce instead of science
dict.update({"stream":"commerce"})
print(dict)

del dict["class"]
print(dict)

dict.clear()
print(dict)

del dict
print(dict)