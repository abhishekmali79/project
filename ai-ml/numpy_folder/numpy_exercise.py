import numpy as np

array1 = np.array([1,2,3]) # 1D array
array2 = np.array([4,5,6]) 
mat = np.array([[1,2,3],[4,5,6],[7,8,9]]) # 2D array or matrix

print(array1)
print(array2)
print(mat)

print("\n")

# special array creation
zeros = np.zeros((3,3)) # matrix filled with zeros
ones = np.ones((2,3))
range = np.arange(0,10,2)
linspace = np.linspace(0,1,5) 



print(zeros)
print(ones)
print(range)
print(linspace)

print("\n")

# array properties
print(array1.ndim,array2.ndim,mat.ndim) # number of dimentions
print(array1.shape,array2.shape,mat.shape) # rows, coloumns
print(array1.size,array2.size,mat.size) #total elements
print(array1.dtype,array2.dtype,mat.dtype) #data type

print("\n")

# mathmatical operations
print(array1+array2)
print(array1-array2)
print(array1*array2)
print(array1/array2)
print(array1%array2)

print("\n")

# reshaping arrays
mat = mat.reshape(1,9)
print(mat)
mat = mat.reshape(3,3)

print("\n")

# slicinng
print(mat)
print(mat[:,1])
print(mat[1,:])
print(mat[1:,1:])

print("\n")

# matrix multiplication
print(mat@mat)

print("\n")

#matrix transpose
print(mat.T)

print("\n")

# masking
print(mat)
print(mat[mat > 5])

print("\n")

# conditional selection
print(np.where(mat>5,mat,0))

print("\n")

# broadcasting (important)
arr = mat + array1
print(arr)

print("\n")

# aggregation with axis
print(np.sum(mat,axis=0))
print(np.mean(mat))
print(np.var(mat))
print(np.std(mat))

print("\n")

# random numbers 
rng = np.random.default_rng(42)

rng_uniform = rng.integers(0,5,size=(3,3))
rngn = rng.normal(0,1,(3,3))

print(rng_uniform)
print(rngn)