"""                                                 19.	Формируется матрица F следующим образом: если в Е количество нулей в нечетных столбцах в области 4,
B | C   Вид матрицы       2     Вид подматрицы      умноженное на К больше, чем произведение чисел в нечетных строках в области 1, то поменять в С симметрично
D | E                   1   3                       области 1 и 2 местами, иначе В и Е поменять местами несимметрично. При этом матрица А не меняется.
                          4                         После чего вычисляется выражение: A*F+ K* F T . Выводятся по мере формирования А, F и все матричные операции последовательно.
"""
import random


def submatrix(x, z):  # функция задания подматриц матрицы A
    b = [x[i][:(n // 2)] for i in range(n // 2)]
    c = [x[i][(n // 2 + z):n] for i in range(n // 2)]
    d = [x[i][:(n // 2)] for i in range(n // 2 + z, n)]
    e = [x[i][(n // 2 + z):n] for i in range(n // 2 + z, n)]
    return b, c, d, e


def print_matrix(x, description):  # функция вывода матрицы
    print(f"\n----{description}----")
    for c in range(n):
        for d in range(n):
            print(x[c][d], end='\t')
        print()

try:
    n = int(input("Задайте количество строк и столбцов N в матрице:\n"))
    while n < 6:
        n = int(input("Задайте количество строк и столбцов N в матрице:\n"))
    k = int(input("Задайте коэффициент K:\n"))

    A = [[0 if ((j == (n // 2) or i == (n // 2)) and n % 2 == 1) else random.randint(-10, 10) for j in range(n)] for i in range(n)]  # задание матрицы A
    print_matrix(A, 'A')
    ab, ac, ad, ae = submatrix(A, n % 2)
    F = []
    fb, fc, fd, fe = ab, ac, ad, ae
    #print(f"\nB = {ab}\nC = {ac}\nD = {ad}\nE = {ae}\n")

    e_cond = len([1 for j in range(len(ae)) for i in range(len(ae)) if (ae[i][j] == 0 and i > (len(ae) // 2) and (i > j > (len(ae) - i - 1)) and j % 2 == 0)])  # подсчёт нулей в нечетных столбцах E в области 4
    multiplic = 1  # переменная для произведения чисел в нечетных строках E в области 1

    for i in range(len(ae)):
        for j in range(len(ae)):
            if ((i < (len(ae) // 2) and (j < i)) or (i >= (len(ae) // 2) and j < (len(ae) - i - 1))) and (i + n // 2 + n % 2) % 2 == 0:
                multiplic *= ae[i][j]

    print(f"\nКоличество нулей в нечетных столбцах E в области 4 = {e_cond}\nПроизведение чисел в нечетных строках E в области 1 = {multiplic}")
    if e_cond * k > multiplic:
        for i in range(len(ac)):
            for j in range(len(ac)):
                if (i < (len(ac) // 2) and (i < j < (len(ac) - i - 1))):
                    fc[i][j], fc[j][i] = fc[j][i], fc[i][j]
    else:
        fb, fe = fe, fb

    for i in range(n):  # цикл задания матрицы F из её подматриц
        if n % 2 == 0:
            if i < (n // 2):
                F.append(fb[i] + fc[i])
            elif i >= (n // 2):
                F.append(fd[i - n//2] + fe[i - n//2])
        else:
            if i < (n // 2):
                F.append(fb[i] + [0] + fc[i])
            elif i == n // 2:
                F.append([0]*n)
            elif i > (n // 2):
                F.append(fd[i - n//2 - 1] + [0] + fe[i - n//2 - 1])
    print_matrix(F, 'F')

    B = [[0 for i in range(n)] for j in range(n)]  # результативная матрица произведения A и F
    for i in range(n):
        for j in range(n):
            B[i][j] = A[i][j] * F[i][j]
    print_matrix(B, 'A * F')

    F_t = F  # задание матрицы для транспонирования
    for i in range(n):
        for j in range(i, n):
            F_t[i][j], F_t[j][i] = F_t[j][i], F_t[i][j]
    print_matrix(F_t, 'F_t')

    F_t = [[j * k for j in i] for i in F_t]  # умножение транспонированной матрицы на коэф. К
    print_matrix(F_t, 'F_t * k')

    C = [[0 for i in range(n)] for j in range(n)]  # результативная матрица суммы A * F и F_t * k
    for i in range(n):
        for j in range(n):
            C[i][j] = B[i][j] + F_t[i][j]
    print_matrix(C, 'A * F + F_t * k')
except ValueError:
    print("Введённые данные не являются числом")