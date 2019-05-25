# coding: utf-8


def n_queen(n):
    visited = [[False] * n for i in range(0, n)]
    count = _n_queen(visited, n, 0, 0)
    return count


def _n_queen(visited, n, i, count):
    if i == n:
        count += 1
        return count
    for j in range(n):
        if judge(visited, n, i, j):
            visited[i][j] = True        # 可以放下皇后
            count = _n_queen(visited, n, i + 1, count)
            visited[i][j] = False       # 回溯
    return count


def judge(visited, n, i, j):
    """判断皇后能否放到i, j这个位置"""
    for k in range(n):
        if visited[i][k]:       # 检查行
            return False
        if visited[k][j]:       # 检查列
            return False

    # 左上角到右下角这条线判断
    t = 1
    while i - t >= 0 and j - t >= 0:
        if visited[i - t][j - t]:
            return False
        t += 1
    t = 1
    while i + t < n and j + t < n:
        if visited[i + t][j + t]:
            return False
        t += 1
    t = 1
    # 左下角到右上角这条线判断
    while i + t < n and j - t >= 0:
        if visited[i + t][j - t]:
            return False
        t += 1
    t = 1

    while i - t >= 0 and j + t < n:
        if visited[i - t][j + t]:
            return False
        t += 1
    return True


if __name__ == "__main__":
    n = 8
    for i in range(3, n + 1):
        print(i, n_queen(i))
