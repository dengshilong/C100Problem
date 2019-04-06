# coding: utf-8


def iteration_fibonacci(n):
    if n <= 2:
        return 1
    a = 1
    b = 1
    while n > 2:
        a, b = b, a + b
        # 等同于如下语句
        # t = a + b
        # a = b
        # b = t
        n -= 1
    return b


if __name__ == "__main__":
    for i in range(1, 10):
        print(i, iteration_fibonacci(i))
