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
        See reference at https://mathworld.wolfram.com/FullReptendPrime.html
        Also check http://oeis.org/A001913 for a list of full reptend primes.
        Full Reptend Prime is a prime p for which 1/p has a maximal period
        decimal expansion of p-1 digits. Basically, this problem asks to find the largest
        full reptend prime under 1000. A prime p is full reptend iff 10 is a primitive
        root modulo p, which means that
            10^k=1 (mod p) 	for k=p-1 and no k less than this.
        For example, 7 is a full reptend prime since
        (10^1,10^2,10^3,10^4,10^5,10^6)=(3,2,6,4,5,1) (mod 7) because only 10^6=1 (mod 7)
        So we search from the largest primes p under 1000, and check whether there is a k below
        p - 1 that satisfy 10^k=1 (mod p).
        """
        from sympy import sieve

        primes = list(sieve.primerange(N))
        for p in reversed(primes):
            mod_prod = 1
            for k in range(1, p):
                mod_prod = (mod_prod * 10) % p
                if mod_prod == 1:
                    # we only want the modular to be 1 only when k is p - 1
                    if k == p - 1:
                        return p
                    break


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
