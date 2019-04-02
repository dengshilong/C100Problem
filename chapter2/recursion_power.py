# coding: utf-8


def recursion_power(m, n):
    if n == 0:
        return 1
    if n & 1:  # n 是奇数
        return m * recursion_power(m, n - 1)
    else:
        temp = recursion_power(m, n >> 1)
        return temp * temp


if __name__ == "__main__":
    for i in range(1, 10):
        for j in range(1, 10):
            assert recursion_power(i, j) == i ** j
    print(recursion_power(3, 4))
