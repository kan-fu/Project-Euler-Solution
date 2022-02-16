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
        The largest prime factor of N can not be larger than the square root of N,
        so we can generate primes up to squre root, and reverse find the first prime that is the factor of N
        """
        from sympy import sieve

        sqrtN = int(N ** (1 / 2)) + 1
        primes = list(sieve.primerange(sqrtN))
        for p in reversed(primes):
            if N % p == 0:
                return p

    def solve2(self, N=600851475143):
        from sympy.ntheory import factorint

        factors = factorint(600851475143)
        return max(factors.keys())


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
