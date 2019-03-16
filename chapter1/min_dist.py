# coding: utf-8

import sys


def min_dist(x, y):
    i = 0
    j = 0
    result = sys.maxsize
    while i < len(x) and j < len(y):
        if x[i] >= y[j]:
            result = min(result, x[i] - y[j])
            j += 1
        else:
            result = min(result, y[j] - x[i])
            i += 1
    return result


if __name__ == "__main__":
    x = [4, 10, 13]
    y = [2, 6, 8]
    print(min_dist(x, y))
