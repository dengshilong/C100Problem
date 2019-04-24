# coding: utf-8


def integer_partition_method(n):
    return _integer_partition_method(n, n)


def _integer_partition_method(n, m):
    """n的分割中,最大值为m的分割方式"""
    if m == 1:
        return [[1] * n]
    res = []
    if n == m:
        res.append([n])
    elif n > m:
        a = _integer_partition_method(n - m, m)
        for item in a:
            item.append(m)
            res.append(item)
    b = _integer_partition_method(n, m - 1)
    res.extend(b)
    return res


if __name__ == "__main__":
    for i in range(1, 10):
        print(i, integer_partition_method(i))
