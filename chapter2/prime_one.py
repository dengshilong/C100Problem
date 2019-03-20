# coding: utf-8
import math


def _is_prime(n, primes):
    if n % 2 == 0 or n % 3 == 0:
        return False
    for p in primes:
        s = int(math.sqrt(n)) + 1
        if p > s:
            break
        if n % p == 0:
            return False
    return True


def prime_one(n):
    primes = [2, 3, 5]
    i = 7
    step = 2
    while i <= n:
        if _is_prime(i, primes):
            primes.append(i)
        step = 6 - step
        i += step
    return primes



if __name__ == "__main__":
    print(prime_one(40))
