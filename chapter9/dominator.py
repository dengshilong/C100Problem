# coding: utf-8


def dominator(x):
    s = [0] * len(x)
    top = -1
    i = 0
    result = []
    while i < len(x):
        if top >= 0 and x[i] >= s[top]:
            result.append((s[top], x[i]))
            top -= 1
        else:
            top += 1
            s[top] = x[i]
            i += 1
    return result


if __name__ == "__main__":
    assert dominator([2, 1, 3, 5, 4]) == [(1, 3), (2, 3), (3, 5)]
    assert dominator([5, 4, 3, 2, 1, 6]) == [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6)]
    assert dominator([2, 3, 3]) == [(2, 3), (3, 3)]
