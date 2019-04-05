# coding: utf-8


def matrix_product(a, b):
    """矩阵乘积"""
    length = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(0, length)) for j in range(0, length)]
            for i in range(0, length)]
    """等同于如下句子，但更快"""
    # m = []
    # for i in range(0, length):
    #     t = []
    #     for j in range(0, length):
    #         s = 0
    #         for k in range(0, length):
    #             s += a[i][k] * b[k][j]
    #         t.append(s)
    #     m.append(t)
    # return m


def matrix_power(m, n):
    """矩阵自乘"""
    if n == 0:
        length = len(m)
        t = [[0] * length for i in range(0, length)]
        for i in range(0, length):
            t[i][i] = 1
        return t
    if n & 1:   # n 是奇数
        t = matrix_power(m, n - 1)
        return matrix_product(m, t)
    else:
        temp = matrix_power(m, n >> 1)
        return matrix_product(temp, temp)


def fast_fibonacci(n):
    if n <= 2:
        return 1
    m = matrix_power([[1, 1], [1, 0]], n - 2)
    return m[0][0] + m[0][1]


if __name__ == "__main__":
    for i in range(1, 10):
        print(i, fast_fibonacci(i))
