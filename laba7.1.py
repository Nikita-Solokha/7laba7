import random
def a(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n-i-1):
            if matrix[0][j] < matrix[0][j+1]:
                for k in range(n):
                    matrix[k][j], matrix[k][j+1] = matrix[k][j+1], matrix[k][j]
    return matrix
def b(d):
    matrix = []
    for _ in range(d):
        lisst = []
        for _ in range(d):
            lisst.append(random.randint(1, 100))
        matrix.append(lisst)
    return matrix
def c(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()
d = int(input("Введите размер матрицы: "))
matrix = b(d)
print("after:")
c(matrix)
e = a(matrix)
print("before:")
c(e)

