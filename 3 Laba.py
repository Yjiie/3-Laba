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
import random


# Функция вывода матриц
def print_matrix(matrix):
    for row in matrix:
        print("|", end='')
        for element in row:
            print("{:3}".format(element), end=' ')
        print("|")
    print("")


def count_in_area_3(matrix):
    res = 0
    for row in range(SIZE_submat-1, SIZE_submat//2, -1):
        for column in range(SIZE_submat - row, row):
            if ((column + 1) % 2 != 0) and matrix[row][column] < K:
                res += 1
    return res


def count_in_area_2(matrix):
    res = 0
    for row in range(1, SIZE_submat//2 + SIZE_submat % 2):
        for column in range(SIZE_submat - 1, SIZE_submat - 1 - row, -1):
            if (column + 1) % 2 == 0:
                res += matrix[row][column]
                if row != SIZE_submat - 1 - row:
                    res += matrix[SIZE_submat - 1 - row][column]
    return res


def replace_arrays_3_and_2(matrix):
    for row in range(SIZE_submat-1, SIZE_submat//2, -1):
        for column in range(SIZE_submat - row, row):
            matrix[row][column], matrix[column][row] = \
                matrix[column][row], matrix[row][column]
    return matrix


# Операции над матрицами
def operations_matrix(matrix1, matrix2, sign, len_matrix):
    # Создаем пустую матрицу для результата
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


# Транспонирование матрицы
def transpose_matrix(matrix, len_matrix):
    # Создаем новую пустую матрицу для хранения результата
    transposed = [[0 for _ in range(len_matrix)] for _ in range(len_matrix)]
    # Транспонируем матрицу
    for i in range(len_matrix):
        for j in range(len_matrix):
            transposed[j][i] = matrix[i][j]
    return transposed


# ==============================================================================================================
#                                                   Начало реализации
# ==============================================================================================================

# Вводим значения K и N с клавиатуры
K = int(input("Введите размер K: "))
while True:
    N = int(input("Введите размер матрицы N: "))
    if 6 <= N <= 50:
        break  # Выход из цикла, если введено корректное значение
    else:
        print("Ошибка: Размер матрицы должен быть не меньше 6 и не больше 50.")       # Иначе программа не имеет смысла

# Создаем пустую матрицу A(N, N)
matrix_A = [[0 for _ in range(N)] for _ in range(N)]

# Определяем размер каждой подматрицы
SIZE_submat = N // 2


# Заполняем матрицу A(N, N) случайными числами
for row in range(N):
    for column in range(N):
        matrix_A[row][column] = random.randint(-10, 10)

''' Заполняем матрицу для тестирования, размер 10x10
N = 10
matrix_A = [
 [1, 2, 3, 4, 5, -5, -4, -3, -2, -1],
 [1, 2, 3, 4, 5, -5, -4, -3, -2, -1],
 [1, 2, 3, 4, 5, -5, -4, -3, -2, -1],
 [1, 2, 3, 4, 5, -5, -4, -3, -2, -1],
 [1, 2, 3, 4, 5, -5, -4, -3, -2, -1],
 [1, 2, 3, 4, 5, -5, -4, -3, -2, -1],
 [1, 2, 3, 4, 5, -5, -4, -3, -2, -1],
 [1, 2, 3, 4, 5, -5, -4, -3, -2, -1],
 [1, 2, 3, 4, 5, -5, -4, -3, -2, -1],
 [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]
]
'''
# Этап №1. Выводим матрицу A
print("Матрица A(N, N):")
print_matrix(matrix_A)

# Этап №2. Создаем и заполняем подматрицу B
matrix_B = [[0 for _ in range(SIZE_submat)] for _ in range(SIZE_submat)]
for row in range(SIZE_submat):
    matrix_B[row] = matrix_A[row][SIZE_submat + N % 2:]
print("Матрица B:")
print_matrix(matrix_B)


# Подсчет чисел меньше К в нечетных столбцах в области 3
count_area_3 = count_in_area_3(matrix_B)
# Подсчет суммы чисел в области 2
count_area_2 = count_in_area_2(matrix_B)

# Выводим результаты подсчета
print("Чисел меньше К в области 3:", count_area_3)
print("Сумма чисел в области 2:", count_area_2)


# Создаем и заполняем матрицу F
matrix_F = [[item for item in row] for row in matrix_A]

# если количество чисел в 3 области больше
if count_area_3 > count_area_2:
    matrix_E = [[0 for _ in range(SIZE_submat)] for _ in range(SIZE_submat)]
    for row in range(SIZE_submat):
        matrix_E[row] = matrix_A[row][:SIZE_submat]
    print("Матрица E:")
    print_matrix(matrix_E)

    # меняем в E симметрично области 3 и 2 местами
    matrix_E = replace_arrays_3_and_2(matrix_E)

    print("Матрица E после замены местами области 3 и 2 симметрично:")
    print_matrix(matrix_E)

    for row in range(SIZE_submat):
        matrix_F[row][:SIZE_submat] = matrix_E[row]
else:
    # меняем B и E несимметрично
    for row in range(SIZE_submat):
        matrix_F[row][SIZE_submat + N % 2:], matrix_F[row][:SIZE_submat] = \
            matrix_F[row][:SIZE_submat], matrix_F[row][SIZE_submat + N % 2:]

print("Матрица F после всех изменений: ")
print_matrix(matrix_F)

print("Произведение K*A: ")
mult_KA = operations_matrix(matrix_A, K, '*', N)
print_matrix(mult_KA)

print("Суммирование матриц (K * A * F): ")
mult_KAF = operations_matrix(mult_KA, matrix_F, '*', N)
print_matrix(mult_KAF)

print("Транспонирование матрицы (A^T): ")
trans_A = transpose_matrix(matrix_A, N)
print_matrix(transpose_matrix(matrix_A, N))

print("Произведение K * A^T: ")
mult_KAT = operations_matrix(trans_A, K, '*', N)
print_matrix(mult_KAT)


print("итоговый результат ((F+A)*A^T – K * F): ")
end_result = operations_matrix(mult_KAF, mult_KAT, '-', N)

for row in end_result:
    print("|", end='')
    for element in row:
        print("{:5}".format(element), end=' ')
    print("|")
print("")




