# coding: utf-8


def voting(a):
    """返回投票过半数的人，为0时代表不存在这样的人"""
    m = 0
    count = 0
    for i in range(len(a)):
        if count == 0:
            m = a[i]
            count += 1
        else:
            if m == a[i]:
                count += 1
            else:
                count -= 1
    if count == 0:
        return 0
    count = a.count(m)
    return m if int(count * 1.0 / len(a) + 0.5) else 0


if __name__ == "__main__":
    assert voting([1, 8, 1, 100, 1]) == 1
    assert voting([1, 2, 1, 2, 3]) == 0
