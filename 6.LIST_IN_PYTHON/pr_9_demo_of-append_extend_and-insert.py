from turtle import color


colors=['red','orange','green']
print("original list:",colors)

# append() method
colors.append("black")
print(colors)

# insert() method
colors.insert(2,'yellow')
print(colors)

# extend() method
color_new=['blue','pink']
colors.extend(color_new)
print(colors)