# coding: utf-8


def gt_count(f, g):
    i = 0
    j = 0
    result = 0
    while i < len(f) and j < len(g):
        if f[i] > g[j]:
            result += len(f) - i
            j += 1
        else:
            i += 1
    return result


if __name__ == "__main__":
    f = [1, 3, 5, 7, 9]
    g = [2, 3, 4, 7, 8]
    print(gt_count(f, g))

