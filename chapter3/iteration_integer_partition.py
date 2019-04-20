# coding: utf-8


def partition(n):
    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][1] = 1
        dp[0][i] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i - j >= 0:
                dp[i][j] = dp[i - j][j] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    return dp[n][n]


if __name__ == "__main__":
    for i in range(1, 10):
        print(i, partition(i))