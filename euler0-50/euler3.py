class Solution:
    def __init__(self):
        import time

        start = time.time()
        self.answer = self.solve()
        elapse = time.time() - start
        if elapse > 1:
            self.time = f"{elapse:.1f}s"
        else:
            self.time = f"{elapse*1000:.1f}ms"

    def solve(self, N=600851475143):
        """
        It can be proved by contradiction that N can at most have one prime factor that is larger than sqrt(N).
        Given the unique prime factorization N = p1^q1 * p2^q2 * ... * pn^qn, where p1 < p2 < ... < pn, qi > 0,
        if we cancel the prime factors that is smaller than sqrt(N), there will be two cases:
        1. the largest prime factor pn <= int(sqrt(N)) (e.g., N = 9, 12)
            ==> the remaining N would be 1
        2. the largest prime factor pn > int(sqrt(N)) (e.g., N = 10, 17)
            ==> the remaining N would be pn (qn must be 1)
        So we can generate primes upto sqrt(N), and cancel these prime factors. In case 1, we need to additionally
        store the largest prime that is smaller than sqrt(N).
        """

        from collections.abc import Iterator

        def rev_sieve(upTo: int) -> Iterator[int]:
            """
            Reversely generate primes upto (including) given number

            >>> list(rev_sieve(10))
            [7, 5, 3, 2]
            >>> list(rev_sieve(11))
            [11, 7, 5, 3, 2]
            """
            primes = [True for _ in range(upTo + 1)]
            # primes[0] = False
            # primes[1] = False
            p = 2
            while p * p <= upTo:
                if primes[p]:
                    for i in range(p * 2, upTo + 1, p):
                        primes[i] = False
                p += 1
            for p in reversed(range(2, upTo + 1)):
                if primes[p]:
                    yield p

        upTo = int(N ** (1 / 2))
        largest_prime_cand = 0  # largest prime factor that is smaller than sqrt(N)
        for p in rev_sieve(upTo):
            if N % p == 0:
                if largest_prime_cand == 0:
                    # record only once since the primes are reversed
                    largest_prime_cand = p
                while N % p == 0:
                    # cancel the prime factor
                    N //= p

        return largest_prime_cand if N == 1 else N

    def solve2(self, N=600851475143):
        """
        sympy has functions to generate primes. Also primes can be looped in a non-reversed order
        """
        from sympy import sieve

        sqrtN = int(N ** (1 / 2))
        largest_prime_cand = 0  # largest prime factor that is smaller than sqrt(N)
        for p in sieve.primerange(sqrtN):
            if N % p == 0:
                largest_prime_cand = p
                while N % p == 0:
                    N //= p
        return largest_prime_cand if N == 1 else N

    def solve3(self, N=600851475143):
        from sympy.ntheory import factorint

        factors = factorint(600851475143)
        return max(factors.keys())


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
