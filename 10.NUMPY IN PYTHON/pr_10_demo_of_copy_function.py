import numpy as np
x=np.array([11,12,13])
y=x
z=np.copy(x)
x[0]=22
print(x)
print()
print(y)
print()
print(z)