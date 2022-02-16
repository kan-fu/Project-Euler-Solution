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

    def solve(self, N=28123):
        """
        Use the same method in euler 21 to calculate sum of proper divisors.
        """
        from sympy.ntheory import factorint
        import math

        abundant = []
        for n in range(1, N):
            factors = factorint(n)
            if (
                math.prod((p ** (q + 1) - 1) // (p - 1) for p, q in factors.items())
                > 2 * n
            ):
                abundant.append(n)
        ans, can_sum = 0, set()
        for i, n1 in enumerate(abundant):
            for n2 in abundant[i:]:
                if n1 + n2 > N:
                    # abundant is inherantly sorted, so we can exit early, no need to
                    # store number that is beyond 28123
                    break
                # can_sum set stores all the numbers that can be written
                # as the sum of two abundant numbers
                can_sum.add(n1 + n2)
        for n in range(N):
            if n not in can_sum:
                ans += n
        return ans


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
