# coding: utf-8


def direct(n):
    return _direct(1, n)


def _direct(i, n):
    if i > n:
        return ['']
    else:
        s = []
        result = _direct(i, n - 1)
        s.extend(result)
        for item in result:
            s.append(item + str(n))
        return s


if __name__ == "__main__":
    print(direct(3))
