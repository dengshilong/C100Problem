# coding: utf-8


def longest_common_subsequence(a, b):
    dp = [[0] * len(b) for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    i = len(a) - 1
    j = len(b) - 1
    res = []
    while i >= 0 and j >= 0:
        if a[i] == b[j]:
            res.append(a[i])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1
    return ''.join(res)[::-1]


if __name__ == "__main__":
    assert longest_common_subsequence('abcd', 'e') == ''
    assert longest_common_subsequence('abcd', 'bwdb') == 'bd'
    assert longest_common_subsequence('asdf', 'bsedf') == 'sdf'
    assert longest_common_subsequence('sdsdfsd', 'bsdfsedf') == 'sdsdf'