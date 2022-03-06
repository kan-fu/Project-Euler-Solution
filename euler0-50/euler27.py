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

    def solve(self, N=1000):
        """
        let n be 0 and 1, we know that b and 1+a+b has to be prime, which also means b and
        1+a+b has to be larger than 1, and a has to be odd. Also when n=b, the n^2+an+b cannot
        be a prime number, so length of prime chain (n) is less than b.
        """
        from sympy import sieve
        from sympy.ntheory import isprime

        max_len, aa, bb = 0, 0, 0
        for b in sieve.primerange(N):
            for a in range(-b, b + 1, 2):
                # exclude if n=1 and n=2 are not primes
                if not isprime(1 + a + b) or not isprime(4 + 2 * a + b):
                    continue
                chain_len = 0
                for n in range(3, b):
                    # already checked the first three n before
                    if not isprime(n * n + a * n + b):
                        break
                    chain_len += 1
                if chain_len > max_len:
                    max_len = chain_len
                    aa, bb = a, b
        return aa * bb


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
