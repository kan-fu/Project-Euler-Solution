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

    def isPal(self, n):
        return str(n) == str(n)[::-1]

    def solve(self, N=600851475143):
        return max(
            i * j
            for i in range(100, 1000)
            for j in range(100, 1000)
            if self.isPal(i * j)
        )


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
