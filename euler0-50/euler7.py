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

    def solve(self, N=10001):
        from sympy import prime

        return prime(N)


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
