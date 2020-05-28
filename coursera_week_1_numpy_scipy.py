import numpy as np
from scipy import linalg


# numpy.unique
x = np.array([[3, 3, 3], [1, 3, 4], [7, 1, 3]], float)
np.unique(x)

# reverse array and return element with index 4
z = np.array([92, 13, 44, 555, 1, -3], float)
rev_array = z[::-1]
index = rev_array[4]

# scalar product of two vectors
a = np.ones(5)
b = np.linspace(2, 2, 5)
_sum = np.dot(a, b)

# product of two matrices and return the diagonal elements of the resulting matrix
a = np.array([[0, 9, 19, 13], [1, 20, 5, 13], [12, 11, 3, 4]], float)
b = np.array([[2, 0, 0, 0], [1, 2, 2, 0], [2, 1, 1, 0], [0, 0, 1, 1]], float)
c = np.dot(a, b)
diagonal = np.diag(c, k=0)

# average value of array elements
b = np.array([[-1, 33, 4, 1], [0, 1, 1, 0]], float)
average = np.average(b)

# determinant
a = np.array([[6, 0, 3], [0, -1, 2], [12, 3, 0]])
det = np.linalg.det(a)  # 0 --> linearly independent (numpy)
det_1 = linalg.det(a)  # 0 --> linearly independent (skipy)

# matrix eigenvalues
a = np.array([[1, -1, -1, 0], [-1, 2, -1, -1], [-1, -1, 2, -1], [0, -1, -1, 1]])
eigenvalues = linalg.eig(a)

# inverse matrix and trace of the inverse matrix (the sum of the elements of the main diagonal)
a = np.array([[2, 4, 0, 4, 1], [2, 4, 1, 1, 0], [1, 1, 1, 2, 2], [0, 1, 3, 2, 4], [2, 2, 2, 0, 2]])
inverse = linalg.inv(a)  # (skipy)
inverse_1 = np.linalg.inv(a)  # (numpy)
trace = np.trace(inverse)


