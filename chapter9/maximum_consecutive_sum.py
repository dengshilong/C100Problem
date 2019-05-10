# coding: utf-8


def bad_method(x):
    max_sum = 0
    for i in range(len(x)):
        s = 0
        for j in range(i, 0, -1):
            s += x[j]
            if s > max_sum:
                max_sum = s
    return max_sum


def maximum_consecutive_sum(x):
    max_sum = 0
    s = 0
    for i in range(len(x)):
        if s < 0:
            s = 0
        s += x[i]
        if s > max_sum:
            max_sum = s
    return max_sum


if __name__ == "__main__":
    x = [1, 2, -6, 3, -2, 4, -1, 3, 2, -4]
    print(bad_method(x))
    print(maximum_consecutive_sum(x))