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

    def solve(self, N=2000000):
        """
        For hackerrank (https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem),
        generate primes upto 10**6, calculate prefix sum of the primes, then use binary search to
        find the largest index that is smaller than or equal to the given n, print the corresponding
        prefix sum.

        primes = list(sieve(10**6))
        prefix_sum = [primes[0]] * len(primes)
        for i in range(1, len(primes)):
            prefix_sum[i] = prefix_sum[i-1] + primes[i]
        t = int(input().strip())
        for a0 in range(t):
            n = int(input().strip())
            left, right = 0, len(primes) - 1
            while left < right:
                mid = (left + right + 1) // 2
                if primes[mid] <= n:
                    left = mid
                else:
                    right = mid - 1
            print(prefix_sum[left])
        """

        from collections.abc import Iterator

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

        return sum(sieve(N))

    def solve2(self, N=2000000):
        from sympy import sieve

        return sum(sieve.primerange(N))


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
