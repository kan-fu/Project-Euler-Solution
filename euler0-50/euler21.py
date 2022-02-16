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

    def solve(self, N=10000):
        """
        See https://mathschallenge.net/index.php?section=faq&ref=number/sum_of_divisors for more info
        on how to calculate the sum of divisors. Basically, given the the unique prime factorization
        n = p1^q1 * p2^q2 * ... * pn^q,
        d[n] = d[p1^q1] * d[p2^q2] * ... * d[pn^q^n]
        For p^q, the divisors are 1, p, p^2, ... , p^q, so the sum is (1-p^(q+1))/(1-p).
        The result minus the number itself is the sum of the proper divisors.
        """
        from sympy.ntheory import factorint
        import math

        d = {}
        for n in range(1, N):
            factors = factorint(n)
            d[n] = (
                math.prod((p ** (q + 1) - 1) // (p - 1) for p, q in factors.items()) - n
            )
        ans = 0
        for a, b in d.items():
            if a != b and b in d and d[b] == a:
                ans += a
        return ans


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
