# coding: utf-8


def string_edit(a, b):
    m = len(a)
    n = len(b)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m):
        dp[i + 1][0] = dp[i][0] + 1
    for i in range(n):
        dp[0][i + 1] = dp[0][i] + 1
    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                dp[i + 1][j + 1] = dp[i][j]
            else:
                dp[i + 1][j + 1] = min(dp[i + 1][j] + 1, dp[i][j + 1] + 1, dp[i][j] + 2)
    return dp[m][n]


if __name__ == "__main__":
    assert string_edit('abcd', 'xbyd') == 4
    assert string_edit('abc', '') == 3
    assert string_edit('abc', 'ac') == 1
    assert string_edit('abcd', 'efcg') == 6
