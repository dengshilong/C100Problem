# coding: utf-8

def knapasck(a, k):
    """求解背包问题，如果有解，dp[i][j]用来记录前i个物品里，解的最后一个物品"""
    n = len(a)
    dp = [[False] * (k + 1) for i in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        for j in range(k + 1):
            if dp[i - 1][j]:    # 如果前i - 1个已经得到解，则前i个的解也得到了
                dp[i][j] = dp[i - 1][j]
            elif j >= a[i - 1] and dp[i - 1][j - a[i - 1]]:
                dp[i][j] = a[i - 1]
    res = []
    if dp[n][k]:
        i = n
        while k > 0 and i > 0:
            res.append(dp[i][k])
            i -= 1
            k -= dp[i][k]
    res.reverse()
    return res


if __name__ == "__main__":
    assert knapasck([1, 2, 4, 7, 10, 12, 13, 15, 17], 27) == [1, 4, 10, 12]
    assert knapasck([1, 5, 10, 15, 20], 14) == []
