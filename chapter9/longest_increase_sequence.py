# coding: utf-8


def longest_increase_sequence(a):
    dp = [0] * (len(a) + 1)
    dp[1] = a[0]
    length = 1
    for item in a:
        if item > dp[length]:
            length += 1
            dp[length] = item
        else:
            for i in range(length, 0, -1):
                if dp[i-1] <= item < dp[i]:
                    break
            dp[i] = item
    return length


if __name__ == "__main__":
    assert longest_increase_sequence([1, 3, 5, 7, 8, 2, 9, 4, 10, 6]) == 7
    assert longest_increase_sequence([2, 3, -1, 2, 3, 4]) == 4



