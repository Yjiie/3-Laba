'''
С клавиатуры вводится два числа K и N.
Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
Для тестирования использовать не случайное заполнение, а целенаправленное.
Вариант 14
14.	Формируется матрица F следующим образом: если в В количество чисел, меньших К в нечетных столбцах в области 3 больше, чем сумма чисел в четных строках в области 2, 
то поменять в Е симметрично области 3 и 2 местами, иначе В и Е поменять местами несимметрично. При этом матрица А не меняется. 
После чего вычисляется выражение: ((К*A)*F– K*AT . Выводятся по мере формирования А, F и все матричные операции последовательно.
Вид матрицы A:
E B
D C

Каждая из матриц B,C,D,E имеет вид: 
                                       1
                                     4   2
                                       3


'''

def print_matrix(matrix):
    for row in matrix:
        print("|", end='')
        for element in row:
            print("{:3}".format(element), end=' ')
        print("|")
    print("")

def operations_matrix(matrix1, matrix2, sign, len_matrix):
    result = [[0 for _ in range(len_matrix)] for _ in range(len_matrix)]
    for row in range(len_matrix):
        for column in range(len_matrix):
            if sign == '+':
                result[row][column] = matrix1[row][column] + matrix2[row][column]
            elif sign == '-':
                result[row][column] = matrix1[row][column] - matrix2[row][column]
            elif sign == '*' and type(matrix2) == int:
                result[row][column] = matrix1[row][column] * matrix2
            else:
                for k in range(len_matrix):
                    result[row][column] += matrix1[row][k] * matrix2[k][column]
    return result

def transpose_matrix(matrix, len_matrix):
    transposed = [[0 for _ in range(len_matrix)] for _ in range(len_matrix)]
    for i in range(len_matrix):
        for j in range(len_matrix):
            transposed[j][i] = matrix[i][j]
    return transposed

K = int(input("Введите число K: "))
while True:
    N = int(input("Введите размер матрицы N: "))
    if 6 <= N <= 50:
        break
    else:
        print("Ошибка: Размер матрицы должен быть не меньше 6 и не больше 50.")

matrix_A = [[i * N + j for j in range(N)] for i in range(N)]
SIZE_submat = N // 2

print("Матрица A(N, N):")
print_matrix(matrix_A)

matrix_B = [row[:SIZE_submat] for row in matrix_A[:SIZE_submat]]
matrix_C = [row[SIZE_submat:] for row in matrix_A[SIZE_submat:]]
matrix_D = [row[:SIZE_submat] for row in matrix_A[SIZE_submat:]]
matrix_E = [row[SIZE_submat:] for row in matrix_A[:SIZE_submat]]

count_region3 = 0
for row in range(SIZE_submat):
    for column in range(SIZE_submat):
        if (column % 2 != 0) and matrix_B[row][column] < K:
            count_region3 += 1

sum_region2 = 0
for row in range(SIZE_submat):
    for column in range(SIZE_submat, N):
        if row % 2 == 0:
            sum_region2 += matrix_C[row][column - SIZE_submat]

matrix_F = [[item for item in row] for row in matrix_A]

if count_region3 > sum_region2:
    for row in range(SIZE_submat):
        for column in range(SIZE_submat):
            if (column % 2 != 0) and (row % 2 == 0):
                matrix_E[row][column], matrix_E[SIZE_submat - 1 - row][SIZE_submat - 1 - column] = \
                    matrix_E[SIZE_submat - 1 - row][SIZE_submat - 1 - column], matrix_E[row][column]
else:
    for row in range(SIZE_submat):
        for column in range(SIZE_submat):
            matrix_F[row][column], matrix_F[row + SIZE_submat][column + SIZE_submat] = \
                matrix_F[row + SIZE_submat][column + SIZE_submat], matrix_F[row][column]

print("Матрица F после всех изменений: ")
print_matrix(matrix_F)

matrix_KA = operations_matrix(matrix_A, K, '*', N)
print("Матрица K*A:")
print_matrix(matrix_KA)

matrix_KAF = operations_matrix(matrix_KA, matrix_F, '*', N)
print("Матрица (K*A)*F:")
print_matrix(matrix_KAF)

matrix_AT = transpose_matrix(matrix_A, N)
print("Матрица A^T:")
print_matrix(matrix_AT)

matrix_KAT = operations_matrix(matrix_AT, K, '*', N)
print("Матрица K*A^T:")
print_matrix(matrix_KAT)

result = operations_matrix(matrix_KAF, matrix_KAT, '-', N)
print("Результат ((K*A)*F – K*A^T):")
print_matrix(result)

