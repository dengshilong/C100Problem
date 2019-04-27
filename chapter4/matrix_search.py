def matrix_search(m, k):
    n = len(m)
    i = 0
    j = n - 1
    while i < n and j >= 0:
        if m[i][j] > k:
            j -= 1
        elif m[i][j] < k:
            i += 1
        else:
            return True
    return False


if __name__ == "__main__":
    m = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 24, 17, 24], [18, 21, 23, 26, 30]]
    print(matrix_search(m, 17))
    print(matrix_search(m, 25))
