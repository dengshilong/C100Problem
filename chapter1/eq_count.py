# coding: utf-8


def eq_count(f, g):
    i = 0
    j = 0
    result = 0
    while i < len(f) and j < len(g):
        if f[i] == g[j]:
            i += 1
            j += 1
            result += 1
        elif f[i] > g[j]:
            j += 1
        else:
            i += 1
    return result


if __name__ == "__main__":
    f = [1, 3, 4, 7, 9]
    g = [3, 5, 7, 8, 10]
    print(eq_count(f, g))
