def solve(n=10001):
    """
    According to https://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number,
    pn / n < log n + log log n for n >= 6, where pn is the nth prime number
    """
    import math
    from typing import Generator

    upper_bound = max(6, int(n * (math.log(n) + math.log(math.log(n)))))

    def sieve(up_to: int) -> Generator[int]:
        """
        Generate primes upto (including) given number

        >>> list(sieve(10))
        [2, 3, 5, 7]
        >>> list(sieve(11))
        [2, 3, 5, 7, 11]
        """
        primes = [True for _ in range(up_to + 1)]
        primes[0] = False
        primes[1] = False
        p = 2
        while p * p <= up_to:
            if primes[p]:
                for i in range(p * 2, up_to + 1, p):
                    primes[i] = False
            p += 1
        for p in range(2, up_to + 1):
            if primes[p]:
                yield p

    gen_sieve = sieve(upper_bound)
    for _ in range(n - 1):
        next(gen_sieve)
    return next(gen_sieve)


def solve2(n=10001):
    from sympy import prime

    return prime(n)


if __name__ == "__main__":
    print(solve())
    print(solve2())
