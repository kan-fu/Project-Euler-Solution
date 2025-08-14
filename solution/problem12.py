class Solution:
    def __init__(self):
        import time

        start = time.time()
        self.answer = self.solve(993)
        elapse = time.time() - start
        if elapse > 1:
            self.time = f"{elapse:.1f}s"
        else:
            self.time = f"{elapse*1000:.1f}ms"

    def solve(self, N=500):
        """
        Given the unique prime factorization n = p1^q1 * p2^q2 * ... * pn^qn,
        the number of factors can be calculated by (1+q1)(1+q2)...(1+qn).
        The reason behind it is that every factor of n must be in the form
        p1^r1 * p2^r2 * ... * pn^rn where 0<=ri<=qi, which has 1+qi options to choose.
        According to the principle of multiplication, the total number of factors is
        the product of all these choices.

        Triangle number has the form n*(n+1)/2, so we can factor n/2 and n+1 when n is even
        or (n+1)/2 and n when n is odd.
        """
        from collections import Counter
        from itertools import count

        import numpy as np
        from sympy.ntheory import factorint

        for n in count(1):
            if n % 2 == 0:
                counter = Counter(factorint(n // 2)) + Counter(factorint(n + 1))
            else:
                counter = Counter(factorint((n + 1) // 2)) + Counter(factorint(n))
            number_of_factors = np.prod([r + 1 for r in counter.values()])
            if number_of_factors > N:
                return n * (n + 1) // 2

    def solve2(self, N=500, start=1):
        """
        No sympy solution. Estimated an upper bound first.
        At first, I could not pass the last two test cases in hackerrank. The trick is to sort the input number first.
        For n1 > n2, we have solve(n1) > solve(n2). For example, the first triangle number to have over 1000 divisors must be
        larger than the one to have over 999 divisors. When calculating solve(1000), we can utilize the return value n (not n*(n+1)//2)
        from solve(999), and set the start value to n, thus reducing repetitive computing. After calculating all the answers,
        sort it back to the original order.

        """
        import math
        from collections import Counter
        from collections.abc import Iterator
        from itertools import count

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

        def factorint(n: int) -> dict[int, int]:
            factors = {}
            for p in primes:
                if p > n:
                    break
                if n % p == 0:
                    q = 0
                    while n % p == 0:
                        q += 1
                        n //= p
                    factors[p] = q
            return factors

        # primes under 42000 are enough to deal with N=1000 in hackerrank
        primes = list(sieve(42000))
        for n in count(start):
            if n % 2 == 0:
                counter = Counter(factorint(n // 2)) + Counter(factorint(n + 1))
            else:
                counter = Counter(factorint((n + 1) // 2)) + Counter(factorint(n))
            number_of_factors = math.prod([r + 1 for r in counter.values()])
            if number_of_factors > N:
                return n * (n + 1) // 2


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
