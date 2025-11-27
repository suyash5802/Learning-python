import numpy as np
import matplotlib as plt

import utils as ut

A=np.array([[1,2],[3,4]])
e1 = np.array([1,2])  
e2 = np.array([2,1])

ut.plot_transformation(A, e1, e2, vector_name='e');

A_eig=np.linalg.eig(A)

print(f"Matrix A:\n{A} \n\nEigenvalues of matrix A:\n{A_eig[0]}\n\nEigenvectors of matrix A:\n{A_eig[1]}")

ut.plot_transformation(A, A_eig[1][:,0], A_eig[1][:,1]);
