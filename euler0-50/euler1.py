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
        return sum([i for i in range(0, N) if i % 3 == 0 or i % 5 == 0])

    def solve2(self, N=1000):
        arithmetic_sum = lambda x, p: p / 2 * (x // p) * (x // p + 1)
        return (
            arithmetic_sum(N - 1, 3)
            + arithmetic_sum(N - 1, 5)
            - arithmetic_sum(N - 1, 15)
        )


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
