# coding: utf-8

"""
把蓝色当成1、白色当成2、红色当成3
i代表1的代表从左到右的位置
k代表3从右到左的位置
"""


def three_flag(x):
    i = 0
    j = 0
    k = len(x) - 1
    while j <= k:
        if x[j] == 1:
            if i != j:
                x[i], x[j] = x[j], x[i]
            i += 1
            j += 1
        elif x[j] == 3:
            x[k], x[j] = x[j], x[k]
            k -= 1
        else:
            j += 1


if __name__ == "__main__":
    x = [2, 1, 1, 3, 2, 1, 3, 2]
    three_flag(x)
    print(x)
