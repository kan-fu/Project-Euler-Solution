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
        from sympy.ntheory import factorint
        from itertools import count
        from collections import Counter
        import numpy as np

        for n in count(1):
            if n % 2 == 0:
                counter = Counter(factorint(n // 2)) + Counter(factorint(n + 1))
            else:
                counter = Counter(factorint((n + 1) // 2)) + Counter(factorint(n))
            number_of_factors = np.prod([r + 1 for r in counter.values()])
            if number_of_factors > N:
                return n * (n + 1) // 2


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
