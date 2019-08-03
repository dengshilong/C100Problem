#coding: utf-8
from chapter3.gray_code import gray_code


def hanoi_tower(n):
    return _hanoi_tower(n, 1, 2, 3)


def _hanoi_tower(n, start, mid, end):
    if n == 1:
        print("Move disk %d from %d to %d" % (n, start, end))
    else:
        _hanoi_tower(n - 1, start, end, mid)
        print("Move disk %d from %d to %d" % (n, start, end))
        _hanoi_tower(n - 1, mid, start, end)


def get_moves(n):
    moves = []
    code = gray_code(n)
    for i in range(1, len(code)):
        for j in range(n):
            if code[i][j] != code[i - 1][j]:
                moves.append(n - j)
                break
    return moves


def itertion_hanoi_tower(n):
    moves = get_moves(n)
    cur = [1] * n
    for i in moves:
        start = cur[i - 1]
        end = (start + (n - i - 1) % 2) % 3 + 1
        cur[i - 1] = end
        print("Move disk %d from %d to %d" % (i, start, end))


if __name__ == "__main__":
    for i in range(1, 6):
        print(i)
        # hanoi_tower(i)
        itertion_hanoi_tower(i)
    itertion_hanoi_tower(4)
