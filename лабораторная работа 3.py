from random import randint


def f(fun):
    def g(n, *args):
        a = fun(*args)
        return ('не ОК', 'ОК')[
            all(map(lambda x: a[x[0]][x[1]] == a[x[1]][x[0]], ((i, j) for i in range(n) for j in range(n))))]

    return g


@f
def h(*args):
    return args


n = int(input('Введите размерность матрицы: '))
arr = [[randint(0, 100) for col in range(n)] for row in range(n)]
[print(*i, sep='\t') for i in arr]

print(h(n, *arr))
