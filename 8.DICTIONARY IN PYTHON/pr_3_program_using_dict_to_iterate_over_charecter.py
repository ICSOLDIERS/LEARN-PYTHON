sentence="Computer is a machine."
charecters={}
for charecter in sentence:
    charecters[charecter]=charecters.get(charecter,0)+1
print(charecters)    