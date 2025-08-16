def solve(n=600851475143):
    """ """

    from collections.abc import Iterator

    def rev_sieve(up_to: int) -> Iterator[int]:
        """
        Reversely generate primes upto (including) given number

        >>> list(rev_sieve(10))
        [7, 5, 3, 2]
        >>> list(rev_sieve(11))
        [11, 7, 5, 3, 2]
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
        for p in reversed(range(2, up_to + 1)):
            if primes[p]:
                yield p

    up_to = int(n ** (1 / 2))
    largest_prime_cand = None  # largest prime factor that is smaller than sqrt(N)
    for p in rev_sieve(up_to):
        if n % p == 0:
            if largest_prime_cand is None:
                # record only once since the primes are reversed
                largest_prime_cand = p
            while n % p == 0:
                # cancel the prime factor
                n //= p

    return largest_prime_cand if n == 1 else n


def solve2(n=600851475143):
    """
    sympy has functions to generate primes. Also primes can be looped in a non-reversed order
    """
    from sympy import sieve

    sqrt_n = int(n ** (1 / 2))
    largest_prime_cand = 0  # largest prime factor that is smaller than sqrt(N)
    for p in sieve.primerange(sqrt_n):
        if n % p == 0:
            largest_prime_cand = p
            while n % p == 0:
                n //= p
    return largest_prime_cand if n == 1 else n


def solve3(n=600851475143):
    from sympy.ntheory import factorint

    factors = factorint(n)
    return max(factors.keys())


if __name__ == "__main__":
    print(solve())
    print(solve2())
    print(solve3())
