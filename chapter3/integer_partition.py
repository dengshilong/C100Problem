# coding: utf-8

def integer_partition(n):
    return _integer_partition(n, n)


def _integer_partition(n, m):
    """n的分割中,最大值为m的分割总数"""
    if n < 0:
        return 0
    if n == 0 or m == 1:
        return 1
    return _integer_partition(n - m, m) + _integer_partition(n, m - 1)


if __name__ == "__main__":
    for i in range(1, 10):
        print(i, integer_partition(i))
