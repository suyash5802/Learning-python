        #it allows Numpy to perform operations on Numpy
#with different shapes by virtually expanding dimensions 
#  so that they match the larger array's shape
#The dimension have the same size
#one of the dimension has a s
import numpy as np

a=np.array([
    [4, -3, 1],
        [2, 1, 3],
        [-1, 2, -5]
],dtype=np.dtype(float))

print(a)

b=np.array([-10,0,17],dtype=np.dtype(float))

x=np.linalg.solve(a,b)
print(f"Solution  {x}")




