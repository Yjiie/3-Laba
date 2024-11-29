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

# Функция вывода матриц
def print_matrix(matrix):
    for row in matrix:
        print("|", end='')
        for element in row:
            print("{:3}".format(element), end=' ')
        print("|")
    print("")

# Операции над матрицами (сложение, вычитание, умножение)
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

# Функция транспонирования матрицы
def transpose_matrix(matrix, len_matrix):
    transposed = [[0 for _ in range(len_matrix)] for _ in range(len_matrix)]
    for i in range(len_matrix):
        for j in range(len_matrix):
            transposed[j][i] = matrix[i][j]
    return transposed

# Функция для создания верхнего треугольника
def create_upper_triangle(N):
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    value = 1
    for i in range(N):
        for j in range(i + 1):
            matrix[i][j] = value
            value += 1
    return matrix

# Функция для создания нижнего треугольника
def create_lower_triangle(N):
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    value = 1
    for i in range(N):
        for j in range(N - i):
            matrix[i][N - j - 1] = value
            value += 1
    return matrix

# Вводим значение K и размер матрицы N
K = int(input("Введите число K: "))
while True:
    N = int(input("Введите размер матрицы N (6 <= N <= 50): "))
    if 6 <= N <= 50:
        break
    else:
        print("Ошибка: Размер матрицы должен быть не меньше 6 и не больше 50.")

# Генерация верхнего и нижнего треугольников
upper_triangle_matrix = create_upper_triangle(N)
lower_triangle_matrix = create_lower_triangle(N)

# Выводим верхний и нижний треугольники
print("Верхний треугольник:")
print_matrix(upper_triangle_matrix)

print("Нижний треугольник:")
print_matrix(lower_triangle_matrix)

SIZE_submat = N // 2

# Подсчет чисел, меньших K в нечетных столбцах в области 3 (матрица B)
count_region3 = 0
for row in range(SIZE_submat):
    for column in range(SIZE_submat):
        if (column % 2 != 0) and upper_triangle_matrix[row][column] < K:
            count_region3 += 1

# Сумма чисел в четных строках в области 2 (матрица C)
sum_region2 = 0
for row in range(SIZE_submat):
    for column in range(SIZE_submat, N):
        if row % 2 == 0:
            sum_region2 += lower_triangle_matrix[row][column - SIZE_submat]

# Создаем матрицу F, которая является копией матрицы A (верхний треугольник)
matrix_F = [[item for item in row] for row in upper_triangle_matrix]

# Проверяем условие и меняем местами области
if count_region3 > sum_region2:
    for row in range(SIZE_submat):
        for column in range(SIZE_submat):
            if (column % 2 != 0) and (row % 2 == 0):
                matrix_F[row][column], matrix_F[SIZE_submat - 1 - row][SIZE_submat - 1 - column] = \
                    matrix_F[SIZE_submat - 1 - row][SIZE_submat - 1 - column], matrix_F[row][column]
else:
    for row in range(SIZE_submat):
        for column in range(SIZE_submat):
            matrix_F[row][column], matrix_F[row + SIZE_submat][column + SIZE_submat] = \
                matrix_F[row + SIZE_submat][column + SIZE_submat], matrix_F[row][column]

# Выводим матрицу F после всех изменений
print("Матрица F после всех изменений:")
print_matrix(matrix_F)

# Вычисляем выражение ((K*A)*F – K*A^T)
matrix_KA = operations_matrix(upper_triangle_matrix, K, '*', N)
print("Матрица K*A:")
print_matrix(matrix_KA)

matrix_KAF = operations_matrix(matrix_KA, matrix_F, '*', N)
print("Матрица (K*A)*F:")
print_matrix(matrix_KAF)

matrix_AT = transpose_matrix(upper_triangle_matrix, N)
print("Матрица A^T:")
print_matrix(matrix_AT)

matrix_KAT = operations_matrix(matrix_AT, K, '*', N)
print("Матрица K*A^T:")
print_matrix(matrix_KAT)

result = operations_matrix(matrix_KAF, matrix_KAT, '-', N)
print("Результат ((K*A)*F – K*A^T):")
print_matrix(result)


