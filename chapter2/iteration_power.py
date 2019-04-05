# coding: utf-8


def iteration_power(m, n):
    p = 1
    while n > 0:
        if n & 1:
            p *= m
        n = n >> 1
        m = m * m
    return p


def iteration_power_two(m, n):
    p = 1
    while n >= 1:
        if n & 1:
            p *= m
            n -= 1
        else:
            m = m * m
            n = n >> 1
    return p


if __name__ == "__main__":
    for i in range(1, 10):
        for j in range(1, 10):
            assert iteration_power(i, j) == i ** j
            assert iteration_power_two(i, j) == i ** j
    print(iteration_power(3, 4))
    print(iteration_power_two(3, 4))
