def matrix(r, c):
    A = []
    for i in range(r):
        n = []
        for j in range(c):
            op = int(input())
            n.append(op)
        A.append(n)
    return A
def transpose(A):
    result = list()
    for i in range(len(A[0])):
        k = []
        for j in range(len(A)):
            k.append(A[j][i])
        result.append(k)
    return result
r = int(input("Enter the number of rows : "))
c = int(input("Enter the number of column : "))
print("Enter the matrix : ")
A = matrix(r,c)
print("The resultant matrix : ")
trans = transpose(A)
for x in trans:
    print(x)