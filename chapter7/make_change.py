# coding: utf-8


def make_change(n, a):
    """n为零钱, a为钞票面额, 找零钱使用钞票数量最少"""
    dp = [n] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(len(a)):
            if i >= a[j]:
                dp[i] = min(dp[i], dp[i - a[j]] + 1)
    return dp[n]


def find_make_change(n, a):
    """n为零钱, a为钞票面额, 找零钱使用钞票数量最少的一种方法"""
    dp = [n] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(len(a)):
            if i >= a[j]:
                dp[i] = min(dp[i], dp[i - a[j]] + 1)
    res = []
    i = n
    while i > 0:
        for j in range(len(a) - 1, -1, -1):
            if i >= j and dp[i] == dp[i - a[j]] + 1:
                res.append(a[j])
                i -= a[j]
                break
    return res


if __name__ == "__main__":
    n = 20
    a = [1, 2, 3, 4]
    for i in range(1, n + 1):
        print(i, make_change(i, a), find_make_change(i, a))
