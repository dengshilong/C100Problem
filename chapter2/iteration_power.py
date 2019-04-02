# coding: utf-8


def iteration_power(m, n):
    p = 1
    while n > 0:
        if n & 1:
            p *= m
        n = n >> 1
        m = m * m
    return p


if __name__ == "__main__":
    for i in range(1, 10):
        for j in range(1, 10):
            assert iteration_power(i, j) == i ** j
    print(iteration_power(3, 4))
