import numpy as np

b = np.random.randn(2)
a = np.random.rand(2)
print(a,'\n',b)

c = np.diag(np.arange(1, 10, 2))
print(c[4][4])
print(c[1])
print(c.shape, c.ndim)

x = c[2] 
y = np.sin(x)*np.sin(x) + np.cos(x)*np.cos(x)
print(y)
x1 = c[2][2] 
y1 = np.sin(x1)*np.sin(x1) + np.cos(x1)*np.cos(x1)

matrix = np.empty((2,2))
matrix[0] = a
matrix[1] = b
print(np.linalg.eigvals(matrix))

mat = np.loadtxt("src/lib/file.txt")
print(mat)