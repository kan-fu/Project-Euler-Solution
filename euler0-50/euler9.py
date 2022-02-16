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
        Pythagorean triple can be generated by
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = M ** 2 + n ** 2
        given an arbitrary pair of integers m and n with m > n > 0.
        Plug into a + b + c = 1000, we can get
            500 = m * (m + n) < 2 * m**2 => m >= 16
        So we have to factor 500 into two numbers with the smaller factor larger than 16.
        Turns out m can only be 20, which leads n to be 5
        """
        m, n = 20, 5
        a, b, c = m**2 - n**2, 2 * m * n, m**2 + n**2
        return a * b * c


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
