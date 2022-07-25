import numpy as np
a=np.array([[1,2,3],[3,4,5],[6,7,8]])
print("original array:")
print(a)
a=a.reshape(1,9)
print("after reshape:")
print(a)