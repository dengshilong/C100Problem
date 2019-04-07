# coding: utf-8


def bad_given_sum(n):
    result = []
    mid = int(n / 2)
    for i in range(1, mid + 1):
        s = i
        for j in range(i + 1, mid + 1 + 1):
            s += j
            if s == n:
                result.append((i, j))
    return result


def given_sum(n):
    result = []
    i = 1
    j = i + 1
    s = i + j
    mid = int(n / 2)
    while i <= mid and j <= mid + 1:
        if s > n:
            s -= i
            i += 1
        else:
            if s == n:
                result.append((i, j))
            j += 1
            s += j
    return result


if __name__ == "__main__":
    print(bad_given_sum(27))
    print(bad_given_sum(10000))
    print(given_sum(27))
    print(given_sum(10000))

