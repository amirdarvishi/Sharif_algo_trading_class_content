import numpy as np

# define two array 
a = np.array([1,3,5], dtype='int16')
b = np.array([[1,5,9,10],[2,6,7,9]])

# print arrays
print(a)
print(b)

# Dimension
print('dimension of a array: ',a.ndim)
print('dimension of b array: ',b.ndim)

# size
print(a.itemsize)
print(a.nbytes)

# print specific element
print(b[1,1])

# specific row 
print(b[1, :])
# column 
print(b[: ,2])

# initialize an array filled with zero
zero_matrix = np.zeros((5,5))
print(zero_matrix)

# initialize an array filled with one 
ones_matrix = np.ones((5,5))
print(ones_matrix)

ones_matrix = np.full((5,5),23)
print(ones_matrix)

random = np.random.rand(4,2)
print(random)

random_int = np.random.randint(1,23, size=(4,6))
print(random_int)


# math
print(b)
print(a + 2)
print(np.sum(b,axis=1))


# stacking 
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
print(np.vstack([v1,v1,v2,v1]))
print(np.hstack([v1,v2]))

