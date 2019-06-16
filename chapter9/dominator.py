# coding: utf-8


def dominator(x):
    s = [0] * len(x)
    top = -1
    dom = [-1] * len(x)     # -1代表不存在支配元素
    for i in range(len(x)):
        while top >= 0 and x[i] >= x[s[top]]:
            dom[s[top]] = i
            top -= 1
        top += 1
        s[top] = i
    return dom


if __name__ == "__main__":
    assert dominator([2, 1, 3, 5, 4]) == [2, 2, 3, -1, -1]
    assert dominator([5, 4, 3, 2, 1, 6]) == [5, 5, 5, 5, 5, -1]
    assert dominator([2, 3, 3]) == [1, 2, -1]