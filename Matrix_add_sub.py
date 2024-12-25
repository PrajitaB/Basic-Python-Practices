#Matrix addition and subtraction
def matrix(r, c):
    Matrix = []
    for i in range(r):
        n = []
        for j in range(c):
            op = int(input())
            n.append(op)
        Matrix.append(n)
    return Matrix
def add(A, B):
    result = []
    for r in range(len(A)):
        p = []
        for c in range(len(B[0])):
            p.append(A[r][c] + B[r][c])
        result.append(p)
    return result
def sub(A, B):
    res = []
    for r in range(len(A)):
        q = []
        for c in range(len(B[0])):
            q.append(A[r][c] - B[r][c])
        res.append(q)
    return res
r = int(input("Enter the number of rows : "))
c = int(input("Enter the number of column : "))
print("Enter the first matrix : ")
A = matrix(r,c)
print("Enter the second matrix : ")
B = matrix(r,c)
operation = int(input("Enter the option : 1.Addition 2.Subtraction : "))
print("The resultant matrix : ")
if operation==1 :
    sum = add(A, B)
    for x in sum:
        print(x)
elif operation==2 :
    diff = sub(A, B)
    for y in diff:
        print(y)
else:
    print("Invalid Choice.")