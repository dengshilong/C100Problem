# coding: utf-8


def sieve(n):
    """筛法得到n以内的素数"""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    i = 2
    while i * 2 <= n:
        if primes[i]:
            primes[i * 2:n + 1:i] = [False] * (int((n - i * 2) / i) + 1)
        i += 1
    return [i for i in range(n + 1) if primes[i]]


if __name__ == "__main__":
    print(sieve(200))
