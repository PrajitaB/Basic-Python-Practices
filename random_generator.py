import random

n = random.random()
print(n)

n = random.randint(1, 100)
print(n)

n = random.randrange(-100, 100, 2)
print(n)

n = random.uniform(50, 100)
print(n)

list = random.sample(range(1, 100), 20)
print(list)

list = [1, 2, 3, 4, 5]
random.shuffle(list)
print(list)
print(random.choice(list))
print(random.sample(list, 2))



#3x3 random matrix(0,1)
import random
def random_matrix(r, c):
    M = []
    for i in range(r):
        N = []
        for j in range(c):
            N.append(random.random())
        M.append(N)
    return M
matrix = random_matrix(3, 3)
print("3x3 random generated matrix (0,1) : ")
for k in matrix:
    print(k)



#3x3 random matrix(-5,5)
import random
def random_matrix(r, c):
    M = []
    for i in range(r):
        N = []
        for j in range(c):
            N.append(random.randint(-5,5))
        M.append(N)
    return M
matrix = random_matrix(3, 3)
print("3x3 random generated matrix (-5,5) : ")
for k in matrix:
    print(k)



#user instructed random matrix
import random
def random_matrix(r, c, p, q):
    M = []
    for i in range(r):
        N = []
        for j in range(c):
            N.append(random.randint(p, q))
        M.append(N)
    return M
r = int(input("Enter the number of rows : "))
c = int(input("Enter the number of column : "))
p = int(input("Enter the minimum value of the matrix elements : "))
q = int(input("Enter the maximum value of the matrix elements : "))
matrix = random_matrix(r, c, p, q)
print("Random generated matrix : ")
for k in matrix:
    print(k)


#Random generation and user instructed extraction of matrix using numpy
import numpy as np

rows = int(input("Enter the number of rows : "))
cols = int(input("Enter the number of column : "))
p = int(input("Enter the minimum value of the matrix elements : "))
q = int(input("Enter the maximum value of the matrix elements : "))

random_matrix = np.random.uniform(low=p, high=q, size=(rows, cols))

print("Random Matrix:")
print(random_matrix)

r = int(input("Enter the starting row of extracted matrix : "))
rr = int(input("Enter the ending row of extracted matrix : "))
c = int(input("Enter the starting column of extracted matrix : "))
cc = int(input("Enter the ending column of extracted matrix : "))

extract_matrix = random_matrix[r:rr, c:cc]

print("Extracted Matrix:")
print(extract_matrix)

#Random extraction of given matrix using numpy
import numpy as np

matrix = np.array([[5.1,3.5,1.4,0.2],
[4.9,3.0,1.4,0.2],
[4.7,3.2,1.3,0.2],
[4.6,3.1,1.5,0.2],
[5.0,3.6,1.4,0.2],
[5.4,3.9,1.7,0.4],
[4.6,3.4,1.4,0.3],
[5.0,3.4,1.5,0.2],
[4.4,2.9,1.4,0.2],
[4.9,3.1,1.5,0.1],
[5.4,3.7,1.5,0.2],
[4.8,3.4,1.6,0.2],
[4.8,3.0,1.4,0.1],
[4.3,3.0,1.1,0.1],
[5.8,4.0,1.2,0.2],
[5.7,4.4,1.5,0.4],
[5.4,3.9,1.3,0.4],
[5.1,3.5,1.4,0.3],
[5.7,3.8,1.7,0.3],
[5.1,3.8,1.5,0.3],
[5.4,3.4,1.7,0.2],
[5.1,3.7,1.5,0.4],
[4.6,3.6,1.0,0.2],
[5.1,3.3,1.7,0.5],
[4.8,3.4,1.9,0.2],
[5.0,3.0,1.6,0.2],
[5.0,3.4,1.6,0.4],
[5.2,3.5,1.5,0.2],
[5.2,3.4,1.4,0.2],
[4.7,3.2,1.6,0.2],
[4.8,3.1,1.6,0.2],
[5.4,3.4,1.5,0.4],
[5.2,4.1,1.5,0.1],
[5.5,4.2,1.4,0.2],
[4.9,3.1,1.5,0.2],
[5.0,3.2,1.2,0.2],
[5.5,3.5,1.3,0.2],
[4.9,3.6,1.4,0.1],
[4.4,3.0,1.3,0.2],
[5.1,3.4,1.5,0.2],
[5.0,3.5,1.3,0.3],
[4.5,2.3,1.3,0.3],
[4.4,3.2,1.3,0.2],
[5.0,3.5,1.6,0.6],
[5.1,3.8,1.9,0.4],
[4.8,3.0,1.4,0.3],
[5.1,3.8,1.6,0.2],
[4.6,3.2,1.4,0.2],
[5.3,3.7,1.5,0.2],
[5.0,3.3,1.4,0.2],
[7.0,3.2,4.7,1.4],
[6.4,3.2,4.5,1.5],
[6.9,3.1,4.9,1.5],
[5.5,2.3,4.0,1.3],
[6.5,2.8,4.6,1.5],
[5.7,2.8,4.5,1.3],
[6.3,3.3,4.7,1.6],
[4.9,2.4,3.3,1.0],
[6.6,2.9,4.6,1.3],
[5.2,2.7,3.9,1.4],
[5.0,2.0,3.5,1.0],
[5.9,3.0,4.2,1.5],
[6.0,2.2,4.0,1.0],
[6.1,2.9,4.7,1.4],
[5.6,2.9,3.6,1.3],
[6.7,3.1,4.4,1.4],
[5.6,3.0,4.5,1.5],
[5.8,2.7,4.1,1.0],
[6.2,2.2,4.5,1.5],
[5.6,2.5,3.9,1.1],
[5.9,3.2,4.8,1.8],
[6.1,2.8,4.0,1.3],
[6.3,2.5,4.9,1.5],
[6.1,2.8,4.7,1.2],
[6.4,2.9,4.3,1.3],
[6.6,3.0,4.4,1.4],
[6.8,2.8,4.8,1.4],
[6.7,3.0,5.0,1.7],
[6.0,2.9,4.5,1.5],
[5.7,2.6,3.5,1.0],
[5.5,2.4,3.8,1.1],
[5.5,2.4,3.7,1.0],
[5.8,2.7,3.9,1.2],
[6.0,2.7,5.1,1.6],
[5.4,3.0,4.5,1.5],
[6.0,3.4,4.5,1.6],
[6.7,3.1,4.7,1.5],
[6.3,2.3,4.4,1.3],
[5.6,3.0,4.1,1.3],
[5.5,2.5,4.0,1.3],
[5.5,2.6,4.4,1.2],
[6.1,3.0,4.6,1.4],
[5.8,2.6,4.0,1.2],
[5.0,2.3,3.3,1.0],
[5.6,2.7,4.2,1.3],
[5.7,3.0,4.2,1.2],
[5.7,2.9,4.2,1.3],
[6.2,2.9,4.3,1.3],
[5.1,2.5,3.0,1.1],
[5.7,2.8,4.1,1.3],
[6.3,3.3,6.0,2.5],
[5.8,2.7,5.1,1.9],
[7.1,3.0,5.9,2.1],
[6.3,2.9,5.6,1.8],
[6.5,3.0,5.8,2.2],
[7.6,3.0,6.6,2.1],
[4.9,2.5,4.5,1.7],
[7.3,2.9,6.3,1.8],
[6.7,2.5,5.8,1.8],
[7.2,3.6,6.1,2.5],
[6.5,3.2,5.1,2.0],
[6.4,2.7,5.3,1.9],
[6.8,3.0,5.5,2.1],
[5.7,2.5,5.0,2.0],
[5.8,2.8,5.1,2.4],
[6.4,3.2,5.3,2.3],
[6.5,3.0,5.5,1.8],
[7.7,3.8,6.7,2.2],
[7.7,2.6,6.9,2.3],
[6.0,2.2,5.0,1.5],
[6.9,3.2,5.7,2.3],
[5.6,2.8,4.9,2.0],
[7.7,2.8,6.7,2.0],
[6.3,2.7,4.9,1.8],
[6.7,3.3,5.7,2.1],
[7.2,3.2,6.0,1.8],
[6.2,2.8,4.8,1.8],
[6.1,3.0,4.9,1.8],
[6.4,2.8,5.6,2.1],
[7.2,3.0,5.8,1.6],
[7.4,2.8,6.1,1.9],
[7.9,3.8,6.4,2.0],
[6.4,2.8,5.6,2.2],
[6.3,2.8,5.1,1.5],
[6.1,2.6,5.6,1.4],
[7.7,3.0,6.1,2.3],
[6.3,3.4,5.6,2.4],
[6.4,3.1,5.5,1.8],
[6.0,3.0,4.8,1.8],
[6.9,3.1,5.4,2.1],
[6.7,3.1,5.6,2.4],
[6.9,3.1,5.1,2.3],
[5.8,2.7,5.1,1.9],
[6.8,3.2,5.9,2.3],
[6.7,3.3,5.7,2.5],
[6.7,3.0,5.2,2.3],
[6.3,2.5,5.0,1.9],
[6.5,3.0,5.2,2.0],
[6.2,3.4,5.4,2.3],
[5.9,3.0,5.1,1.8]])

submatrix_rows = int(input("Enter the number of rows of the sub-matrix:"))
submatrix_cols = int(input("Enter the number of columns of the sub-matrix:"))
num = int(input("Enter the number of sub-matrix you want:"))
rows, cols = matrix.shape
submatrices = []

for n in range(num):
    start_row = np.random.randint(0, rows - submatrix_rows + 1)
    start_col = np.random.randint(0, cols - submatrix_cols + 1)
    submatrix = matrix[start_row:start_row + submatrix_rows, start_col:start_col + submatrix_cols]
    submatrices.append(submatrix)
for i, submatrix in enumerate(submatrices):
    print(f"Submatrix {i + 1}:")
    print(submatrix)