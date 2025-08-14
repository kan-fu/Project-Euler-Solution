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

    def solve(self, N=4 * 10**6):
        a, b = 1, 2
        ans = 0
        while b < N:
            if b % 2 == 0:
                ans += b
            b, a = a + b, b
        return ans


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
