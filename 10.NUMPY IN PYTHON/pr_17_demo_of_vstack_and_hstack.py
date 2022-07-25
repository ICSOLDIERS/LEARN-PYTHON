import numpy as np
x=np.array([[1,2,3],[4,5,6]])
y=np.array([[11,22,33],[44,55,66]])
print("array vertically concatenated\n:",np.vstack((x,y)))
print("array horizontally concatenated\n:",np.hstack((x,y)))