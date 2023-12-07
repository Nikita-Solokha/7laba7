import random
n = int(input("Введите размер матрицы: "))
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    matrix.append(row)
for i in range(n):
    for j in range(n):
        matrix[i][j] = random.randint(-10, 10)
print("Матрица:")
for row in matrix:
    print(row)
count = 0
for i in range(n):
    for j in range(n):
        if j > n - i - 1 and matrix[i][j] < 0:
            count += 1
print("Количество отрицательных элементов ниже побочной диагонали:", count)

