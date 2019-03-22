# coding: utf-8


def recursion_power(m, n):
    if n == 0:
        return 1
    if n & 1 == 1:  # n 是奇数
        return m * recursion_power(m, n - 1)
    else:
        return recursion_power(m, n >> 1) ** 2


if __name__ == "__main__":
    for i in range(1, 10):
        for j in range(1, 10):
            assert recursion_power(i, j) == i ** j
    print(recursion_power(3, 4))
