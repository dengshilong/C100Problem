# coding: utf-8


def factor(n):
    s = ''
    p = 2
    while n > 1 and n >= p:
        if n % p == 0:
            count = 0
            while n % p == 0:
                n = int(n / p)
                count += 1
            s += '{}({})'.format(p, count)
        p += 1
    return s


if __name__ == "__main__":
    print(factor(72))
    print(factor(181944))
