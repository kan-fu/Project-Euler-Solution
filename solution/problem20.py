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

    def solve(self, N=100):
        import math

        return sum(map(int, str(math.factorial(N))))


if __name__ == "__main__":
    solver = Solution()
    print(solver.answer, solver.time)
