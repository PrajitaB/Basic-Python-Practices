# Matrix Multiplication
def matrix(r, c):
    Matrix = []
    for i in range(0, r):
        n = []
        for j in range(0, c):
            op = int(input())
            n.append(op)
        Matrix.append(n)
    return Matrix
def mul(A, B):
    C = []
    for i in range(0, len(A)):
        C.append([])
    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            C[i].append(j)
            C[i][j] = 0
    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            for k in range(0, len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C
p = int(input("Enter the number of rows of the 1st matrix : "))
q = int(input("Enter the number of column of 1st matrix or the number of rows of the 2nd matrix : "))
r = int(input("Enter the number of column of the 2nd matrix : "))
print("Enter the first matrix : ")
A = matrix(p, q)
print("Enter the second matrix : ")
B = matrix(q, r)
print("The resultant matrix : ")
multi = mul(A, B)
for z in multi:
    print(z)