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

    def solve(self, N=10001):
        """
        According to https://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number,
        pn / n < log n + log log n for n >= 6, where pn is the nth prime number
        """
        import math
        from collections.abc import Iterator

        upper_bound = max(6, int(N * (math.log(N) + math.log(math.log(N)))))

        def sieve(upTo: int) -> Iterator[int]:
            """
            Generate primes upto (including) given number

            >>> list(sieve(10))
            [2, 3, 5, 7]
            >>> list(sieve(11))
            [2, 3, 5, 7, 11]
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
            for p in range(2, upTo + 1):
                if primes[p]:
                    yield p

        gen_sieve = sieve(upper_bound)
        for _ in range(N - 1):
            next(gen_sieve)
        return next(gen_sieve)

    def solve2(self, N=10001):
        from sympy import prime

        return prime(N)


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
